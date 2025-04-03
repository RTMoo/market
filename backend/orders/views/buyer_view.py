from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from orders.serializers import OrderSerializer
from orders.models import Order, OrderItem
from orders.utils import create_order


class BuyerOrderListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        buyer_id = request.user.id
        orders = Order.objects.filter(buyer=buyer_id).prefetch_related("items__product")

        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BuyerOrderDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, order_id):
        buyer_id = request.user.id
        order = (
            Order.objects.filter(id=order_id, buyer=buyer_id)
            .prefetch_related("items__product")
            .first()
        )
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BuyerOrderCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = OrderSerializer(data=request.data)

        if serializer.is_valid():
            order = create_order(request, serializer.validated_data)
            data = OrderSerializer(instance=order).data

            return Response(data=data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BuyerOrderStatusUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, order_item_id):
        buyer_id = request.user.id
        order_item = (
            OrderItem.objects.filter(id=order_item_id).select_related("order").first()
        )

        if not order_item:
            return Response(
                {"detail": "Элемент заказа не найден"},
                status=status.HTTP_404_NOT_FOUND,
            )

        if order_item.order.buyer_id != buyer_id:
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

        if item_status in (OrderItem.Status.CANCELED, OrderItem.Status.DELIVERED):
            if (
                item_status == OrderItem.Status.DELIVERED
                and order_item.status != OrderItem.Status.SHIPPED
            ):
                return Response(
                    {"detail": "Нельзя доставить то что не отправлено, АУФ!"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            order_item.status = item_status
            order_item.save()
            return Response({"detail": "Статус обновлен"}, status=status.HTTP_200_OK)

        return Response(
            {"detail": "Неверное значение статуса"},
            status=status.HTTP_400_BAD_REQUEST,
        )
