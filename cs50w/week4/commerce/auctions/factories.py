import random
import pytz
import factory
from factory.django import DjangoModelFactory
from auctions.models import User, Category, Listing, Watchlist, Bid, Comment


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
    url = factory.LazyAttribute(lambda o: f"https://fakeimg.pl/400x400/?text={o.name}")
    starting_bid = factory.Faker("random_int", min=10, max=50)

    @factory.post_generation
    def categories(self, create, extracted):
        if not create:
            return

        if extracted:
            for category in extracted:
                self.categories.add(category)
        else:
            categories = CategoryFactory.create_batch(random.randint(1, 5))
            self.categories.add(*categories)


class WatchlistFactory(DjangoModelFactory):
    class Meta:
        model = Watchlist

    user = factory.SubFactory(UserFactory)

    @factory.post_generation
    def listings(self, create, extracted):
        if not create:
            return

        if extracted:
            for listing in extracted:
                self.listings.add(listing)

        else:
            listings = ListingFactory.create_batch(random.randint(1, 10))
            self.listings.add(*listings)


class BidFactory(DjangoModelFactory):
    class Meta:
        model = Bid

    user = factory.SubFactory(UserFactory)
    listing = factory.SubFactory(ListingFactory)
    amount = factory.LazyAttribute(lambda o: random.randint(round(o.listing.starting_bid), 100))
    # amount = factory.Faker("random_int", min=self.listing.starting_bid, max=1000000)


class CommentFactory(DjangoModelFactory):
    class Meta:
        model = Comment

    timestamp = factory.Faker("date_time_between", start_date="-30d", end_date="now", tzinfo=pytz.utc)
    user = factory.SubFactory(UserFactory)
    listing = factory.SubFactory(ListingFactory)
    content = factory.Faker("text", max_nb_chars=300)

if User.objects.all().count() == 0:
    UserFactory.create_batch(10)

if Category.objects.all().count() == 0:
    CategoryFactory.create_batch(10)

if Listing.objects.all().count() == 0:
    users = User.objects.all()
    categories = Category.objects.all()
    n = categories.count() // 2
    for user in random.sample(list(users), users.count() // 2):
        for _ in range(5):
            listing = ListingFactory(user=user, categories=random.sample(list(categories), random.randint(1, n + 1)))

if Watchlist.objects.all().count() == 0:
    for user in User.objects.all():
        listings = Listing.objects.exclude(user=user)
        n = listings.count() // 2
        watchlist = WatchlistFactory(user=user, listings=random.sample(list(listings), random.randint(1, n + 1)))

if Bid.objects.all().count() == 0:
    listings = Listing.objects.all()
    for listing in random.sample(list(listings), round(listings.count() * (2/3))):
        users = User.objects.exclude(username=listing.user)
        for user in random.sample(list(users), users.count() // 2):
            bid = BidFactory(user=user, listing=listing)

if Comment.objects.all().count() == 0:
    listings = Listing.objects.all()
    users = User.objects.all()
    for listing in random.sample(list(listings), round(listings.count() * (2/3))):
        for user in random.sample(list(users), round(users.count() * (2/3))):
            CommentFactory.create_batch(1, user=user, listing=listing)
