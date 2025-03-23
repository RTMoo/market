from django.urls import path
from orders.views import (
    OrderCreateView,
    OrderListView,
    OrderDetailView,
    OrderItemDetailView,
    SellerOrderItemListView,
    SellerOrderItemUpdateView,
)

urlpatterns = [
    # Покупатель
    path("list/", OrderListView.as_view(), name="order_list"),
    path("create/", OrderCreateView.as_view(), name="order_create"),
    path("get/<int:order_id>/", OrderDetailView.as_view(), name="order_detail"),
    path(
        "item/get/<int:order_item_id>/",
        OrderItemDetailView.as_view(),
        name="order_item_detail",
    ),
    # Продавец
    path(
        "seller/order/list/",
        SellerOrderItemListView.as_view(),
        name="seller_order_item_list",
    ),
    path(
        "seller/item/update/<int:order_item_id>/",
        SellerOrderItemUpdateView.as_view(),
        name="seller_order_item_update",
    ),
]
