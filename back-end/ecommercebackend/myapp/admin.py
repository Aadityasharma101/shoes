from django.contrib import admin
from .models import Brand, Category, Product, Order, OrderItem, Cart, Review

# Register all models (except User)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Cart)
admin.site.register(Review)
