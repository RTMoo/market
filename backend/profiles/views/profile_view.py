from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from profiles.serializers import ProfileSerializer
from profiles.models import Profile
from rest_framework.decorators import api_view, permission_classes
from django.core.cache import cache


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_profile_detail(request):
    user_id = request.user.id
    cache_key = f"profile_user_{user_id}"

    data = cache.get(cache_key)
    if not data:
        profile = Profile.objects.filter(user_id=user_id).select_related("user").first()
        data = ProfileSerializer(instance=profile).data
        cache.set(cache_key, data, 60 * 60)

    return Response(data=data, status=status.HTTP_200_OK)


@api_view(["PATCH"])
@permission_classes([IsAuthenticated])
def update_profile(request):
    serializer = ProfileSerializer(data=request.data, partial=True)
    if serializer.is_valid():
        user_id = request.user.id
        cache_key = f"profile_user_{user_id}"

        Profile.objects.filter(user_id=user_id).update(**serializer.validated_data)
        profile = Profile.objects.filter(user_id=user_id).select_related("user").first()
        data = ProfileSerializer(instance=profile).data

        cache.delete(cache_key)
        return Response(data=data, status=status.HTTP_200_OK)

    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
