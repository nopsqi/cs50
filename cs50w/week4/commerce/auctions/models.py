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
    categories = models.ManyToManyField(Category, related_name="categories")
    starting_bid = models.IntegerField()


class Bid(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users")
    listing_id = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="listings")
    ammount = models.IntegerField()


class BidHistory(Bid):
    timestamp = models.DateField(auto_add_now=True)


class Comment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users")
    comment = models.CharField(max_length=300)
