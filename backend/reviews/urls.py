from django.urls import path
from reviews.views import add_review, update_review, get_product_reviews, delete_review

urlpatterns = [
    path("product/<int:product_id>/", get_product_reviews, name="get_review_list"),
    path("create/", add_review, name="add_review"),
    path("update/<int:review_id>/", update_review, name="update_review"),
    path("delete/<int:review_id>/", delete_review, name="delete_review"),
]
