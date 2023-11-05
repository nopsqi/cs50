import re
from decimal import Decimal
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import (
    HttpResponse,
    HttpResponseRedirect,
    HttpResponseForbidden,
    HttpResponseNotFound,
)
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from django.db.models import Q

from .models import User, Category, Listing, Watchlist, Bid, Comment


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        exclude = ["active", "user"]
        labels = {"url": "Image URL"}

    def __init__(self, *args, **kwargs):
        super(ListingForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update(
                {
                    "class": "form-control"
                }
            )
        self.fields["name"].widget.attrs["value"] = "Name"
        self.fields["url"].widget.attrs["value"] = ""
        print(self.fields["url"].widget.attrs)


class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ["amount"]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        self.listing = kwargs.pop("listing")

        super().__init__(*args, **kwargs)

        for field in iter(self.fields):
            self.fields[field].label = ""
            self.fields[field].widget.attrs["class"] = "form-control"
            self.fields[field].disabled = self.request.user == self.listing.winner
            # self.fields[field].disabled = False
        min_value = self.listing.current_bid + Decimal(1)
        self.fields["amount"].widget.attrs["value"] = round(min_value, 2)
        self.fields["amount"].validators = [MinValueValidator(min_value)]


    def clean(self):
        cleaned_data = super().clean()
        if self.request.user == self.listing.winner:
            raise ValidationError("You already the highest bid")
        cleaned_data["user"] = self.request.user
        cleaned_data["listing"] = self.listing
        return cleaned_data


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
        labels = {"content": ""}
        widgets = {
            "content": forms.Textarea(attrs={"class": "form-control", "rows": 3})
        }


@login_required(login_url="login")
def index(request):
    listings = Listing.objects.exclude(Q(user=request.user) | Q(active=False) | Q(id__in=request.user.watchlist.get().listings.all())).order_by("-modified")
    for listing in listings:
        listing.is_in_watchlist = listing in request.user.watchlist.get().listings.all()
    return render(request, "auctions/index.html", {"title": "All listings", "listings": listings})


def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(
                request,
                "auctions/login.html",
                {"message": "Invalid username and/or password."},
            )
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(
                request, "auctions/register.html", {"message": "Passwords must match."}
            )

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(
                request,
                "auctions/register.html",
                {"message": "Username already taken."},
            )
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


@login_required(login_url="login")
def create(request):
    if request.method == "GET":
        return render(request, "auctions/create.html", {"form": ListingForm()})

    form = ListingForm(request.POST)
    if form.is_valid():
        form.instance.user = request.user
        form.instance.current_bid = form.instance.starting_bid
        listing = form.save()
        return HttpResponseRedirect(f"{reverse('listing.show')}?id={listing.id}")
    else:
        return render(request, "auctions/create.html", {"form": form})


@login_required(login_url="login")
def listings(request, username):
    listings = get_object_or_404(User, username=username).listings.order_by("-modified")
    for listing in listings:
        listing.is_in_watchlist = listing in request.user.watchlist.get().listings.all()
    return render(
        request,
        "auctions/index.html",
        {"title": f"{username} listings", "listings": listings},
    )


class listing:
    @staticmethod
    @login_required(login_url="login")
    def show(request):
        listing = get_object_or_404(Listing, id=request.GET.get("id"))
        listing.is_in_watchlist = listing in request.user.watchlist.get().listings.all()
        bid_form = BidForm(listing=listing, request=request)
        return render(
            request,
            "auctions/listing.html",
            {
                "listing": listing,
                "is_winner": bid_form.fields["amount"].disabled,
                "bid_form": bid_form,
                "comment_form": CommentForm(),
            },
        )

    @staticmethod
    @login_required(login_url="login")
    def bid(request):
        if request.method == "GET":
            return HttpResponseForbidden()

        listing = get_object_or_404(Listing, id=request.POST.get("id"))
        if listing.user == request.user:
            return HttpResponseRedirect(f"{reverse('listing.show')}?id={listing.id}")
        form = BidForm(request.POST, request=request, listing=listing)
        if not form.is_valid():
            return render(
                request, "auctions/listing.html", {"listing": listing, "bid_form": form}
            )
        if bid := Bid.objects.filter(
            user=form.cleaned_data["user"], listing=form.cleaned_data["listing"]
        ).first():
            bid.amount = form.cleaned_data["amount"]
            bid.save()
        else:
            form.instance.user = form.cleaned_data["user"]
            form.instance.listing = form.cleaned_data["listing"]
            form.save()

        return HttpResponseRedirect(f"{reverse('listing.show')}?id={listing.id}")

    @staticmethod
    @login_required(login_url="login")
    def delete(request):
        if request.method == "GET":
            return HttpResponseForbidden()

        listing = get_object_or_404(Listing, id=request.POST.get("id"))
        if listing.user != request.user:
            return HttpResponseForbidden()
        listing.delete()
        if re.search(r"id=\d+", request.POST.get("prev")):
            return HttpResponseRedirect(reverse("listings", args=[request.user]))
        return HttpResponseRedirect(request.POST.get("prev"))

    @staticmethod
    @login_required(login_url="login")
    def close(request):
        if request.method == "GET":
            return HttpResponseForbidden()

        listing = get_object_or_404(Listing, id=request.POST.get("id"))
        if listing.user != request.user:
            return HttpResponseForbidden()
        listing.active = False
        listing.save()
        return HttpResponseRedirect(request.POST.get("prev"))


class watchlist:
    @staticmethod
    @login_required(login_url="login")
    def show(request):
        listings = (
            User.objects.get(username=request.user)
            .watchlist.get()
            .listings.all()
            .order_by("-modified")
        )
        for listing in listings:
            listing.is_in_watchlist = True
        return render(request, "auctions/index.html", {"title": "Watchlist", "listings": listings})

    @staticmethod
    @login_required(login_url="login")
    def modify(request):
        if request.method == "GET":
            return HttpResponseForbidden()

        listing = get_object_or_404(Listing, id=request.POST.get("id"))
        if listing.user != request.user:
            if request.POST.get("action") == "add":
                request.user.watchlist.get().listings.add(listing)
            if request.POST.get("action") == "delete":
                request.user.watchlist.get().listings.remove(listing)
        return HttpResponseRedirect(f"{request.POST.get('prev', reverse('index'))}")


class comment:
    @staticmethod
    @login_required(login_url="login")
    def add(request):
        if request.method == "GET":
            return HttpResponseForbidden()

        listing = get_object_or_404(Listing, id=request.POST.get("id"))
        bid_form = BidForm(request=request, listing=listing)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form.instance.user = request.user
            comment_form.instance.listing = listing
            listing.comments.add(comment_form.instance, bulk=False)
        else:
            return render(
                request,
                "auctions/listing",
                {
                    "listing": listing,
                    "is_winner": bid_form.fields["amount"].disabled,
                    "bid_form": bid_form,
                    "comment_form": comment_form,
                },
            )
        return HttpResponseRedirect(f"{reverse('listing.show')}?id={listing.id}")


@login_required(login_url="login")
def search(request):
    listings = Listing.objects.order_by("-modified")
    print(dir(request.GET))
    print(list(request.GET.lists()))
    if request.GET.get("category"):
        categories = [
            get_object_or_404(Category, name=category.lower())
            for category in request.GET.getlist("category")
        ]
        for category in categories:
            listings = listings.filter(categories=category)
    for listing in listings:
        listing.show_in_list = True
    return render(
        request,
        "auctions/index.html",
        {
            "title": "Search "
            + ", ".join([f"{key}: {value}" for key, value in request.GET.lists()]),
            "listings": listings,
        },
    )


@login_required(login_url="login")
def categories(request):
    return render(
        request, "auctions/categories.html", {"categories": Category.objects.all()}
    )
