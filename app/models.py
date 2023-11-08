from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    image = models.ImageField(
        upload_to='static/images/products/',
        null=True,
        blank=True,
        default='static/images/products/placeholder.png'
    )
    price = models.DecimalField(max_digits=50,decimal_places=2)
    inventory = models.DecimalField(max_digits=50,decimal_places=3)

    def __str__(self):
        return self.description
