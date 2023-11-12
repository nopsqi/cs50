
from django.urls import path

from . import views

urlpatterns = [
    path("", views.pages.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("api/user", views.api.user, name="api.user"),
    path("api/post", views.api.post, name="api.post"),
    path("api/posts", views.api.posts, name="api.posts"),
    path("<str:username>", views.pages.profile, name="profile")
]
