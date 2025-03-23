from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from orders.models import OrderItem
from orders.serializers import OrderItemSerializer


class SellerOrderItemListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_id = request.user.id
        orders = OrderItem.objects.filter(seller=user_id)

        serializer = OrderItemSerializer(instance=orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SellerOrderItemUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, order_item_id):
        seller = request.user.id
        order_item = OrderItem.objects.filter(id=order_item_id).first()

        if not order_item:
            return Response(
                {"detail": "Элемент заказа не найден"},
                status=status.HTTP_404_NOT_FOUND,
            )

        if order_item.seller.id != seller:
            return Response(
                {"detail": "Элемент заказа не принадлежит вам"},
                status=status.HTTP_403_FORBIDDEN,
            )

        item_status = request.data.get("status")
        if item_status in (i[0] for i in OrderItem.Status.choices):
            order_item.status = item_status
            order_item.save()
            return Response({"detail": "Статус обновлен"}, status=status.HTTP_200_OK)

        return Response(
            {"detail": "Неверное значение статуса"},
            status=status.HTTP_400_BAD_REQUEST,
        )
