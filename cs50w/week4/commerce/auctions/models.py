from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Category(models.Model):
    name = models.CharField(max_length=16)

    class Meta:
        verbose_name_plural = "Categories"


class Listing(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listings")
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=64)
    url = models.URLField()
    categories = models.ManyToManyField(Category, related_name="lisings")
    starting_bid = models.IntegerField()


class Bid(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids")
    listing_id = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bids")
    ammount = models.IntegerField()


class BidHistory(Bid):
    timestamp = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Bid History"
        verbose_name_plural = "Bid Histories"

class Comment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    comment = models.CharField(max_length=300)
