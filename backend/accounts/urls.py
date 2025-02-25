from django.urls import path
from rest_framework_simplejwt.views import TokenBlacklistView, TokenRefreshView

from accounts.views import CustomTokenObtainPairView, UserRegistrationAPIView

urlpatterns = [
    path("register/", UserRegistrationAPIView.as_view(), name="register"),
    path("login/", CustomTokenObtainPairView.as_view(), name="login"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("logout/", TokenBlacklistView.as_view(), name="logout"),
]
