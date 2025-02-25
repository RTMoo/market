from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from accounts.serializers import UserRegistrationSerializer
from .serializers import CustomTokenObtainPairSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Представление для получения JWT-токена.

    Использует кастомный сериализатор `CustomTokenObtainPairSerializer`,
    который проверяет учетные данные и выдает пару токенов (access и refresh).
    """

    serializer_class = CustomTokenObtainPairSerializer


class UserRegistrationAPIView(APIView):
    """
    Представление для регистрации нового пользователя.

    Позволяет любому пользователю (`AllowAny`) создать новый аккаунт,
    отправив email и пароль. Возвращает данные нового пользователя
    при успешной регистрации.

    Attributes:
        permission_classes (list): Разрешает доступ всем пользователям.
        serializer_class (UserRegistrationSerializer): Сериализатор для регистрации.
    """

    permission_classes = [AllowAny]
    serializer_class = UserRegistrationSerializer

    def post(self, request):
        """
        Обрабатывает POST-запрос для регистрации пользователя.

        Args:
            request (Request): Запрос с данными пользователя.

        Returns:
            Response: JSON-ответ с данными пользователя при успешной регистрации (201),
            либо с ошибками валидации (400).
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
