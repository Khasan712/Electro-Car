from django.conf import settings
from django.db import models


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
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='blog/images')
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
