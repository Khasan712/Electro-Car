from django.shortcuts import render, redirect

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.conf import settings
from django.contrib.auth.models import User

from .models import (
    Header,
    Post
)
from .serializers import (
    HeaderSerializers,
    PostSerializers
)


# For Header "POST"
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


# For Header "GET"
@api_view(['GET',])
def get_header(request, pk):
    try:
        header = Header.objects.get(id=pk)
    except Header.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = HeaderSerializers(header)
        return Response(serializer.data)

# For Header "DELETE"
@api_view(['DELETE',])
def delete_header(request, pk):
    try:
        header = Header.objects.get(id=pk)
    except Header.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "DELETE":
        header.delete()
        return Response({"data":"deleted"}, status=status.HTTP_204_NO_CONTENT)

# =============================================================================


# For Post "POST"
@api_view(['POST',])
def create_post(request):
    serializer = PostSerializers(request.POST or request.FILES)
    author = User.objects.all()[0]
    if request.method == 'POST':
        serializer = PostSerializers(author, data=request.data)
        print("1")
        if serializer.is_valid():
            print(serializer.data)
            serializer.save(author)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        data = {}
        data["False"] = "Wrong"
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)


# For Post "GET"
@api_view(['GET',])
def get_post(request, pk):
    try:
        post = Post.objects.get(id=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = PostSerializers(post)
        return Response(serializer.data)

# For Post "DELETE"
@api_view(['DELETE',])
def delete_post(request, pk):
    try:
        post = Post.objects.get(id=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "DELETE":
        post.delete()
        return Response({"data":"deleted"}, status=status.HTTP_204_NO_CONTENT)



        
