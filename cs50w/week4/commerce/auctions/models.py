from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Category(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Categories"


class Listing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listings")
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=64)
    url = models.URLField()
    categories = models.ManyToManyField(Category, related_name="lisings")
    starting_bid = models.DecimalField(max_digits=11, decimal_places=2)

    def __str__(self):
        return f"{self.name} by {self.user_id.username}"


class Bid(models.Model):
    last_modified = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bids")
    amount = models.DecimalField(max_digits=11, decimal_places=2)


class BidHistory(models.Model):
    timestamp = models.DateField(auto_now_add=True)
    bid = models.ForeignKey(Bid, on_delete=models.DO_NOTHING, related_name="histories")
    amount = models.DecimalField(max_digits=11, decimal_places=2)

    class Meta:
        verbose_name = "Bid History"
        verbose_name_plural = "Bid Histories"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="comments")
    content = models.CharField(max_length=300)

    def __str__(self):
        return f"{user.username} at {listing.name} said {content[:10]}"
