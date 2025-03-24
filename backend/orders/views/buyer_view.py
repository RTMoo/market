from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from orders.serializers import OrderSerializer
from orders.models import Order
from orders.utils import create_order


class OrderListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        buyer_id = request.user.id
        orders = Order.objects.filter(buyer=buyer_id).prefetch_related("items__product")

        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class OrderDetailView(APIView):
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


class OrderCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = OrderSerializer(data=request.data)

        if serializer.is_valid():
            create_order(request, serializer.validated_data)
            return Response(status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
