from django.urls import path
from orders.views import (
    OrderCreateView,
    OrderListView,
)

urlpatterns = [
    path("", OrderListView.as_view(), name="order_list"),
    path("create/", OrderCreateView.as_view(), name="order_create"),
]
