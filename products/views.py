from django.shortcuts import render
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.viewsets import ModelViewSet
from products.models import Product, Order, Review, ProductCollection, Item
from .filters import  ProductFilter, ReviewFilter, OrderFilter
from .serializers import UserSerializer, ProductSerializer, OrderSerializer, ItemSerializer, ReviewSerializer, ProductCollectionSerializer

class IsOwnerOrAdmin(permissions.BasePermission):
    """Класс разрешений для владельца объекта"""
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return obj.creator == request.user

class ProductViewSet(ModelViewSet):
    """ViewSet для товара."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAdminUser()]
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return []

class OrderViewSet(ModelViewSet):
    """ViewSet для заказа"""
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filterset_class = OrderFilter

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create"]:
            return [IsAuthenticated()]
        if self.action in ["list"]:
            return [IsAdminUser()]
        if self.action in ["retrieve", "update", "partial_update", "destroy"]:
            return [IsOwnerOrAdmin()]
        return []

    def get_serializer_context(self):
        return {
            "request": self.request
        }

class ReviweViewSet(ModelViewSet):
    """ViewSet для отзывов."""
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filterset_class = ReviewFilter

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create"]:
            return [IsAuthenticated()]
        if self.action in ["update", "partial_update", "destroy"]:
            return [IsOwnerOrAdmin()]
        return []

class ProductCollectionViewSet(ModelViewSet):
    """ViewSet для подборок"""
    queryset = ProductCollection.objects.all()
    serializer_class = ProductCollectionSerializer

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAdminUser()]
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return []