from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("watchlist/add", views.add_watchlist, name="watchlist.add"),
    path("listing", views.listing, name="listing"),
    path("listing/close", views.close, name="close"),
    path("listing/delete", views.delete, name="delete"),
    path("listing/bid", views.bid, name="bid"),
    path("<str:username>", views.listings, name="listings"),
]
