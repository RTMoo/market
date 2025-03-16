from django.urls import path
from orders.views import (
    OrderCreateView,
    OrderListView,
    OrderDetailView
)

urlpatterns = [
    path("", OrderListView.as_view(), name="order_list"),
    path("create/", OrderCreateView.as_view(), name="order_create"),
    path("<int:order_id>/", OrderDetailView.as_view(), name="order_detail"),
]
