from django.urls import path
from profiles.views import get_profile_detail, update_profile

urlpatterns = [
    path("me/", get_profile_detail, name="get_profile_detail"),
    path("update/", update_profile, name="update_your_profile"),
]
