from products.views import ProductListView, CategoryViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"product", ProductListView)
router.register(r"category", CategoryViewSet)

urlpatterns = router.urls
