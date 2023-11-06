from mail.models import User, Email
import factory
from factory.django import DjangoModelFactory


class UserFactory(DjangoEmailFactory):
    class Meta:
        model = User

    username = factory.Faker("user_name")
    email = factory.Faker("email")


class EmailFactory(DjangoEmailFactory):
    class Meta:
        model = Email

    user = factory.SubFactory()
