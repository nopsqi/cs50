import factory
from auctions.models import User, Category, Listing, Bid, BidHistory, Comment


def main():
    for _ in range(5):
        category = CategoryFactory()


class UserFactory(factory.django.DjangoFactory):
    class Meta:
        model = User

    username = factory.Faker("user_name")
    email = factory.Faker("email")
    password = "asdf"


class CategoryFactory(factory.django.DjangoFactory):
    class Meta:
        model = Category

    name = factory.Faker("word")


if __name__ == "__main__":
    main()
