from django.db import transaction
from rest_framework.serializers import ModelSerializer, ValidationError
from orders.models import Order, OrderItem
from .order_item import OrderItemSerializer
from carts.models import CartItem
from accounts.models import CustomUser


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
        read_only_fields = ["buyer", "total_price", "status", "created_at"]

    def create(self, validated_data):
        """Создание заказа из корзины"""
        user_id = self.context["request"].user.id

        cart_items = CartItem.objects.filter(cart__user_id=user_id).select_related(
            "product"
        )
        if not cart_items:
            raise ValidationError("Корзина пуста")

        with transaction.atomic():
            buyer = CustomUser.objects.filter(id=user_id).first()
            total_price = sum(item.product.price * item.quantity for item in cart_items)

            order = Order.objects.create(
                buyer=buyer,
                full_name=validated_data["full_name"],
                phone_number=validated_data["phone_number"],
                to_address=validated_data["to_address"],
                total_price=total_price,
            )

            order_items = [
                OrderItem(
                    order=order,
                    product=item.product,
                    seller=item.product.seller,
                    quantity=item.quantity,
                    price=item.product.price,
                )
                for item in cart_items
            ]
            OrderItem.objects.bulk_create(order_items)

            cart_items.delete()

        return order
