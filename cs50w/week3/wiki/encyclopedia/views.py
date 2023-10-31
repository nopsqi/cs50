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
    return render(request, "encyclopedia/entry_page.html", {
        "title": title,
        "entry": entry
    })

def search(request):
    print(util.search_entry(request.GET["q"]))
    return render(request, "encyclopedia/search_result.html", {
        "query": request.GET["q"],
        "result": util.search_entry(request.GET["q"])
    })

