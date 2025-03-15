from rest_framework.serializers import (
    ModelSerializer,
    EmailField,
    CharField,
    ValidationError,
)

from accounts.models import CustomUser
from profiles.models import Profile
from carts.models import Cart


class UserRegistrationSerializer(ModelSerializer):
    """
    Сериализатор для регистрации пользователя.
    """

    email = EmailField(required=True)
    password = CharField(write_only=True)
    password2 = CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ["email", "password", "password2"]

    def validate(self, data):
        """
        Проверяет, существует ли пользователь с таким email, и совпадают ли пароли.
        """

        if CustomUser.objects.only("id").filter(email=data["email"]).exists():
            raise ValidationError({"email": "Этот email уже используется"})

        if data["password"] != data["password2"]:
            raise ValidationError({"password": "Пароли не совпадают"})

        return data

    def create(self, validated_data):
        """
        Создаёт нового пользователя после успешной валидации данных.
        """

        validated_data.pop("password2")
        user = CustomUser.objects.create_user(**validated_data)
        Profile.objects.create(user=user)
        Cart.objects.create(user=user)

        return user
