from rest_framework import serializers
from .models import (
    Header,
    Post
)


class HeaderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Header
        fields = ("video", 'image', 'title', 'content')

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("image", 'description', 'title')