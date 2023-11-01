import factory
from .models import User, Category, Listing, Bid, BidHistory, Comment


class UserFactory(factory.django.DjangoFactory):
    class Meta:
        model = User

    username = factory.Faker("user_name")
    email = 
