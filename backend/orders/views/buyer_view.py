from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from orders.serializers import OrderSerializer
from orders.models import Order, OrderItem
from orders.utils import create_order
from django.core.cache import cache

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def buyer_order_list(request):
    buyer_id = request.user.id
    cache_key = f"buyer_{buyer_id}_order_list"
    
    order_data = cache.get(cache_key)
    
    if not order_data:
        orders = Order.objects.filter(buyer=buyer_id).prefetch_related("items__product")
        order_data = OrderSerializer(orders, many=True).data
        
        cache.set(cache_key, order_data, timeout=60 * 60)

    return Response(data=order_data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def buyer_order_detail(request, order_id):
    buyer_id = request.user.id
    cache_key = f"buyer_{buyer_id}_order_detail_{order_id}"

    order_data = cache.get(cache_key)
    
    if not order_data:
        order = (
            Order.objects.filter(id=order_id, buyer=buyer_id)
            .prefetch_related("items__product")
            .first()
        )
        if not order:
            return Response({"detail": "Заказ не найден"}, status=status.HTTP_404_NOT_FOUND)

        order_data = OrderSerializer(order).data
        
        cache.set(cache_key, order_data, timeout=60 * 60)

    return Response(data=order_data, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def buyer_order_create(request):
    buyer_id = request.user.id
    serializer = OrderSerializer(data=request.data)

    if serializer.is_valid():
        order = create_order(request, serializer.validated_data)
        data = OrderSerializer(instance=order).data
        cache_key_buyer = f"buyer_{buyer_id}_order_list"
        cache_key_seller = f"seller_{order.seller_id}_order_list"
        
        cache.delete(cache_key_buyer)
        cache.delete(cache_key_seller)
        
        return Response(data=data, status=status.HTTP_201_CREATED)

    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PATCH"])
@permission_classes([IsAuthenticated])
def buyer_order_status_update(request, order_item_id):
    buyer_id = request.user.id
    order_item = (
        OrderItem.objects.filter(id=order_item_id).select_related("order").first()
    )

    if not order_item:
        return Response(
            {"detail": "Элемент заказа не найден"},
            status=status.HTTP_404_NOT_FOUND,
        )

    if order_item.order.buyer_id != buyer_id:
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

    if item_status in (OrderItem.Status.CANCELED, OrderItem.Status.DELIVERED):
        if (
            item_status == OrderItem.Status.DELIVERED
            and order_item.status != OrderItem.Status.SHIPPED
        ):
            return Response(
                {"detail": "Нельзя доставить то что не отправлено, АУФ!"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        order_item.status = item_status
        order_item.save()
        
        # Очищаем кэш для покупателя и продавца
        cache_key_buyer = f"buyer_{buyer_id}_order_detail_{order_item.order_id}"
        cache_key_seller = f"seller_{order_item.seller_id}_order_detail_{order_item.order_id}"

        cache.delete(cache_key_buyer)
        cache.delete(cache_key_seller)

        return Response({"detail": "Статус обновлен"}, status=status.HTTP_200_OK)

    return Response(
        {"detail": "Неверное значение статуса"},
        status=status.HTTP_400_BAD_REQUEST,
    )
