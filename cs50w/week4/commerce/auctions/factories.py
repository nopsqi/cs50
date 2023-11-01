import factory
from models import User, Category, Listing, Bid, BidHistory, Comment


def main():
    for _ in range(10):
        
        user = UserFactory()


class UserFactory(factory.django.DjangoFactory):
    class Meta:
        model = User

    username = factory.Faker("user_name")
    email = factory.Faker("email")
    password = "asdf"


if __name__ == "__main__":
    main()
