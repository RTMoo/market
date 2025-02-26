from products.views import ProductViewSet, CategoryViewSet, ReviewViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"product", ProductViewSet)
router.register(r"category", CategoryViewSet)
router.register(r"review", ReviewViewSet)

urlpatterns = router.urls
