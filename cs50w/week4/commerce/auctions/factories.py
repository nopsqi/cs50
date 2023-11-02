import random
import factory
from auctions.models import User, Category, Listing, Bid, BidHistory, Comment


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("user_name")
    email = factory.Faker("email")
    password = "pbkdf2_sha256$600000$Nhn7kL55O0rKMEzGd59oTm$9XFB9m6u+Ro8fThSWtvpdyBNQ9Rle+f/40Aq0k92vDg="


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker("word")


class ListingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Listing

    user_id = factory.SubFactory(UserFactory)
    name = factory.Faker("text", max_nb_chars=32)
    description = factory.Faker("text", max_nb_chars=64)
    url = "https://fakeimg.pl/350x200/?text=Image"
    starting_bid = factory.Faker("random_int", min=50, max=500000)

    @factory.post_generation
    def categories(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for category in extracted:
                self.categories.add(category)
        else:
            categories = CategoryFactory.create_batch(random.randint(1, 5))
            self.categories.add(*categories)


UserFactory.create_batch(5)
# CategoryFactory.create_batch(10)

for user in random.sample(list(User.objects.exclude(username="admin")), 3):
    ListingFactory.create_batch(5, user_id=user)
