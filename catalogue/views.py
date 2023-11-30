from django.http import HttpResponse
from django.shortcuts import render
from .models import Track
from .models import Album
from .models import Artist

def home(request):
    # searchTerm = request.GET.get('searchTerm')
    albums = Album.objects.all()
    artists = Artist.objects.all()
    tracks = Track.objects.all()
    return render(request, 'home.html', {'albums': albums}, {'artists': artists}, {'tracks':tracks})
    # return render(request, 'home.html', {'searchTerm': searchTerm, 'tracks': tracks})

def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email':email})

def about(request):
    return render(request, 'about.html')

# def index(request):
#     return HttpResponse("Hello, world. You're at the catalogue index.")