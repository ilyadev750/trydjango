from django.http import HttpResponse
from django.shortcuts import render

def homepage(*args, **kwargs):
    return HttpResponse("<h1>Hello, World</h1>")

def another_view(*args, **kwargs):
    return HttpResponse("<h4>Another view/h4>")
