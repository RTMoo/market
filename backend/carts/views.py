from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from carts.serializers import CartItemSerializer, CartSerializer
from carts.models import Cart, CartItem


class CartView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_id = request.user.id

        cart = (
            Cart.objects.filter(user_id=user_id)
            .prefetch_related("items__product")
            .first()
        )

        if not cart:
            return Response(
                {"detail": "Корзина не найдена"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = CartSerializer(instance=cart)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class CartAddView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = CartItemSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, cart_item_id):
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

        # Получаем элемент корзины и связанный с ним продукт

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

        # Проверяем наличие товара на складе
        if quantity > cart_item.product.stock:
            return Response(
                {
                    "detail": f"Максимально доступное количество: {cart_item.product.stock}"
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Обновляем количество в корзине
        cart_item.quantity = quantity
        cart_item.save()

        return Response({"quantity": "Количество обновлено"}, status=status.HTTP_200_OK)


class CartDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, cart_item_id):
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


class CartClearView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        user_id = request.user.id
        cart = Cart.objects.filter(user_id=user_id).first()
        if cart:
            CartItem.objects.filter(cart=cart).delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
