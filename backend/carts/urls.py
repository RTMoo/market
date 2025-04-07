from django.urls import path
from carts.views import (
    get_cart_list,
    add_cart_item,
    update_cart_item,
    delete_cart_item,
    clear_cart,
)

urlpatterns = [
    path("list/", get_cart_list, name="cart_list"),
    path("add/", add_cart_item, name="cart_add"),
    path("update/<int:cart_item_id>/", update_cart_item, name="cart_update"),
    path("delete/<int:cart_item_id>/", delete_cart_item, name="cart_delete"),
    path("clear/", clear_cart, name="cart_clear"),
]
