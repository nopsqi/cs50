from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Item(models.Model):
    name = models.CharField(max_length=64)
    url = models.URLField()


class Category(models.Model):
    name = models.CharField(max_length=32)


class Listing(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="item")


class Bid(models.Model):
    pass


class Comment(models.Model):
    pass
