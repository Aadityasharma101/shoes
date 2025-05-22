from django.contrib import admin
from .models import(Category,Shoes,Customer,Orders)

# Register your models here.
admin.site.register([Category,Shoes,Customer,Orders])
