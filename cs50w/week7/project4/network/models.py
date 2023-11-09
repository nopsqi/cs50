from django.contrib.auth.models import AbstractUser
from django.contrib.humanize.templatetags import humanize
from django.db import models


class User(AbstractUser):
    followings = models.ManyToManyField("self", related_name="followers")
    followers = models.ManyToManyField("self", related_name="followings")


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    content = models.TextField(default=False)
    likes = models.ManyToManyField(User, related_name="liked_posts")

    def __str__(self):
        return f"{self.user} says {self.content}"

    def serialize(self):
        return {
            "id": self.id,
            "created": humanize.naturaltime(self.created),
            "modified": humanize.naturaltime(self.modified),
            "user": self.user.username,
            "content": self.content,
            "likes": [user.username for user in self.likes.all()],
        }
