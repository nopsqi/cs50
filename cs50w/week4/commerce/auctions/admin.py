from django.contrib import admin
from .models import User, Category, Listing, Watchlist, Bid, Comment

# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    filter_horizontal = ("categories",)

class WatchlistAdmin(admin.ModelAdmin):
    filter_horizontal = ("listings",)

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Listing, ListingAdmin)
admin.site.register(Watchlist, WatchlistAdmin)
admin.site.register(Bid)
admin.site.register(Comment)
