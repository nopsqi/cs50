from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator


class User(AbstractUser):
    pass


class Category(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Categories"


class Listing(models.Model):
    modified = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listings")
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=64)
    url = models.URLField()
    categories = models.ManyToManyField(Category, related_name="lisings")
    starting_bid = models.DecimalField(max_digits=11, decimal_places=2, validators=[MinValueValidator(0.01)])
    current_bid = models.DecimalField(blank=True, null=True, max_digits=11, decimal_places=2, validators=[MinValueValidator(0.01)])

    def __str__(self):
        return f"{self.name} by {self.user.username}"


class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bids")
    amount = models.DecimalField(max_digits=11, decimal_places=2, validators=[MinValueValidator(0.01)])

    def __str__(self):
        return f"{self.user.username} bid {self.listing.name} ${self.amount}"


class Comment(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="comments")
    content = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.user.username} at {self.listing.name[:10]} said {self.content[:30]}"
