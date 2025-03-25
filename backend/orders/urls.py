from django.urls import path
from orders.views import (
    BuyerOrderCreateView,
    BuyerOrderListView,
    BuyerOrderDetailView,
    BuyerOrderStatusUpdateView,
    SellerOrderListView,
    SellerOrderStatusUpdateView,
    SellerOrderDetailView,
)

urlpatterns = [
    # Покупатель
    path("buyer/list/", BuyerOrderListView.as_view(), name="buyer_order_list"),
    path("buyer/create/", BuyerOrderCreateView.as_view(), name="buyer_order_create"),
    path(
        "buyer/get/<int:order_id>/",
        BuyerOrderDetailView.as_view(),
        name="buyer_order_detail",
    ),
    path(
        "buyer/update/<int:order_item_id>/",
        BuyerOrderStatusUpdateView.as_view(),
        name="buyer_order_update",
    ),
    # Продавец
    path(
        "seller/get/<int:order_id>/",
        SellerOrderDetailView.as_view(),
        name="seler_order_detail",
    ),
    path(
        "seller/list/",
        SellerOrderListView.as_view(),
        name="seller_order_list",
    ),
    path(
        "seller/update/<int:order_item_id>/",
        SellerOrderStatusUpdateView.as_view(),
        name="seller_order_update",
    ),
]
