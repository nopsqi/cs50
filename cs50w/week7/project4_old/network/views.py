import json
from django.core.paginator import Paginator, EmptyPage
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import User, Post


@login_required(login_url="login")
def user(request, username):
    return render(request, "network/index.html", {"api": f"/posts?user={username}&page=1"})


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
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


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
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

class api:
    @staticmethod
    @login_required(login_url="login")
    def posts(request):
        if request.method != "GET":
            return JsonResponse({"error": "GET request required"}, status=400)

        pages = None

        if request.GET.get("user"):
            try:
                user = User.objects.get(username=request.GET.get("user"))
            except User.DoesNotExist:
                return JsonResponse({"error": "User not found"}, status=400)
            pages = Post.objects.filter(user=user).order_by("-modified")

        if str(request.GET.get("following")).lower() == "true":
            if not pages:
                pages = Post.objects
            pages = pages.filter(user__followers=request.user)

        if not pages:
            pages = Post.objects.order_by("-modified")

        pages = Paginator(pages, 10)

        try:
            page = int(request.GET.get("page"))
            posts = pages.page(page)
        except ValueError:
            return JsonResponse({"eror": "Page must be a number."}, status=400)
        except EmptyPage:
            return JsonResponse({"error": "Page not found"}, status=404)


        posts = [post.serialize() for post in posts]
        for post in posts:
            post["like"] = request.user.username in post["likes"]

        return JsonResponse({
            "page": page,
            "pages": len(pages.page_range),
            "posts": posts
        }, safe=False)

    @staticmethod
    @csrf_exempt
    @login_required(login_url="login")
    def post(request):
        if request.method != "POST":
            return JsonResponse({"error": "POST request required"}, status=400)

        if (content := json.loads(request.body).get('content')):
            post = Post(user=request.user, content=content)
            post.save()
            return JsonResponse(post.serialize(), safe=False)

        return JsonResponse({"error": "Post can't be empty"}, status=400)


    @staticmethod
    @login_required(login_url="login")
    def user(request):
        if request.method != "GET":
            return JsonResponse({"error": "GET request required"}, status=400)

        try:
            user = User.objects.get(username=request.GET.get("username")).serialize()
            user["is_mine"] = request.user.id == user["id"]
            user["is_follow"] = request.user.username in user["followers"]
            return JsonResponse(user, safe=False)
        except User.DoesNotExist:
            return JsonResponse({"error": "User doesn't exist"}, status=404)


class pages:
    @staticmethod
    @login_required(login_url="login")
    def index(request):
        return render(request, "network/index.html", {"api": "/api/posts"})

    @login_required(login_url="login")
    def profile(request, username):
        get_object_or_404(User, username=username)
        return render(request, "network/profile.html", {"api": f"/api/posts?user={username}"})