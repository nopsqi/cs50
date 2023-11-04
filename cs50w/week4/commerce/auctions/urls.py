from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("listing", views.listing, name="listing"),
    path("close", views.close, name="close"),
    path("delete", views.delete, name="delete"),
    path("bid", views.bid, name="bid"),
    path("<str:username>", views.listings, name="listings"),
]
