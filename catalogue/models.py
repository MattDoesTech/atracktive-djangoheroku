from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to='catalogue/images/artists')

    def __str__(self):
        return self.name
    
class Track(models.Model):
    name = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    description = models.CharField(max_length=250)
    audio_file = models.FileField(blank=True,null=True,upload_to='catalogue/audio/')
    image = models.ImageField(upload_to='catalogue/images/tracks')  
    release_date = models.DateField(auto_now_add=True)
    # audio_link = models.CharField(max_length=200,blank=True,null=True)
    # url = models.URLField(blank=True)
    def __str__(self):
        return self.name
    
    
class Album(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    release_date = models.DateField(auto_now_add=True)
    artists = models.ForeignKey(Artist, on_delete=models.CASCADE)
    tracks = models.ManyToManyField(Track)
    image = models.ImageField(upload_to='catalogue/images/albums')

    def __str__(self):
        return self.name

# Create your models here.

# class Artist(models.Model):
#     name = models.CharField(max_length=100)
#     bio = models.TextField()

# class Song(models.Model):
#     title = models.CharField(max_length=100)
#     artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
#     audio_file = models.FileField(upload_to='audio/')
#     release_date = models.DateField()

# class Album(models.Model):
#     title = models.CharField(max_length=100)
#     artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
#     release_date = models.DateField()
#     songs = models.ManyToManyField(Song)
