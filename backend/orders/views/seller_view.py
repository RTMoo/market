from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from orders.models import OrderItem, Order
from orders.serializers import OrderSerializer, OrderItemSerializer
from django.core.cache import cache


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def seller_order_list(request):
    seller_id = request.user.id
    cache_key = f"seller_{seller_id}_order_list"
    data = cache.get(cache_key)

    if not data:
        orders = (
            Order.objects.filter(items__seller=seller_id)
            .distinct()
            .prefetch_related("items__product")
        )

        data = OrderSerializer(instance=orders, many=True).data
        cache.set(cache_key, data, timeout=60 * 60)

    return Response(data=data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def seller_order_detail(request, order_id):
    seller_id = request.user.id
    cache_key = f"seller_{seller_id}_order_detail_{order_id}"

    order_data = cache.get(cache_key)

    if not order_data:
        order = (
            Order.objects.filter(id=order_id).prefetch_related("items__product").first()
        )
        if not order:
            return Response(
                {"detail": "Order not found"}, status=status.HTTP_404_NOT_FOUND
            )

        # Фильтруем товары, оставляя только те, где seller_id = текущий продавец
        filtered_items = OrderItem.objects.filter(
            seller_id=seller_id, order=order
        ).select_related("product")

        order_data = OrderSerializer(order).data
        order_data["items"] = OrderItemSerializer(filtered_items, many=True).data

        # Вычисляем общую стоимость
        total_price = sum(
            i["quantity"] * i["product_price"] for i in order_data["items"]
        )
        order_data["total_price"] = total_price

        cache.set(cache_key, order_data, timeout=60 * 60)

    return Response(data=order_data, status=status.HTTP_200_OK)


@api_view(["PATCH"])
@permission_classes([IsAuthenticated])
def seller_order_status_update(request, order_item_id):
    order_item = (
        OrderItem.objects.filter(id=order_item_id).select_related("order").first()
    )
    buyer_id = order_item.order.buyer_id
    seller_id = request.user.id

    if not order_item:
        return Response(
            {"detail": "Элемент заказа не найден"},
            status=status.HTTP_404_NOT_FOUND,
        )

    if order_item.seller_id != seller_id:
        return Response(
            {"detail": "Элемент заказа не принадлежит вам"},
            status=status.HTTP_403_FORBIDDEN,
        )

    if order_item.status == OrderItem.Status.CANCELED:
        return Response(
            {"detail": "Заказ уже отменен, нельзя менять статус"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    item_status = request.data.get("status")

    if item_status in (OrderItem.Status.CANCELED, OrderItem.Status.SHIPPED):
        order_item.status = item_status
        order_item.save()

        cache_key_buyer = f"buyer_{buyer_id}_order_detail_{order_item.order_id}"
        cache_key_seller = f"seller_{seller_id}_order_detail_{order_item.order_id}"

        cache.delete(cache_key_buyer)
        cache.delete(cache_key_seller)

        return Response({"detail": "Статус обновлен"}, status=status.HTTP_200_OK)

    return Response(
        {"detail": "Неверное значение статуса"},
        status=status.HTTP_400_BAD_REQUEST,
    )
