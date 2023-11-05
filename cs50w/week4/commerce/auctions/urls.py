from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("watchlist", views.watchlist.show, name="watchlist"),
    path("watchlist/add", views.watchlist.modify, name="watchlist.add"),
    path("watchlist/delete", views.watchlist.modify, name="watchlist.delete"),
    path("listing", views.listing.show, name="listing.show"),
    path("listing/close", views.listing.close, name="listing.close"),
    path("listing/delete", views.listing.delete, name="listing.delete"),
    path("listing/bid", views.listing.bid, name="listing.bid"),
    path("comment/add", views.comment.add, name="comment.add"),
    path("<str:username>", views.listings, name="listings"),
]
