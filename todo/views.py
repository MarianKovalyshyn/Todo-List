from django.shortcuts import render


def index(request) -> render:
    return render(request, "todo/index.html")
