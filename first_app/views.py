from django.shortcuts import render
from django.http import HttpResponse

def first_app(request):
    return HttpResponse("Hello World!")
