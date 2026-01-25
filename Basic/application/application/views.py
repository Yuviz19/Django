from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "websites/home.html")


def about(request):
    return render(request, "websites/about.html")


def contact(request):
    return render(request, "websites/contacts.html")
