import random
import factory
from factory.django import DjangoModelFactory
from auctions.models import User, Category, Listing, Bid, Comment


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("user_name")
    email = factory.Faker("email")
    password = "pbkdf2_sha256$600000$Nhn7kL55O0rKMEzGd59oTm$9XFB9m6u+Ro8fThSWtvpdyBNQ9Rle+f/40Aq0k92vDg="


class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker("word")


class ListingFactory(DjangoModelFactory):
    class Meta:
        model = Listing

    user = factory.SubFactory(UserFactory)
    name = factory.Faker("text", max_nb_chars=32)
    description = factory.Faker("text", max_nb_chars=64)
    url = f"https://fakeimg.pl/400x400/?text={self.name}"
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


class BidFactory(DjangoModelFactory):
    class Meta:
        model = Bid

    user = factory.SubFactory(UserFactory)
    listing = factory.SubFactory(ListingFactory)
    amount = factory.LazyAttribute(lambda o: random.randint(round(o.listing.starting_bid), 1000000))
    # amount = factory.Faker("random_int", min=self.listing.starting_bid, max=1000000)


class CommentFactory(DjangoModelFactory):
    class Meta:
        model = Comment

    user = factory.SubFactory(UserFactory)
    listing = factory.SubFactory(ListingFactory)
    content = factory.Faker("text", max_nb_chars=300)

if User.objects.all().count() == 0:
    UserFactory.create_batch(5)

if Category.objects.all().count() == 0:
    CategoryFactory.create_batch(10)

if Listing.objects.all().count() == 0:
    for user in random.sample(list(User.objects.exclude(username="administrator")), 3):
        ListingFactory.create_batch(5, user=user, categories=random.sample(list(Category.objects.all()), 4))

if Bid.objects.all().count() == 0:
    for listing in Listing.objects.all():
        for user in User.objects.exclude(username=listing.user):
            bid = BidFactory(user=user, listing=listing)

if Comment.objects.all().count() == 0:
    for listing in Listing.objects.all():
        for user in User.objects.exclude(username="administrator"):
            CommentFactory.create_batch(2, user=user, listing=listing)
