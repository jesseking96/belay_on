from django.db import models

# Create your models here.
class Event(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    picture = models.ImageField(upload_to='images/')
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)
