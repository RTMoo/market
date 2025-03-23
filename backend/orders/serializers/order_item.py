from rest_framework.serializers import (
    ModelSerializer,
    IntegerField,
    CharField,
    DecimalField,
)
from orders.models import OrderItem


class OrderItemSerializer(ModelSerializer):
    product_id = IntegerField(write_only=True)
    product_name = CharField(source="product.title", read_only=True)
    product_price = DecimalField(
        source="product.price",
        read_only=True,
        decimal_places=2,
        coerce_to_string=False,
        max_digits=10,
    )

    class Meta:
        model = OrderItem
        fields = [
            "id",
            "order",
            "seller",
            "quantity",
            "product_id",
            "product_name",
            "product_price",
            "status",
        ]
