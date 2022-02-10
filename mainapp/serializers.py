from dataclasses import fields
from rest_framework import serializers

from .models import (
    CarImage,
    Color,
    Brend,
    Car
)




class ColorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ('color',)

class BrendSerializers(serializers.ModelSerializer):
    class Meta:
        model = Brend
        fields = ('name',)

class CarSerializers(serializers.ModelSerializer):
    color = serializers.CharField()
    brend = serializers.CharField()
    class Meta:
        model = Car
        fields = (
            'brend',
            'name',
            'description',
            'color',
            'country',
            'year',
            'type_body',
            'number_place',
            'number_door',
            'power_motor',
            'power_battery',
            'power_reserve',
            'max_speed',
            'acceleration',
            'length',
            'width',
            'height',
        )

class CarImageSerializers(serializers.ModelSerializer):
    car = serializers.CharField()
    class Meta:
        model = CarImage
        fields = ('image', 'video', 'car')