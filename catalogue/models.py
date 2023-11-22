from django.db import models

class Track(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    audio_file = models.FileField(blank=True,null=True)
    audio_link = models.CharField(max_length=200,blank=True,null=True)
    image = models.ImageField(upload_to='catalogue/images/')
    url = models.URLField(blank=True)

# Create your models here.
