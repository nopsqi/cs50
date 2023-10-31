from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry_page(request, title):
    if not (entry := util.get_entry(title)):
        raise Http404("Entry doesn't exist")
    return render(request, f"encyclopedia/entry_page.html", {
        "entry": entry
    })

def search(request):
    if request.method == "GET":
        return HttpResponse(request.GET["q"])

