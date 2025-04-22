from django.db import transaction
from rest_framework.exceptions import ValidationError
from carts.models import CartItem
from carts.utils import delete_buyer_cart_cache
from orders.models import Order, OrderItem
from django.core.cache import cache


def get_order_cache(buyer_id):
    key = f"buyer_{buyer_id}_order_list"
    data = cache.get(key)

    return data


def set_order_cache(buyer_id, data):
    key = f"buyer_{buyer_id}_order_list"
    cache.set(key, data, 60 * 60)


def delete_order_cache(buyer_id):
    key = f"buyer_{buyer_id}_order_list"
    cache.delete(key)


def delete_all_seller_order_cache(order_items):
    """
    Удаляет все кэши продавцов связанных с товарами
    """

    for item in order_items:
        cache_key_seller = f"seller_{item.product.seller_id}_order_list"
        cache.delete(cache_key_seller)


def create_order(request, validated_data):
    buyer_id = request.user.id

    cart_items = list(
        CartItem.objects.select_related("product")
        .only("product_id", "product__price", "product__seller_id", "quantity")
        .filter(cart__buyer_id=buyer_id)
    )

    if not cart_items:
        raise ValidationError("Корзина пуста")

    with transaction.atomic():
        total_price = sum(item.product.price * item.quantity for item in cart_items)

        order = Order.objects.create(
            buyer_id=buyer_id,
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
        CartItem.objects.filter(cart__buyer_id=buyer_id).delete()

        # Очищаем кэш
        delete_all_seller_order_cache(order_items=order_items)
        delete_buyer_cart_cache(buyer_id=buyer_id)

        return order
