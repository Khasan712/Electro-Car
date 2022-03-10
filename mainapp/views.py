from django.shortcuts import redirect, render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import generics
# import requests

# Create your views here.
from .models import (
    CarImage,
    Color,
    Brend,
    Car,
)
from .forms import CarForm
from .serializers import (
    CarImageSerializers,
    ColorSerializers,
    BrendSerializers,
    CarSerializers
)

import json
from rest_framework.decorators import action

from mainapp import serializers



class CreateCarView(APIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializers

    def post(self, request):
        serializer = CarSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # def get(self, request, pk=None):
    #     get_car = self.get_object(pk)
    #     serializer = CarSerializers(get_car)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

# RetrieveUpdateDestroyAPIView

class CarRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Car.objects.all()
    serializer_class = CarSerializers







def index(request):
    if request.method == "POST":
        car_name = request.POST.get('name')
        images = request.FILES.getlist('images')
        car = Car.objects.create(name=car_name)
        for img in images:
            CarImage.objects.create(car=car, image=img)

    return render(request, 'index.html')


def car_detail(request, pk):
    car_url = 'http://127.0.0.1:8000/get/car/'
    # get_car = requests.get()
    return render(request, 'car-detail.com')


# For Image "POST"
@api_view(['POST',])
def create_image(request):
    serializer = CarImageSerializers(request.POST or request.FILES)
    if request.method == 'POST':
        serializer = CarImageSerializers(data=request.data)
        if serializer.is_valid():
            print(request.data)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        data = {}
        data["False"] = "Anything is wrong"
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

# For Image "GET"
@api_view(['GET',])
def get_image(request, pk):
    try:
        image = CarImage.objects.get(id=pk)
    except CarImage.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = CarImageSerializers(image)
        return Response(serializer.data)


# For Image "DELETE"
@api_view(['DELETE',])
def delete_image(request, pk):
    try:
        image = CarImage.objects.get(id=pk)
    except CarImage.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        image.delete()
        return Response({'message': "Deleted"},status=status.HTTP_204_NO_CONTENT)


# ------------------------------------------------------------------

# For Color "POST"
@api_view(['POST',])
def create_color(request):
    serializer = ColorSerializers(request.POST)
    if request.method == 'POST':
        serializer = ColorSerializers(data=request.data)
        if serializer.is_valid():
            print(request.data)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        data = {}
        data["False"] = "Anything is wrong"
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)



# For Color "GET"
@api_view(['GET',])
def get_color(request, pk):
    try:
        color = Color.objects.get(id=pk)
    except Color.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ColorSerializers(color)
        return Response(serializer.data)

# For Color "DELETE"
@api_view(['DELETE',])
def delete_color(request, pk):
    try:
        color = Color.objects.get(id=pk)
    except Color.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        color.delete()
        return Response({'message': "Deleted"},status=status.HTTP_204_NO_CONTENT)


# ----------------------------------------------------------------


# For Brend "POST"
@api_view(['POST',])
def create_brend(request):
    serializer = BrendSerializers(request.POST)
    if request.method == 'POST':
        serializer = BrendSerializers(data=request.data)
        if serializer.is_valid():
            print(request.data)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        data = {}
        data["False"] = "Anything is wrong"
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

# For Brend "GET"
@api_view(['GET',])
def get_brend(request, pk):
    try:
        brend = Brend.objects.get(id=pk)
    except Brend.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = BrendSerializers(brend)
        return Response(serializer.data)

# For Brend "DELETE"
@api_view(['DELETE',])
def delete_brend(request, pk):
    try:
        brend = Brend.objects.get(id=pk)
    except Brend.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        brend.delete()
        return Response({'message': "Deleted"},status=status.HTTP_204_NO_CONTENT)

# ----------------------------------------------------------------











# For Car "POST"
@api_view(['POST',])
def create_car(request):
    serializer = CarSerializers(data=request.data)
    if request.method == 'POST':
        serializer = CarSerializers(data=request.data)
        data = {}
        if serializer.is_valid():
            car = serializer.save()
            data['name'] = car.name
            car_brend = request.POST.get('brend')
            brend = Brend.objects.get(name=car_brend)
            print(brend)
            # data['brend'] = brend
            return Response(data, status=status.HTTP_201_CREATED)
        data = {}
        data["False"] = "Anything is wrong"
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)















# For Car "GET"
@api_view(['GET',])
def get_car(request, pk):
    try:
        car = Car.objects.get(id=pk)
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = CarSerializers(car)
        return Response(serializer.data)

# For Car "DELETE"
@api_view(['DELETE',])
def delete_car(request, pk):
    try:
        car = Car.objects.get(id=pk)
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        car.delete()
        return Response({'message': "Deleted"},status=status.HTTP_204_NO_CONTENT)

# ----------------------------------------------------------------






