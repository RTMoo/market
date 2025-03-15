from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.db.utils import IntegrityError
from phonenumbers import parse, is_valid_number, NumberParseException

from profiles.serializers import ProfileSerializer
from profiles.models import Profile


class ProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer

    def get(self, request):
        """
        Получить профиль текущего пользователя
        """

        try:
            profile = (
                Profile.objects.filter(user=request.user.id)
                .values(
                    "first_name",
                    "last_name",
                    "phone_number",
                    "user__email",
                    "user__role",
                )
                .first()
            )
            data = self.serializer_class(profile).data
            data["email"] = profile["user__email"]
            data["role"] = profile["user__role"]
        except TypeError:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        return Response(data=data, status=status.HTTP_200_OK)

    def patch(self, request):
        """
        Обновить профиль пользователя (только измененные поля)
        """

        pn = request.data.get("phone_number")
        if len(pn) > 0:
            try:
                is_valid_number(parse(pn))
            except NumberParseException:
                return Response(
                    {"message": "Invalid data phone_number"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        try:
            updated_rows = Profile.objects.filter(user=request.user.id).update(
                **request.data
            )

            if updated_rows == 0:
                return Response(
                    data={"message": "profile not updated"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            return Response({"message": "profile updated"}, status=status.HTTP_200_OK)

        except IntegrityError:
            return Response(
                {"message": "Phone number must be unique"},
                status=status.HTTP_400_BAD_REQUEST,
            )
