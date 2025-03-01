from django.urls import path
from profiles.views import ProfileAPIView

urlpatterns = [
    path("me/", ProfileAPIView.as_view(), name="get_patch_profile"),
]
