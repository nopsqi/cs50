from mail.models import User, Email
import factory
from factory.django import DjangoModelFactory


class UserFactory(DjangoEmailFactory):
    class Meta:
        model = User

    username = factory.Faker("user_name")
    email = factory.Faker("email")
    password = "pbkdf2_sha256$600000$Nhn7kL55O0rKMEzGd59oTm$9XFB9m6u+Ro8fThSWtvpdyBNQ9Rle+f/40Aq0k92vDg="


class EmailFactory(DjangoEmailFactory):
    class Meta:
        model = Email

    user = factory.SubFactory(UserFactory)
    sender = factory.SubFactory(UserFactory)
    subject = factory.Faker("sentence", nb_words=)
