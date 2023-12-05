from django.http import HttpResponse
from django.shortcuts import render
from .models import Track
from .models import Album
from .models import Artist

def home(request):
    albums = Album.objects.first()

    context = {
        'albums': albums,
    }

    return render(request, 'home.html', context)
    # searchTerm = request.GET.get('searchTerm')
    # albums = Album.objects.all()
    # return render(request, 'home.html', {'albums': albums})
    # return render(request, 'home.html', {'searchTerm': searchTerm, 'tracks': tracks})

def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email':email})

def about(request):
    return render(request, 'about.html')

# def index(request):
#     return HttpResponse("Hello, world. You're at the catalogue index.")