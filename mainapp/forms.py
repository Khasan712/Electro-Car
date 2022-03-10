from django import forms
from .models import CarImage, Car


# class CarImageForm(forms.ModelForm):
#     file_field = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
#     class Meta:
#         model = CarImage
#         fields = ['name',]

class CarForm(forms.ModelForm):
    file_field = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    class Meta:
        model = Car
        fields = ['name',]