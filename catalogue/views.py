from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {'name': 'John Doe'})

def about(request):
    return render(request, 'about.html')

# def index(request):
#     return HttpResponse("Hello, world. You're at the catalogue index.")