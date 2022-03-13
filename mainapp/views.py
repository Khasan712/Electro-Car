from django.shortcuts import redirect, render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import generics
from django.db.models import F, Q
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

class CarRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializers




class CreateColor(generics.ListCreateAPIView):
    queryset = Brend.objects.all()
    serializer_class =  BrendSerializers


class BrendReUpDel(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brend.objects.all()
    serializer_class = BrendSerializers
    
