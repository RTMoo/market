from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from accounts.serializers import UserRegistrationSerializer
from rest_framework_simplejwt.views import TokenRefreshView, TokenBlacklistView
from accounts.utils import set_jwt_token


class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Хранение токена в HttpOnly
    """

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        if response.status_code == status.HTTP_200_OK:
            access_token = response.data.get("access")
            refresh_token = response.data.get("refresh")

            if access_token and refresh_token:
                response = set_jwt_token(
                    response=response,
                    access_token=access_token,
                    refresh_token=refresh_token,
                )
                # Удаляем токены из тела ответа
                del response.data["access"]
                del response.data["refresh"]

        return response


class CustomTokenRefreshView(TokenRefreshView):
    """
    Обновление access токена
    """

    def post(self, request, *args, **kwargs):
        refresh_token = request.COOKIES.get("refresh_token")

        if not refresh_token:
            return Response(
                {"detail": "Refresh token is missing"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        request.data["refresh"] = refresh_token

        response = super().post(request, *args, **kwargs)

        if response.status_code == status.HTTP_200_OK:
            new_access_token = response.data.get("access")

            if new_access_token:
                response = set_jwt_token(
                    response=response, access_token=new_access_token
                )

                del response.data["access"]

        return response


class CustomTokenBlacklistView(TokenBlacklistView):
    """
    Выход из системы и очистка куков
    """

    def post(self, request, *args, **kwargs):
        # Получаем refresh токен из куки (Потому что фронтенд не должен передавать вручную)
        refresh_token = request.COOKIES.get("refresh_token")

        if not refresh_token:
            return Response(
                {"detail": "Refresh token is missing"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Добавляем refresh-токен в данные запроса
        request.data.update({"refresh": refresh_token})

        response = super().post(request, *args, **kwargs)

        if response.status_code == status.HTTP_200_OK:
            # Удаляем куки с токенами
            response.delete_cookie("access_token")
            response.delete_cookie("refresh_token")

        return response


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
