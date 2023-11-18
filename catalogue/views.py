from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    searchTrack = request.GET.get('searchTrack')
    return render(request, 'home.html', {'searchTrack': searchTrack})

def signup(request):
    email = request.Get.get('email')
    return render(request, 'signup.html', {'email':email})

def about(request):
    return render(request, 'about.html')

# def index(request):
#     return HttpResponse("Hello, world. You're at the catalogue index.")