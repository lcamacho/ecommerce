from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Tag(models.Model):
    name = models.CharField(max_length=10, unique=True)


class Category(models.Model):
    name = models.CharField(max_length=10, unique=True)


class Product(models.Model):
    sku = models.CharField(max_length=4, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image_one = models.ImageField(upload_to="media/")
    image_two = models.ImageField(upload_to="media/")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
