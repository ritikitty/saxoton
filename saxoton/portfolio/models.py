from django.db import models
from django.contrib.auth.models import User
from django import forms
import os

class FeaturedWorks(models.Model):
    TitleFat = models.CharField(max_length=100)
    TitleNormal = models.CharField(max_length=100)
    Name = models.CharField(max_length=100)
    Description = models.CharField(max_length=100)
    image = models.ImageField(blank=True, null=True, upload_to='media')
    
    def __str__(self):
        return self.Name

class Gigs(models.Model):
    Name = models.CharField(max_length=100)
    Date = models.DateTimeField(null=True)
    Ticket = models.CharField(max_length=100)

class GalleryPicture(models.Model):
    Name = models.CharField(max_length=100)
    Description = models.CharField(max_length=100)
    image = models.ImageField(blank=True, null=True, upload_to='media')
    
