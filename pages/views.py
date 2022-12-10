from django.http import HttpResponse
from django.shortcuts import render

def homepage(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello, World</h1>")
    print(request.user)
    return render(request, "home.html", {})

def another_view(request, *args, **kwargs):
    return render(request, "another_info.html", {})
