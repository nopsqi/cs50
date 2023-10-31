from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import Http404, HttpResponse, HttpResponseRedirect

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry_page(request, title):
    if not (entry := util.get_entry(title)):
        raise Http404("Entry doesn't exist")
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "entry": entry
    })


def search(request):
    return render(request, "encyclopedia/search.html", {
        "query": request.GET["q"],
        "result": util.search_entry(request.GET["q"])
    })


def create(request):
    if request.method == "POST":
        if util.get_entry(request.POST["title"]):
            raise Http404(f"Entry with title {request.POST['title']} exist")
        util.save_entry(request.POST["title"], request.POST["markdown"])
        return HttpResponseRedirect(reverse("entry", args=[request.POST["title"]]))
    return render(request, "encyclopedia/create.html")

