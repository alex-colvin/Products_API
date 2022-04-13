from django.db import models
from products.models import Product

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=255)
    body = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
