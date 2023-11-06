import random
from django.utils import timezone
from mail.models import User, Email
import factory
from factory.django import DjangoModelFactory


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("email")
    password = "pbkdf2_sha256$600000$Nhn7kL55O0rKMEzGd59oTm$9XFB9m6u+Ro8fThSWtvpdyBNQ9Rle+f/40Aq0k92vDg="


class EmailFactory(DjangoModelFactory):
    class Meta:
        model = Email

    user = factory.SubFactory(UserFactory)
    sender = factory.SubFactory(UserFactory)
    subject = factory.Faker("sentence", nb_words=random.randint(1, 4))
    body = factory.Faker("text")
    timestamp = factory.Faker("date_time_between", start_date="-1y", end_date="now", tzinfo=timezone.get_current_timezone())
    read = factory.LazyAttribute(lambda o: True if o.user == o.sender else factory.Faker("boolean"))
    archived = factory.Faker("boolean")

    @factory.post_generation
    def recipients(self, create, extracted):
        if not create:
            return
        if extracted:
            for recipient in extracted:
                self.recipients.add(recipient)


if User.objects.count() == 0:
    UserFactory.create_batch(20)

if Email.objects.count() == 0:
    for sender in random.sample(list(User.objects.all()), round(User.objects.count() * (2/3))):
        users = User.objects.all()
        for _ in range(5):
            EmailFactory(
                user=random.choice(list(users.exclude(id=sender.id))),
                sender=sender
                recipients=random.sample(list(users), random.randint(1, users.count()))
            )
