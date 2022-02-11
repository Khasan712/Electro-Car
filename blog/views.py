from django.shortcuts import render, redirect

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import (
    Header,
    Post
)
from .serializers import (
    HeaderSerializers,
    PostSerializers
)

@api_view(['POST',])
def create_header(request):
    serializer = HeaderSerializers(request.POST or request.FILES)
    if request.method == 'POST':
        serializer = HeaderSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        data = {}
        data["False"] = "Wrong"
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
