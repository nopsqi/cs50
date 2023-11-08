from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    followings = models.ManyToManyField("self", related_name="followers")
    followers = models.ManyToManyField("self", related_name="followings")


class Post(models):
    created = models.DateTimeField(auto_add_now=true)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
