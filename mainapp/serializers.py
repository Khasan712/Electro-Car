from dataclasses import fields
from rest_framework import serializers

from .models import CarImage, Color, Brend, Car






class ColorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ('color',)


class BrendSerializers(serializers.ModelSerializer):
    # cars_all = serializers.SerializerMethodField()
    # cars = CarSerializers(many=True, read_only=True)
    class Meta:
        model = Brend
        fields = ('name',)

    # def get_cars_all(self, brand):
    #     return CarSerializers(brand.cars, many=True).data


class CarSerializers(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = (
            'name',
            'brend',
        )



class CarImageSerializers(serializers.ModelSerializer):
    car = serializers.CharField()
    small = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)
    medium = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)
    large = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)

    class Meta:
        model = CarImage
        fields = ('image', 'video', 'car', 'small', 'medium', 'large')




            # 'description',
            # 'color',
            # 'country',
            # 'year',
            # 'type_body',
            # 'number_place',
            # 'number_door',
            # 'power_motor',
            # 'power_battery',
            # 'power_reserve',
            # 'max_speed',
            # 'acceleration',
            # 'length',
            # 'width',
            # 'height',
            # 'images'
        # )

    # def get_images(self, obj):
    #     return CarImageSerializers(obj.car_images, many=True).data

