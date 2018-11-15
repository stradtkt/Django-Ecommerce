from django.db import models
from django.conf import settings
from products.models import Product

User = settings.AUTH_USER_MODEL

class Cart(models.Model):
    user = models.ForeignKey(User, related_name="buyer", null=True, blank=True)
    products = models.ManyToManyField(Product, related_name="products")
    total = models.DecimalField(decimal_places=2, max_digits=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.id)
