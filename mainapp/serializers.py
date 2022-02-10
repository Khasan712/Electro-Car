from dataclasses import fields
from rest_framework.serializers import ModelSerializer

from .models import PostImage


class PostImageSerializers(ModelSerializer):
    class Meta:
        model = PostImage
        fields = ('image',)

    # def save(self, **kwargs):

    #     return super().save(**kwargs)