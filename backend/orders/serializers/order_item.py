from rest_framework.serializers import ModelSerializer
from orders.models import OrderItem


class OrderItemSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ["id", "order", "product", "seller", "quantity"]
