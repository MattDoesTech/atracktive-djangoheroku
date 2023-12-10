from django.http import HttpResponse
from django.shortcuts import render
from .models import Album, Artist, Track

def home(request):
    albums = Album.objects.all()
    

    context = {
        'albums': albums,
        'artist': Artist.objects.all(),  # Include artists in the context
        'tracks': Track.objects.all(),      # Include songs in the context
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

def view1(request):
    return render(request, 'view1.html')

def view2(request):
    return render(request, 'view2.html')

def view3(request):
    return render(request, 'view3.html')

def sign_out(request):
    return render(request, 'sign_out.html')

# def index(request):
#     return HttpResponse("Hello, world. You're at the catalogue index.")