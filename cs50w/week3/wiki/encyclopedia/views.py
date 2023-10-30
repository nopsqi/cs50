from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry_page(request, title):
    return render(request, f"encyclopedia/entry_page.html", {
        "entry": util.get_entry(title)
    })

