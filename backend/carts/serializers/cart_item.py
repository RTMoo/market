from rest_framework.serializers import (
    ModelSerializer,
    IntegerField,
    CharField,
    DecimalField,
    SerializerMethodField,
)

from carts.models import CartItem, Cart
from products.models import Product
from rest_framework.exceptions import PermissionDenied, ValidationError


class CartItemSerializer(ModelSerializer):
    product_id = IntegerField(write_only=True)
    product_name = CharField(source="product.name", read_only=True)
    product_price = DecimalField(
        source="product.price",
        read_only=True,
        decimal_places=2,
        coerce_to_string=False,
        max_digits=10,
    )
    total_item_price = SerializerMethodField()

    def get_total_item_price(self, obj):
        return obj.quantity * obj.product.price

    class Meta:
        model = CartItem
        fields = [
            "id",
            "product_id",
            "product_name",
            "product_price",
            "quantity",
            "seller",
            "total_item_price",
        ]
        read_only_fields = ["id", "total_item_price", "seller"]
