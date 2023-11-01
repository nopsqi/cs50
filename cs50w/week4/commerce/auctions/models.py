from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Category(models.Model):
    name = models.CharField(max_length=16)


class Listing(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users")
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=64)
    url = models.URLField()
    category = models.ManyToManyField(Category, related_name="categories")
    starting_bid = models.IntegerField()
    current_bid = models.ForeignKey(Bid, )


class Bid(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users")
    liting_id = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="listings")
    ammount = models.IntegerField()


class Comment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users")
    comment = models.CharField(max_length=300)
