from django.shortcuts import render, get_object_or_404

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry_page(request, title):
    return render(request, f"encyclopedia/entry_page.html", {
        "entry": get_object_or_404(util.get_entry(title))
    })

