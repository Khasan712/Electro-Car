from email import message
from django.shortcuts import redirect, render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
from .models import (
    CarImage,
    Color,
    Brend,
    Car,
)
from .forms import CarImageForm
from .serializers import (
    CarImageSerializers,
    ColorSerializers,
    BrendSerializers,
    CarSerializers
)

def index(request):
    image = CarImage.objects.all()
    form = CarImageForm(request.POST and request.FILES)
    if request.method == 'POST':
        form = CarImageForm(request.POST and request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'image':image,
        'form':form
    }
    return render(request, 'index.html', context)

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
    serializer = CarSerializers(request.POST)
    if request.method == 'POST':
        serializer = CarSerializers(data=request.data)
        if serializer.is_valid():
            print(request.data)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
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






