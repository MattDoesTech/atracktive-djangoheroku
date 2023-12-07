from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("signup/", views.signup, name="signup"),
    path("view1/", views.view1, name="view1"),
    path("view2/", views.view2, name="view2"),
    path("view3/", views.view3, name="view3"),
    path("signout/", views.signout, name="signout"),
]
urlpatterns += static(settings.MEDIA_URL, 
  document_root=settings.MEDIA_ROOT)