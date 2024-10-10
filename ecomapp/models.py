from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=255,null=True)
   
  

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    prname = models.CharField(null=True,max_length=255)
    prprice = models.IntegerField(null=True)
    prdesc = models.CharField(max_length=255,null=True)
    primg = models.ImageField(upload_to="image/", null=True)

class userdetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    username = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=255,null=True)
    number = models.CharField(max_length=255,null=True)
    usimg = models.ImageField(blank=True,upload_to='image/',null=True)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    prod = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=1,null=True)
    def subtotal(self):
        return self.prod.prprice * self.quantity

 