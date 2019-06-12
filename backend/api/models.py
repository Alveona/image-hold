from django.db import models
from django.conf import settings
# Create your models here.

class Image(models.Model):
    img = models.ImageField(upload_to='images/')
    date = models.DateField(auto_now_add=True)
    size = models.IntegerField()
    place = models.CharField(max_length = 255)
