from rest_framework.serializers import ModelSerializer, EmailField, CharField
from profiles.models import Profile
from phonenumber_field.modelfields import PhoneNumberField


class ProfileSerializer(ModelSerializer):
    email = EmailField(source="user.email")
    role = CharField(source="user.role")
    phone_number = PhoneNumberField()

    class Meta:
        model = Profile
        fields = ["first_name", "last_name", "phone_number", "email", "role"]
        read_only_fields = ["email", "role"]
