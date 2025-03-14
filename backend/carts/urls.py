from django.urls import path
from carts.views import (
    CartAddView,
    CartView,
    CartUpdateView,
    CartDeleteView,
    CartClearView,
)

urlpatterns = [
    path("", CartView.as_view(), name="cart_list"),
    path("add/", CartAddView.as_view(), name="cart_add"),
    path("update/<int:cart_item_id>/", CartUpdateView.as_view(), name="cart_update"),
    path("delete/<int:cart_item_id>/", CartDeleteView.as_view(), name="cart_delete"),
    path("clear/", CartClearView.as_view(), name="cart_clear"),
]
