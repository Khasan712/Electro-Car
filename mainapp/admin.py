from django.contrib import admin

# Register your models here.
from .models import (
    CarImage,
    Color,
    Brend,
    Car
)

@admin.register(CarImage)
class CarImageAdmin(admin.ModelAdmin):
    list_display = ['id']

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ['id']

@admin.register(Brend)
class BrendAdmin(admin.ModelAdmin):
    list_display = ['id']

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['id']