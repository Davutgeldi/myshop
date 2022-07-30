from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=150, blank=True)


class Products(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='product_images', blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
