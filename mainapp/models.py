
from keyword import kwlist
from django.db import models
from PIL import Image
from django_resized import ResizedImageField
from django_countries.fields import CountryField
# Create your models here.

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill



class Color(models.Model):
    color = models.CharField(max_length=100)

    def __str__(self):
        return self.color

class Brend(models.Model):
    name = models.CharField(max_length=500)


    def __str__(self):
        return self.name


class Car(models.Model):
    brend = models.ForeignKey(Brend, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=250)
    description = models.TextField()
    color = models.ManyToManyField(Color, blank=True)
    country = CountryField()
    year = models.IntegerField()
    type_body = models.CharField(max_length=300, verbose_name='kuzov')
    number_place = models.IntegerField()
    number_door = models.IntegerField()
    power_motor = models.CharField(max_length=250)
    power_battery = models.FloatField()
    power_reserve = models.IntegerField(verbose_name='quvvat_zahirasi')
    max_speed = models.IntegerField()
    acceleration  = models.FloatField(verbose_name='tezlanish')
    length = models.FloatField()
    width = models.FloatField()
    height = models.FloatField()
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class PostImage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='car_images', null=True)
    image = models.ImageField(upload_to='image')

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


