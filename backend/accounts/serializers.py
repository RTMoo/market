from rest_framework import serializers

from accounts.models import CustomUser
from profiles.models import Profile


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
        Profile.objects.create(user=user)
        
        return user
