from rest_framework.serializers import ModelSerializer
from orders.models import Order
from .order_item import OrderItemSerializer


class OrderSerializer(ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = [
            "id",
            "buyer",
            "full_name",
            "phone_number",
            "to_address",
            "total_price",
            "status",
            "created_at",
            "items",
        ]
        read_only_fields = ["id", "buyer", "total_price", "status", "created_at"]
