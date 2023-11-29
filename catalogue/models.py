from django.db import models

class Track(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    audio_file = models.FileField(blank=True,null=True,upload_to='catalogue/audio/')
    audio_link = models.CharField(max_length=200,blank=True,null=True)
    image = models.ImageField(upload_to='catalogue/images/tracks')  
    # url = models.URLField(blank=True)
    def __str__(self):
        return self.name

class Artist(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='catalogue/images/artists')

    def __str__(self):
        return self.name
    
class Album(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    artist = models.ManyToManyField(Artist)
    tracks = models.ManyToManyField(Track)
    image = models.ImageField(upload_to='catalogue/images/albums')

    def __str__(self):
        return self.name

# Create your models here.
