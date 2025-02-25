from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from accounts.models import CustomUser


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Кастомный сериализатор для получения JWT-токена по email и паролю.
    """

    def validate(self, data):
        """
        Проверяет введённые email и пароль, аутентифицирует пользователя
        и выдаёт JWT-токены (access и refresh).
        """
        email = data.get("email")
        password = data.get("password")

        if not email or not password:
            raise serializers.ValidationError("Необходимо указать email и пароль")

        user = authenticate(
            request=self.context.get("request"), email=email, password=password
        )

        if not user:
            raise serializers.ValidationError("Неверные email или пароль")

        refresh = self.get_token(user)

        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "email": user.email,
        }


class CustomUserSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели CustomUser.
    """

    class Meta:
        model = CustomUser
        fields = ["id", "email"]


class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Сериализатор для регистрации пользователя.
    """

    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ["email", "password", "password2"]

    def validate(self, data):
        """
        Проверяет, существует ли пользователь с таким email, и совпадают ли пароли.
        """
        if CustomUser.objects.only("id").filter(email=data["email"]).exists():
            raise serializers.ValidationError({"email": "Этот email уже используется"})

        if data["password"] != data["password2"]:
            raise serializers.ValidationError({"password": "Пароли не совпадают"})

        return data

    def create(self, validated_data):
        """
        Создаёт нового пользователя после успешной валидации данных.
        """
        validated_data.pop("password2")
        user = CustomUser.objects.create_user(**validated_data)
        return user
