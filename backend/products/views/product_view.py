from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from rest_framework.response import Response
from products.models import Product
from products.serializers import ProductSerializer
from products.utils import clear_product_cache, normalize_query_dict
from products.filters import ProductFilter, ALLOWED_FILTER_FIELDS
from commons.paginations import ProductPagination
from accounts.models import CustomUser
from django.core.cache import cache


@api_view(["GET"])
@permission_classes([AllowAny])
def get_product_list(request):
    filter_query = normalize_query_dict(
        request.query_params, allowed_fields=ALLOWED_FILTER_FIELDS
    )
    CACHE_KEY = f"paginator_{filter_query}"

    paginated_data = cache.get(CACHE_KEY)

    if not paginated_data:
        product_filter = ProductFilter(
            request.query_params,
            queryset=Product.objects.all().select_related("category"),
        )
        filtered_products = product_filter.qs

        paginator = ProductPagination()
        queryset = paginator.paginate_queryset(
            queryset=filtered_products, request=request
        )

        data = ProductSerializer(instance=queryset, many=True).data
        paginated_data = paginator.get_paginated_response(data).data

        cache.set(CACHE_KEY, paginated_data, 60 * 10)

    return Response(data=paginated_data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_product_detail(request, product_id):
    CACHE_KEY = f"product_{product_id}"
    product_data = cache.get(CACHE_KEY)

    if not product_data:
        product = (
            Product.objects.filter(id=product_id).select_related("category").first()
        )

        if not product:
            return Response(
                data="Нет такого продукта в базе данных",
                status=status.HTTP_404_NOT_FOUND,
            )

        product_data = ProductSerializer(instance=product).data
        cache.set(CACHE_KEY, product_data, timeout=60 * 10)

    return Response(data=product_data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_seller_product_list(request):
    seller_id = request.user.id
    CACHE_KEY = f"product_list_seller_{seller_id}"
    data = cache.get(CACHE_KEY)

    if not data:
        product = Product.objects.filter(seller_id=seller_id).select_related("category")
        data = ProductSerializer(instance=product, many=True).data
        cache.set(CACHE_KEY, data, timeout=60 * 10)

    return Response(data=data, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        seller_id = request.user.id
        seller = CustomUser.objects.filter(id=seller_id).first()

        if not seller:
            return Response(
                data="Такого продавца нет в базе данных",
                status=status.HTTP_404_NOT_FOUND,
            )

        if seller.role != CustomUser.Role.SELLER:
            return Response(
                data="Вы не можете создать продукт так как не являетесь продавцом",
                status=status.HTTP_403_FORBIDDEN,
            )

        validated_data = serializer.validated_data
        product = Product.objects.create(seller=seller, **validated_data)
        clear_product_cache(seller_id=seller_id)

        data = ProductSerializer(instance=product).data
        return Response(data=data, status=status.HTTP_201_CREATED)

    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PATCH"])
@permission_classes([IsAuthenticated])
def update_product(request, product_id):
    serializer = ProductSerializer(data=request.data, partial=True)

    if serializer.is_valid():
        validated_data = serializer.validated_data
        seller_id = request.user.id
        category_id = validated_data["category_id"]

        Product.objects.filter(id=product_id, seller_id=seller_id).update(
            **validated_data
        )
        clear_product_cache(seller_id=seller_id)

        product = Product.objects.filter(
            id=product_id, seller_id=seller_id, category_id=category_id
        ).first()
        data = ProductSerializer(instance=product).data

        return Response(data=data, status=status.HTTP_200_OK)

    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_product(request, product_id):
    seller_id = request.user.id
    is_deleted, _ = Product.objects.filter(id=product_id, seller_id=seller_id).delete()

    if is_deleted:
        clear_product_cache(seller_id=seller_id)
        return Response(status=status.HTTP_204_NO_CONTENT)

    return Response(status=status.HTTP_403_FORBIDDEN)
