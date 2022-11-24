from django.db import models

# Create your models here.
class ProductData(models.Model):
    product_id=models.CharField(max_length=100)
    product_name=models.CharField(max_length=100)
    product_cost=models.IntegerField()
    product_color=models.CharField(max_length=100)
    product_class=models.CharField(max_length=100)