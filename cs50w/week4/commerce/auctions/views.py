from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import User, Category, Listing


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        exclude = ["user", "current_bid"]
        labels = {
            "url": "Image URL"
        }
        widgets = {
            "categories": forms.CheckboxSelectMultiple
        }

    def __init__(self, *args, **kwargs):
        super(ListingForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                "class": "form-group d-flex justify-content-around" if field == "categories" else "form-control"
            })


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
            form.save()
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/create.html", {
                "form": form
            })

    return render(request, "auctions/create.html", {
        "form": ListingForm()
    })


@login_required(login_url="login")
def mylistings(request, username):
    return render(request, "auctions/index.html", {
        "title": f"{username} Listings",
        "listings": Listing.objects.filter(user=User.objects.filter(username=username).first())
    })


def listing(request):
    return render(request, "auctions/listing.html", {
        # "listing": get_object_or_404(Listing, id=request.GET.get("id"))
        "listing": 
    })
