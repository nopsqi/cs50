import random
import factory
from django.utils import timezone
from factory.django import DjangoModelFactory
from network.models import *


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("user_name")
    email = factory.Faker("email")
    password = "pbkdf2_sha256$600000$Nhn7kL55O0rKMEzGd59oTm$9XFB9m6u+Ro8fThSWtvpdyBNQ9Rle+f/40Aq0k92vDg="

    @factory.post_generation
    def followings(self, created, extracted):
        if not created:
            return
        if extracted:
            for following in extracted:
                self.followings.add(following)

    @factory.post_generation
    def followers(self, created, extracted):
        if not created:
            return
        if extracted:
            for follower in extracted:
                self.followers.add(follower)


class PostFactory(DjangoModelFactory):
    class Meta:
        model = Post

    created = lambda _: factory.Faker("date_time_between", start_date="-1y", end_date="now", tzinfo=timezone.get_current_timezone())
    modified = factory.LazyAttribute(lambda o: o.created)
    user = factory.SubFactory(UserFactory)
    content = factory.Faker("text")

    @factory.post_generation
    def likes(self, created, extracted):
        if not created:
            return
        if extracted:
            for like in extracted:
                self.likes.add(like)


if User.objects.count() == 0:
    UserFactory.create_batch(20)
    users = User.objects.all()
    for user in random.sample(list(users), round(users.count() * 0.5)):
        followers = users.exclude(id=user.id)
        followers = random.sample(list(followers), random.randint(
            1,
            followers.count()
        ))
        user.followers.add(*followers)

if Post.objects.count() == 0:
    users = User.objects.all()
    for user in random.sample(list(users), round(users.count() * 0.8)):
        for _ in range(2):
            likes = users.exclude(id=user.id)
            likes = random.sample(list(likes), random.randint(
                1,
                likes.count()
            ))
            PostFactory(user=user, likes=likes)
