from rest_framework.serializers import ModelSerializer
from profiles.models import Profile


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ["first_name", "last_name", "phone_number"]
