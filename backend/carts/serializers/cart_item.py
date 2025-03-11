from rest_framework.serializers import (
    ModelSerializer,
    IntegerField,
    CharField,
    DecimalField,
    SerializerMethodField,
    ValidationError,
)
from carts.models import CartItem, Cart
from products.models import Product


class CartItemSerializer(ModelSerializer):
    product_id = IntegerField(write_only=True)
    product_name = CharField(source="product.title", read_only=True)
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
            "total_item_price",
        ]

    def create(self, validated_data):
        user = self.context["request"].user.id
        product_id = validated_data.pop("product_id")

        cart = Cart.objects.filter(user=user).first()
        product = Product.objects.filter(id=product_id).first()
        if not cart:
            raise ValidationError("Корзина не найдено, возможно вы не авторизованы")

        if not product:
            raise ValidationError("Продукт не найден")

        validated_data["product"] = product
        validated_data["cart"] = cart

        res = CartItem.objects.create(**validated_data)
        return res
