
from hashlib import blake2b
from django.db import models
from PIL import Image
from django_resized import ResizedImageField
from django_countries.fields import CountryField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Color(models.Model):
    color = models.CharField(max_length=100)

    def __str__(self):
        return str(self.color)


class Brend(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)


class Car(models.Model):
    # images = models.FileField(blank=True, null=True)
    brend = models.ForeignKey(Brend, on_delete=models.CASCADE, related_name='cars', blank=True, null=True)
    name = models.CharField(max_length=250, blank=True)
    description = models.TextField(blank=True)
    color = models.ManyToManyField(Color, blank=True)
    country = CountryField(blank=True)
    year = models.CharField(max_length=250, blank=True, null=True)
    type_body = models.CharField(max_length=300, verbose_name='kuzov', blank=True)
    number_place = models.CharField(max_length=250, blank=True, null=True)
    number_door = models.CharField(max_length=250, blank=True, null=True)
    power_motor = models.CharField(max_length=250, blank=True, null=True)
    power_battery = models.CharField(max_length=250, blank=True, null=True)
    power_reserve = models.CharField(max_length=250, verbose_name='quvvat_zahirasi', blank=True, null=True)
    max_speed = models.CharField(max_length=250, blank=True, null=True)
    acceleration = models.CharField(max_length=250, verbose_name='tezlanish', blank=True, null=True)
    length = models.CharField(max_length=250, blank=True, null=True)
    width = models.CharField(max_length=250, blank=True, null=True)
    height = models.CharField(max_length=250, blank=True, null=True)

    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class CarImage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='car_images', null=True, blank=True)
    image = models.FileField(upload_to='image', blank=True, null=True)
    video = models.FileField(upload_to='car/videos', blank=True, null=True)

    small = ImageSpecField(
        source='image',
        processors=[ResizeToFill(250, 250)],
        format='JPEG',
        options={'quality': 100}
    )
    medium = ImageSpecField(
        source='image',
        processors=[ResizeToFill(400, 400)],
        format='JPEG',
        options={'quality': 100}
    )                              
    large = ImageSpecField(
        source='image',
        processors=[ResizeToFill(800, 800)],
        format='JPEG',
        options={'quality': 100}
    )


