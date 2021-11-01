
from django.db import models
from django.db.models.fields import FloatField

# Create your models here.
class weather(models.Model):
    city = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    longitude = models.FloatField(blank=True,null=True)
    lattitude = models.FloatField(blank=True,null=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    temp = models.FloatField(blank=True,null=True)
    tempmax = models.FloatField(blank=True,null=True)
    tempmin = models.FloatField(blank=True,null=True)
    humidity = models.FloatField(blank=True,null=True)
    sunset = models.FloatField(blank=True,null=True)
    sunrise = models.FloatField(blank=True,null=True)
    windspeed = models.FloatField(blank=True,null=True)
    timezone = models.FloatField(blank=True,null=True)
    visibility = models.FloatField(blank=True,null=True)
    
    
     
    
     
