from .views import ProductCollectionViewSet, ProductViewSet, OrderViewSet, ReviweViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('products', ProductViewSet, basename='products')
router.register('orders', OrderViewSet, basename='orders')
router.register('product-reviews', ReviweViewSet, basename='product-reviews')
router.register('product-collections', ProductCollectionViewSet, basename='product-collections')


urlpatterns = []
urlpatterns += router.urls