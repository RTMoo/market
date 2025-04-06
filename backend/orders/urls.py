from django.urls import path
from orders.views import (
    buyer_order_create,
    buyer_order_list,
    buyer_order_detail,
    buyer_order_status_update,
    seller_order_list,
    seller_order_status_update,
    seller_order_detail,
)

urlpatterns = [
    # Покупатель
    path("buyer/list/", buyer_order_list, name="buyer_order_list"),
    path("buyer/create/", buyer_order_create, name="buyer_order_create"),
    path(
        "buyer/get/<int:order_id>/",
        buyer_order_detail,
        name="buyer_order_detail",
    ),
    path(
        "buyer/update/<int:order_item_id>/",
        buyer_order_status_update,
        name="buyer_order_update",
    ),
    # Продавец
    path(
        "seller/get/<int:order_id>/",
        seller_order_detail,
        name="seller_order_detail",
    ),
    path(
        "seller/list/",
        seller_order_list,
        name="seller_order_list",
    ),
    path(
        "seller/update/<int:order_item_id>/",
        seller_order_status_update,
        name="seller_order_update",
    ),
]
