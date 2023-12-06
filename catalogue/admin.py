from django.contrib import admin
from .models import Track
from .models import Artist
from .models import Album
admin.site.register(Track)
admin.site.register(Album)
admin.site.register(Artist)
# Register your models here.
