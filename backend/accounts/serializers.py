from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from accounts.models import CustomUser
from profiles.models import Profile


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def get_token(self, user):
        token = super().get_token(user)

        # Кастомные поля в payload токена
        token["is_staff"] = user.is_staff
        token["email"] = user.email

        return token


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
        profile = Profile.objects.create(user=user)
        print(profile.first_name)
        return user
