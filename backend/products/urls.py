from django.urls import path, include
from products.views import (
    ProductViewSet,
    CategoryViewSet,
    UserProductViewSet,
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"product", ProductViewSet)
router.register(r"category", CategoryViewSet)
router.register(r"user-products", UserProductViewSet, basename="user-products")

urlpatterns = router.urls
