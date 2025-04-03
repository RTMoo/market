from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from rest_framework.response import Response
from products.models import Category
from products.serializers import CategorySerializer
from commons.permissions import IsModerator


@api_view(["GET"])
@permission_classes([AllowAny])
def get_category_list(request):
    category_list = Category.objects.all()
    data = CategorySerializer(instance=category_list, many=True).data

    return Response(data=data, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([IsAuthenticated, IsModerator])
def create_category(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        category = Category.objects.create(**serializer.validated_data)
        data = CategorySerializer(instance=category).data

        return Response(data=data, status=status.HTTP_201_CREATED)

    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PATCH"])
@permission_classes([IsAuthenticated, IsModerator])
def update_category(request, category_id):
    serializer = CategorySerializer(data=request.data, partial=True)
    if serializer.is_valid():
        Category.objects.filter(id=category_id).update(**serializer.validated_data)
        category = Category.objects.filter(id=category_id).first()
        data = CategorySerializer(instance=category).data

        return Response(data=data, status=status.HTTP_200_OK)

    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated, IsModerator])
def delete_category(request, category_id):
    is_deleted, _ = Category.objects.filter(id=category_id).delete()

    if is_deleted:
        return Response(status=status.HTTP_204_NO_CONTENT)

    return Response(status=status.HTTP_404_NOT_FOUND)
