from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status


@api_view(["GET"])
@permission_classes([AllowAny])
def get_category_list(request):
    pass


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_category(request):
    pass


@api_view(["PATCH"])
@permission_classes([IsAuthenticated])
def update_category(request, category_id):
    pass


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_category(request, category_id):
    pass
