from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from category.permissions import IsSuperUserOrReadOnly
from category.serializers import CategorySerializer
from category.models import Category


class CreateCategoryAPIView(CreateAPIView):
    permission_classes = [IsSuperUserOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryListAPIView(ListAPIView):
    permission_classes = [IsSuperUserOrReadOnly]
    # queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = Category.objects.filter(sub_category=None)
        return queryset

class CategoryRUDAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsSuperUserOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer