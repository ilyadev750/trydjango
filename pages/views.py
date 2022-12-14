from django.http import HttpResponse
from django.shortcuts import render

def homepage(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello, World</h1>")
    print(request.user)
    return render(request, "home.html", {})

def another_view(request, *args, **kwargs):
    return render(request, "another_info.html", {})

def rendering(request, *args, **kwargs):
    my_context = {
        "my_text": "This is horosho!",
        "number": 305,
        "items": [1,2,3,4,5]
    }
    return render(request, "new_home.html", my_context)