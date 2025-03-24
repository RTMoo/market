from django.urls import path
from orders.views import (
    OrderCreateView,
    OrderListView,
    OrderDetailView,
    SellerOrderListView,
    SellerOrderItemUpdateView,
    SellerOrderDetailView,
)

urlpatterns = [
    # Покупатель
    path("list/", OrderListView.as_view(), name="order_list"),
    path("create/", OrderCreateView.as_view(), name="order_create"),
    path("get/<int:order_id>/", OrderDetailView.as_view(), name="order_detail"),
    # Продавец
    path(
        "seller/get/<int:order_id>/",
        SellerOrderDetailView.as_view(),
        name="seler_order_detail",
    ),
    path(
        "seller/list/",
        SellerOrderListView.as_view(),
        name="seller_order_item_list",
    ),
    path(
        "seller/update/<int:order_item_id>/",
        SellerOrderItemUpdateView.as_view(),
        name="seller_order_item_update",
    ),
]
