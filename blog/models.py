from distutils.command.upload import upload
from email.mime import image
import re
from turtle import title
from django.db import models

# Create your models here.

class Header(models.Model):
    video = models.FileField(upload_to='header/vidoe', blank=True)
    image = models.ImageField(upload_to='header/image', blank=True)
    title = models.CharField(max_length=500, blank=True)    
    content = models.CharField(max_length=500, blank=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Post(models.Model):
    image = models.ImageField(upload_to='blog/images')
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
