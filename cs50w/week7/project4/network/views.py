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

        if request.GET.get("username"):
            try:
                username = User.objects.get(username=request.GET.get("user"))
            except User.DoesNotExist:
                return JsonResponse({"error": "User not found"}, status=400)
            pages = Post.objects.filter(user=username).order_by("-modified")

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
            return JsonResponse({"error": "Page not found", "pages": len(pages.page_range)}, status=404)


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
        if request.method == "GET":
            return JsonResponse({"error": "POST, DELETE, or PUT request required"}, status=400)

        body = json.loads(request.body)
        id = body.get("id")
        like = body.get("like")
        content = body.get("content")

        if request.method == "POST" and content:
            post = Post(user=request.user, content=content)
            post.save()
            return JsonResponse(post.serialize(), safe=False)

        if not id:
            return JsonResponse({"error": "Post id required"}, status=400)

        try:
            post = Post.objects.get(id=id)
        except Post.DoesNotExist:
            return JsonResponse({"error": "Post doesn't exist"}, status=404)

        if request.method == "PUT" and like is not None:
            if like:
                post.likes.remove(request.user)
            else:
                post.likes.add(request.user)
            serialize = post.serialize()
            serialize["like"] = not like
            return JsonResponse(serialize, safe=False)

        if post.user != request.user:
            return JsonResponse({"error": "Unaothorize action"}, status=400)

        if request.method == "DELETE":
            serialize = post.serialize()
            post.delete()
            return JsonResponse(serialize, safe=False)

        if request.method == "PUT" and content:
            if content == post.content:
                return JsonResponse({"error": "Post content is the same"}, status=400)
            post.content = content
            post.save()
            return JsonResponse(post.serialize(), safe=False)

        return JsonResponse({"error": "Invalid operation"}, status=400)


    @staticmethod
    @login_required(login_url="login")
    def user(request):
        if request.method == 'DELETE':
            return JsonResponse({"error": "GET or PUT request required"}, status=400)

        if request.method == 'GET':
            username = request.GET.get("username")

            if not username:
                return JsonResponse(request.user.serialize(), safe=False)

            try:
                user = User.objects.get(username=username).serialize()
            except User.DoesNotExist:
                return JsonResponse({"error": "User doesn't exist"}, status=404)

            user["is_mine"] = request.user.id == user["id"]
            user["is_follow"] = request.user.username in user["followers"]
            return JsonResponse(user, safe=False)

        if request.method == 'PUT':
            body = json.loads(request.body)
            id = body.get("id")
            is_follow = body.get("is_follow")

            if not id:
                return JsonResponse({"error": "User id required"}, status=400)
            if not is_follow:
                return JsonResponse({"error": "Follow status required"}, status=400)

            try:
                user = User.objects.get(id=id)
            except User.DoesNotExist:
                return JsonResponse({"error": "User doesn't exist"}, status=404)

            if is_follow:
                user.followings.remove(request.user)
                request.user.followers.remove(user)
            else:
                user.followings.add(request.user)
                request.user.followers.add(user)
            serialize = user.serialize()
            serialize["is_follow"] = not is_follow
            return JsonResponse(serialize, safe=False)


class pages:
    @staticmethod
    @login_required(login_url="login")
    def index(request):
        return render(request, "network/index.html", {"api": "/api/posts?page=1"})

    @login_required(login_url="login")
    def profile(request, username):
        get_object_or_404(User, username=username)
        return render(request, "network/profile.html", {"api": f"/api/posts?page=1&username={username}"})
