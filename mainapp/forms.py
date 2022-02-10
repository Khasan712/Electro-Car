from django.forms import ModelForm
from .models import PostImage


class PostImageForm(ModelForm):
    class Meta:
        model = PostImage
        fields = '__all__'