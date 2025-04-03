from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/accounts/", include("accounts.urls")),
    path("api/catalogs/", include("products.urls")),
    path("api/profiles/", include("profiles.urls")),
    path("api/carts/", include("carts.urls")),
    path("api/orders/", include("orders.urls")),
    path("api/reviews/", include("reviews.urls")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/docs/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/docs/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"
    ),
    path("silk/", include("silk.urls", namespace="silk")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
