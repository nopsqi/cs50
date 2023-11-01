import factory
from models import User, Category, Listing, Bid, BidHistory, Comment


def main():
    CategoryFactory.create_batch(10)


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("user_name")
    email = factory.Faker("email")
    password = "asdf"


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker("word")


if __name__ == "__main__":
    main()
