from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('hello')

def room(request):
    return HttpResponse('You are in the Backrooms')
