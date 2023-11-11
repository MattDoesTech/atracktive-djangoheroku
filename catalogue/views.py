from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse('<h1>Welcome to Home Page</h1>')

def about(request):
    return HttpResponse('<h1>Welcome to About Page</h1>')

# def index(request):
#     return HttpResponse("Hello, world. You're at the catalogue index.")