from django.db import models
from django.contrib.auth.models import User


class Brand(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True) 
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name



class Keybord(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name



class Headphone(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name








STAR_CHOICES = [
    (1, '⭐'),
    (2, '⭐⭐'),
    (3, '⭐⭐⭐'),
    (4, '⭐⭐⭐⭐'),
    (5, '⭐⭐⭐⭐⭐'),
]



class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    email = models.EmailField()
    star = models.IntegerField(choices=STAR_CHOICES)  # Now it correctly stores an integer
    body = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} rated {self.product.name} {dict(STAR_CHOICES)[self.star]}"




