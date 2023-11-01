from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Item(models.Model):
    name = models.CharField(max_length=64)


class Category(models.Model):
    pass


class Listing(models.Model):
    pass


class Bid(models.Model):
    pass


class Comment(models.Model):
    pass
