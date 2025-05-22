from django.db import models

# Create your models here.
from django.db import models

# 1. Shoe Category (e.g. Sports, Casual, Formal)
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# 2. Shoe Model
class Shoes(models.Model):
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    size = models.IntegerField()  # Example: 7, 8, 9, etc.
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()  # Number of items in stock
    description = models.TextField()
    image = models.ImageField(upload_to='shoe_images/', blank=True)

    def __str__(self):
        return f"{self.brand} - {self.name} (Size: {self.size})"

# 3. Customer Model
class Customer(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name

# 4. Order Model
class Orders(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    shoe = models.ForeignKey(Shoes, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    delivered = models.BooleanField(default=False)

    def __str__(self):
        return f"Order #{self.id} by {self.customer.name}"

