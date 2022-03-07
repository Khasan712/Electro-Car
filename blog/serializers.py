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
    author = serializers.CharField()
    class Meta:
        model = Post
        fields = ("author", "image", 'description', 'title')