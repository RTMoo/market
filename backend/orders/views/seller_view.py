from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from orders.models import OrderItem, Order
from orders.serializers import OrderSerializer, OrderItemSerializer


class SellerOrderListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        seller_id = request.user.id
        orders = (
            Order.objects.filter(items__seller=seller_id)
            .distinct()
            .prefetch_related("items__product")
        )

        serializer = OrderSerializer(instance=orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SellerOrderDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, order_id):
        seller_id = request.user.id
        order = (
            Order.objects.filter(id=order_id).prefetch_related("items__product").first()
        )

        if not order:
            return Response(
                {"detail": "Order not found"}, status=status.HTTP_404_NOT_FOUND
            )

        # Фильтруем товары, оставляя только те, где seller_id = текущий продавец
        filtered_items = OrderItem.objects.filter(
            seller_id=seller_id, order=order
        ).select_related("product")

        order_data = OrderSerializer(order).data
        order_data["items"] = OrderItemSerializer(filtered_items, many=True).data

        # Вычисляем общую стоимость
        total_price = sum(
            i["quantity"] * i["product_price"] for i in order_data["items"]
        )
        order_data["total_price"] = total_price

        return Response(data=order_data, status=status.HTTP_200_OK)


class SellerOrderStatusUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, order_item_id):
        seller_id = request.user.id
        order_item = OrderItem.objects.filter(id=order_item_id).first()

        if not order_item:
            return Response(
                {"detail": "Элемент заказа не найден"},
                status=status.HTTP_404_NOT_FOUND,
            )

        if order_item.seller_id != seller_id:
            return Response(
                {"detail": "Элемент заказа не принадлежит вам"},
                status=status.HTTP_403_FORBIDDEN,
            )

        if order_item.status == OrderItem.Status.CANCELED:
            return Response(
                {"detail": "Заказ уже отменен, нельзя менять статус"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        item_status = request.data.get("status")

        if item_status in (OrderItem.Status.CANCELED, OrderItem.Status.SHIPPED):
            order_item.status = item_status
            order_item.save()
            return Response({"detail": "Статус обновлен"}, status=status.HTTP_200_OK)

        return Response(
            {"detail": "Неверное значение статуса"},
            status=status.HTTP_400_BAD_REQUEST,
        )
