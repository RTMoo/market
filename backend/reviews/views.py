from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from reviews.models import Review
from reviews.serializers import ReviewSerializer
from orders.models import OrderItem
from products.models import Product
from accounts.models import CustomUser
from django.core.cache import cache
from reviews.utils import clear_review_cache

@api_view(["GET"])
@permission_classes([AllowAny])
def get_product_reviews(request, product_id):
    """Получить список отзывов на конкретный товар"""
    cache_key = f"product_{product_id}_reviews"
    
    data = cache.get(cache_key)
    
    if not data:
        buyer_id = request.user.id if request.user.is_authenticated else None
        if buyer_id:
            # Отзыв текущего пользователя чтобы было удобнее работать с изменением отзыва
            buyer_review = Review.objects.filter(
                product_id=product_id, buyer_id=buyer_id
            ).first()

            # Все отзывы кроме текущего пользователя
            reviews = Review.objects.filter(product_id=product_id).exclude(
                buyer_id=buyer_id
            )
        else:
            buyer_review = None
            reviews = Review.objects.filter(product_id=product_id)

        buyer_review_data = (
            ReviewSerializer(instance=buyer_review).data if buyer_review else None
        )
        reviews_data = ReviewSerializer(instance=reviews, many=True).data

        data = {
            "reviews": reviews_data,
            "buyerReview": buyer_review_data,
        }
        
        cache.set(cache_key, data, 60 * 60)

    return Response(data=data, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_review(request):
    """Оставить отзыв, если пользователь купил товар"""

    serializer = ReviewSerializer(data=request.data)

    serializer.is_valid(raise_exception=True)
    validated_data = serializer.validated_data
    product_id = validated_data["product_id"]

    product = get_object_or_404(Product, id=product_id)
    buyer = get_object_or_404(CustomUser, id=request.user.id)

    # Проверяем, покупал ли пользователь товар и оставлял ли он отзыв
    has_bought = OrderItem.objects.filter(order__buyer=buyer, product=product).exists()
    has_reviewed = Review.objects.filter(buyer=buyer, product=product).exists()

    if not has_bought:
        return Response(
            {"detail": "Оставить отзыв можно только после покупки данного товара"},
            status=status.HTTP_403_FORBIDDEN,
        )

    if has_reviewed:
        return Response(
            {"detail": "Вы уже оставили отзыв на этот товар."},
            status=status.HTTP_403_FORBIDDEN,
        )

    review = Review.objects.create(
        buyer=buyer, product=product, **serializer.validated_data
    )

    clear_review_cache(product_id)

    return Response(ReviewSerializer(review).data, status=status.HTTP_201_CREATED)


@api_view(["PATCH"])
@permission_classes([IsAuthenticated])
def update_review(request, review_id):
    """Обновить отзыв (только владелец)"""

    review = Review.objects.filter(id=review_id).first()

    if not review:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if review.buyer_id != request.user.id:
        return Response(status=status.HTTP_403_FORBIDDEN)

    # Обновляем только переданные поля
    serializer = ReviewSerializer(review, data=request.data, partial=True)
    if serializer.is_valid():
        # Обновляем вручную
        for field, value in serializer.validated_data.items():
            setattr(review, field, value)
        review.save()

        clear_review_cache(review.product_id)

        data = ReviewSerializer(review).data
        return Response(data=data, status=status.HTTP_200_OK)

    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_review(request, review_id):
    """Удалить отзыв (только владелец или модератор)"""

    buyer_id = request.user.id
    review = Review.objects.filter(id=review_id).first()

    if not review:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if review.buyer_id != buyer_id:
        return Response(status=status.HTTP_403_FORBIDDEN)
    
    product_id = review.product_id
    review.delete()
    clear_review_cache(product_id)

    return Response(status=status.HTTP_204_NO_CONTENT)
