import random
from django import forms
from django.core.exceptions import ValidationError
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import Http404, HttpResponse, HttpResponseRedirect
import markdown2

from . import util


class EditEntryForm(forms.Form):
    markdown = forms.CharField(label="Markdown", widget=forms.Textarea(attrs={"rows": 15}))


def validate_title(title):
    if util.get_entry(title):
        raise ValidationError(f"Value with title {title} exist")


class NewEntryForm(EditEntryForm):
    title = forms.CharField(label="Title", widget=forms.Textarea(attrs={"rows": 1}), validators=[validate_title])

    field_order = ["title", "markdown"]


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title):
    if not (entry := util.get_entry(title)):
        raise Http404("Entry doesn't exist")
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "entry": markdown2.markdown(entry),
    })


def search(request):
    return render(request, "encyclopedia/search.html", {
        "query": request.GET["q"],
        "result": util.search_entry(request.GET["q"])
    })


def create(request):
    if request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_valid():
            util.save_entry(form.cleaned_data["title"], form.cleaned_data["markdown"])
            return HttpResponseRedirect(reverse("entry", args=[request.POST["title"]]))
        else:
            return render(request, "encyclopedia/create.html", {
                "form": form
            })

    return render(request, "encyclopedia/create.html", {
        "form": NewEntryForm()
    })


def edit(request, title):
    if request.method == "POST":
        util.save_entry(title, request.POST["markdown"])
        return HttpResponseRedirect(reverse("entry", args=[title]))
    return render(request, "encyclopedia/edit.html", {
        "title": title,
        "form": {"markdown": util.get_entry(title)},
    })


def random_page(request):
    return HttpResponseRedirect(reverse("entry", args=[random.choice(util.list_entries())]))


def delete(request, title):
    util.delete(title)
    return HttpResponseRedirect(reverse("index"))
