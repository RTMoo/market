from rest_framework.serializers import ModelSerializer, SerializerMethodField
from carts.models import Cart
from .cart_item import CartItemSerializer


class CartSerializer(ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    total_price = SerializerMethodField()

    def get_total_price(self, obj):
        return sum(item.quantity * item.product.price for item in obj.items.all())

    class Meta:
        model = Cart
        fields = ["id", "user", "items", "total_price"]
