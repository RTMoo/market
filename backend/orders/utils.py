from django.db import transaction
from rest_framework.exceptions import ValidationError
from carts.models import CartItem
from orders.models import Order, OrderItem
from accounts.models import CustomUser


def create_order(request, validated_data):
    user_id = request.user.id

    cart_items = list(
        CartItem.objects.select_related("product")
        .only("product_id", "product__price", "product__seller_id", "quantity")
        .filter(cart__user_id=user_id)
    )

    if not cart_items:
        raise ValidationError("Корзина пуста")

    with transaction.atomic():
        total_price = sum(item.product.price * item.quantity for item in cart_items)

        order = Order.objects.create(
            buyer_id=user_id,
            full_name=validated_data["full_name"],
            phone_number=validated_data["phone_number"],
            to_address=validated_data["to_address"],
            total_price=total_price,
        )

        order_items = [
            OrderItem(
                order=order,
                product_id=item.product_id,
                seller_id=item.product.seller_id,
                quantity=item.quantity,
            )
            for item in cart_items
        ]

        OrderItem.objects.bulk_create(order_items)

        # Удаление товаров из корзины
        CartItem.objects.filter(cart__user_id=user_id).delete()

