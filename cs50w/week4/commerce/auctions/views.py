from decimal import Decimal
import re
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError

from .models import User, Category, Listing, Bid


class ListingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ListingForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                "class": "form-group d-flex justify-content-around" if field == "categories" else "form-control"
            })

    class Meta:
        model = Listing
        exclude = ["active", "user", "current_bid"]
        labels = {
            "url": "Image URL"
        }
        widgets = {
            "categories": forms.CheckboxSelectMultiple
        }


class BidForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        self.listing = kwargs.pop("listing")
        if (bid := self.listing.bids.order_by("-amount").first()):
            self.highest_bidder = bid.user
        else:
            self.highest_bidder = None

        super().__init__(*args, **kwargs)

        for field in iter(self.fields):
            self.fields[field].label = ""
            self.fields[field].widget.attrs["class"] = "form-control"
            self.fields[field].disabled = self.request.user == self.highest_bidder
            # self.fields[field].disabled = False
        min_value = self.listing.current_bid + Decimal(1)
        self.fields["amount"].widget.attrs["value"] = round(min_value, 2)
        self.fields["amount"].validators = [MinValueValidator(min_value)]

    class Meta:
        model = Bid
        fields = ["amount"]

    def clean(self):
        cleaned_data = super().clean()
        if self.request.user == self.highest_bidder:
            raise ValidationError("You already the highest bid")
        cleaned_data["user"] = self.request.user
        cleaned_data["listing"] = self.listing
        return cleaned_data


@login_required(login_url="login")
def index(request):
    for listing in Listing.objects.all():
        if listing.current_bid:
            continue
        if (bid := listing.bids.order_by("-amount").first()):
            listing.current_bid = bid.amount
        else:
            listing.current_bid = listing.starting_bid
        listing.save()
    return render(request, "auctions/index.html", {
        "listings": Listing.objects.all()
    })


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
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
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
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


@login_required(login_url="login")
def create(request):
    if request.method == "POST":
        form = ListingForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.instance.current_bid = form.instance.starting_bid
            listing = form.save()
            return HttpResponseRedirect(f"{reverse('listing')}?id={listing.id}")
        else:
            return render(request, "auctions/create.html", {
                "form": form
            })

    return render(request, "auctions/create.html", {
        "form": ListingForm()
    })


@login_required(login_url="login")
def listings(request, username):
    return render(request, "auctions/index.html", {
        "title": f"{username} Listings",
        "listings": get_object_or_404(User, username=username).listings.all()
    })


@login_required(login_url="login")
def listing(request):
    listing = get_object_or_404(Listing, id=request.GET.get("id"))
    form = BidForm(listing=listing, request=request)
    return render(request, "auctions/listing.html", {
        "listing": listing,
        "bid_form": form,
        "is_winner": form.fields["amount"].disabled
    })


@login_required(login_url="login")
def delete(request):
    listing = get_object_or_404(Listing, id=request.GET.get("id"))
    if request.user == listing.user:
        listing.delete()
        if re.search(r"id=\d+", request.GET.get("prev", "")):
            return HttpResponseRedirect(reverse("index"))
        return HttpResponseRedirect(request.GET.get("prev", reverse("index")))

    return HttpResponseForbidden()


@login_required(login_url="login")
def bid(request):
    if request.method == "POST":
        listing = get_object_or_404(Listing, id=request.POST.get("id"))
        if listing.user == request.user:
            return HttpResponseRedirect(f"{reverse('listing')}?id={listing.id}")
        form = BidForm(request.POST, request=request, listing=listing)
        if not form.is_valid():
            return render(request, "auctions/listing.html", {
                "listing": listing,
                "bid_form": form
            })
        if (bid := Bid.objects.filter(user=form.cleaned_data["user"], listing=form.cleaned_data["listing"]).first()):
            bid.amount = form.cleaned_data["amount"]
            bid.save()
        else:
            form.instance.user = form.cleaned_data["user"]
            form.instance.listing = form.cleaned_data["listing"]
            form.save()
        listing.current_bid = form.cleaned_data["amount"]
        listing.save()

        return HttpResponseRedirect(f"{reverse('listing')}?id={listing.id}")

    return HttpResponseForbidden()


@login_required(login_url="login")
def close(request):
    listing = get_object_or_404(Listing, id=request.GET.get("id"))
