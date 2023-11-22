from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("signup/", views.signup, name="signup"),
]
urlpatterns += static(settings.MEDIA_URL, 
  document_root=settings.MEDIA_ROOT)