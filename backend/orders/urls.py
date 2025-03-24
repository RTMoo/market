from django.urls import path
from orders.views import (
    BuyerOrderCreateView,
    BuyerOrderListView,
    BuyerOrderDetailView,
    SellerOrderListView,
    SellerOrderStatusUpdateView,
    SellerOrderDetailView,
)

urlpatterns = [
    # Покупатель
    path("list/", BuyerOrderListView.as_view(), name="order_list"),
    path("create/", BuyerOrderCreateView.as_view(), name="order_create"),
    path("get/<int:order_id>/", BuyerOrderDetailView.as_view(), name="order_detail"),
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
        SellerOrderStatusUpdateView.as_view(),
        name="seller_order_item_update",
    ),
]
