from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError, PermissionDenied

from carts.serializers import CartSerializer, CartItemSerializer
from carts.models import Cart, CartItem
from products.models import Product


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_cart_list(request):
    user_id = request.user.id

    cart = (
        Cart.objects.filter(user_id=user_id).prefetch_related("items__product").first()
    )

    if not cart:
        return Response(
            {"detail": "Корзина не найдена"}, status=status.HTTP_404_NOT_FOUND
        )

    cart_data = CartSerializer(instance=cart).data

    return Response(data=cart_data, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_cart_item(request):
    serializer = CartItemSerializer(data=request.data, context={"request": request})
    if not serializer.is_valid():
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    validated_data = serializer.validated_data
    user_id = request.user.id
    product_id = validated_data.pop("product_id")

    cart = Cart.objects.filter(user_id=user_id).first()
    product = Product.objects.filter(id=product_id).select_related("seller").first()

    if not product:
        raise ValidationError({"detail": "Продукт не найден"})

    if product.seller_id == user_id:
        raise PermissionDenied({"detail": "Нельзя добавить свои товары в корзину"})

    if not cart:
        raise ValidationError(
            {"detail": "Корзина не найдена, возможно вы не авторизованы"}
        )

    if CartItem.objects.filter(cart=cart, product=product).exists():
        raise ValidationError({"detail": "У вас уже есть такой товар в корзине"})

    cart_item = CartItem.objects.create(
        cart=cart, product=product, seller=product.seller, quantity=1
    )

    cart_data = CartItemSerializer(instance=cart_item).data

    return Response(data=cart_data, status=status.HTTP_201_CREATED)


@api_view(["PATCH"])
@permission_classes([IsAuthenticated])
def update_cart_item(request, cart_item_id):
    quantity = request.data.get("quantity")
    user_id = request.user.id

    if quantity is None:
        return Response(
            {"detail": "Не указано количество"}, status=status.HTTP_400_BAD_REQUEST
        )

    if quantity < 1:
        return Response(
            {"detail": "Количество должно быть больше 0"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    cart_item = (
        CartItem.objects.select_related("product")
        .filter(id=cart_item_id, cart__user_id=user_id)
        .first()
    )

    if not cart_item:
        return Response(
            {"detail": "Элемент корзины не найден"},
            status=status.HTTP_404_NOT_FOUND,
        )

    if quantity > cart_item.product.stock:
        return Response(
            {"detail": f"Максимально доступное количество: {cart_item.product.stock}"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    cart_item.quantity = quantity
    cart_item.save()

    return Response({"quantity": "Количество обновлено"}, status=status.HTTP_200_OK)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_cart_item(request, cart_item_id):
    user_id = request.user.id

    deleted_count, _ = CartItem.objects.filter(
        id=cart_item_id, cart__user_id=user_id
    ).delete()

    if deleted_count == 0:
        return Response(
            {"detail": "Элемент корзины не найден"},
            status=status.HTTP_404_NOT_FOUND,
        )

    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def clear_cart(request):
    user_id = request.user.id
    cart = Cart.objects.filter(user_id=user_id).first()
    if cart:
        CartItem.objects.filter(cart=cart).delete()

    return Response(status=status.HTTP_204_NO_CONTENT)
