from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet, BrandViewSet, CategoryViewSet, ProductViewSet,
    OrderViewSet, OrderItemViewSet, CartViewSet, ReviewViewSet
)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'brands', BrandViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order-items', OrderItemViewSet)
router.register(r'carts', CartViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
