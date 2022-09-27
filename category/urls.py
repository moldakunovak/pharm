from django.urls import path

from .views import CreateCategoryAPIView, CategoryListAPIView, CategoryRUDAPIView


urlpatterns = [
    path("category/", CreateCategoryAPIView.as_view()),
    path("category-list/", CategoryListAPIView.as_view()),
    path("category-rud/<int:pk>/", CategoryRUDAPIView.as_view()),
]
