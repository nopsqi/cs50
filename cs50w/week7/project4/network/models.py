from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Profile(models):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="profile")
    
