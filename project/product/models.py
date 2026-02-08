from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField()
    price = models.FloatField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)