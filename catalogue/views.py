from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Welcome to Home Page</h1>')

# def index(request):
#     return HttpResponse("Hello, world. You're at the catalogue index.")