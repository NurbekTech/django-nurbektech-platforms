from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello, Django!</h1>")


def page_not_found(request, exception):
    return HttpResponseNotFound("Page Not Found")
