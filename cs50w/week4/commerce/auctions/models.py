from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Listing(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=64)
    url = models.URLField()
    starting_bid = models.IntegerField()


class Bid(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users")
    liting_id = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="listings")
