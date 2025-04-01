from django.urls import path
from products.views import (
    get_product_list,
    create_product,
    get_product_detail,
    delete_product,
    update_product,
    get_category_list,
    create_category,
    update_category,
    delete_category,
)

urlpatterns = [
    path("products/list/", get_product_list, name="get_product_list"),
    path("products/create/", create_product, name="create_product"),
    path(
        "products/<int:product_id>/get/", get_product_detail, name="get_product_detail"
    ),
    path("products/<int:product_id>/delete/", delete_product, name="delete_product"),
    path("products/<int:product_id>/update/", update_product, name="update_product"),
    path("categories/list", get_category_list, name="get_category_list"),
    path("categories/create/", create_category, name="create_category"),
    path(
        "categories/<int:category_id>/update/", update_category, name="update_category"
    ),
    path(
        "categories/<int:category_id>/delete/", delete_category, name="delete_category"
    ),
]
