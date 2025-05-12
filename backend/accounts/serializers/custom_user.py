from rest_framework.serializers import (
    ModelSerializer,
    EmailField,
    CharField,
    ValidationError,
)
from accounts.models import CustomUser
from accounts.tasks import send_confirmation_email
from profiles.models import Profile
from carts.models import Cart


class UserRegistrationSerializer(ModelSerializer):
    """
    Сериализатор для регистрации пользователя.
    """

    email = EmailField(required=True)
    password = CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ["email", "password"]

    def validate(self, data):
        """
        Проверяет, существует ли пользователь с таким email, и совпадают ли пароли.
        """

        user = CustomUser.objects.filter(email=data["email"]).first()
        if user and user.is_active:
            raise ValidationError({"email": "Этот email уже используется"})

        return data

    def create(self, validated_data):
        """
        Создаёт нового пользователя после успешной валидации данных.
        """
        user = CustomUser.objects.filter(email=validated_data["email"]).first()

        if not user:
            user = CustomUser.objects.create_user(**validated_data)
            Profile.objects.create(user=user)
            Cart.objects.create(buyer=user)
        else:
            user.set_password(validated_data["password"])
            user.save()
        print(1)
        send_confirmation_email.delay(user.email)
        print(2)
        return user
