from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from rest_framework.response import Response
from products.models import Product
from products.serializers import ProductSerializer
from commons.paginations import ProductPagination
from accounts.models import CustomUser


@api_view(["GET"])
@permission_classes([AllowAny])
def get_product_list(request):
    product_list = Product.objects.all()
    paginator = ProductPagination()
    queryset = paginator.paginate_queryset(queryset=product_list, request=request)
    data = ProductSerializer(instance=queryset, many=True).data

    return paginator.get_paginated_response(data)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_product_detail(request, product_id):
    product = Product.objects.filter(id=product_id).first()

    if not product:
        return Response({"Not found"}, status=status.HTTP_404_NOT_FOUND)

    data = ProductSerializer(instance=product).data
    return Response(data=data, status=status.HTTP_200_OK)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        seller = CustomUser.objects.filter(id=request.user.id).first()

        if not seller:
            return Response(
                "Такого продавца нет в базе данных", status=status.HTTP_404_NOT_FOUND
            )

        if seller.role != CustomUser.Role.SELLER:
            return Response(
                "Вы не можете создать продукт так как не являетесь продавцом",
                status=status.HTTP_403_FORBIDDEN,
            )

        validated_data = serializer.validated_data
        product = Product.objects.create(seller=seller, **validated_data)

        data = ProductSerializer(instance=product).data
        return Response(data=data, status=status.HTTP_200_OK)

    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PATCH"])
@permission_classes([IsAuthenticated])
def update_product(request, product_id):
    pass


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_product(request, product_id):
    pass
