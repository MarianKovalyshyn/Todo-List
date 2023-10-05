from django.shortcuts import render
from django.views import generic

from todo.models import Tag


def index(request) -> render:
    return render(request, "todo/index.html")


class TagListView(generic.ListView):
    model = Tag
