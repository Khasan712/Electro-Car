from django.forms import ModelForm
from .models import CarImage


class CarImageForm(ModelForm):
    class Meta:
        model = CarImage
        fields = '__all__'