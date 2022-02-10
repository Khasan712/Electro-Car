from django.shortcuts import redirect, render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
from .models import PostImage
from .forms import PostImageForm
from .serializers import PostImageSerializers

def index(request):
    image = PostImage.objects.all()
    form = PostImageForm(request.POST and request.FILES)
    if request.method == 'POST':
        form = PostImageForm(request.POST and request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'image':image,
        'form':form
    }
    return render(request, 'index.html', context)


@api_view(['POST',])
def create_image(request):
    serializer = PostImageSerializers(request.POST or request.FILES)
    if request.method == 'POST':
        serializer = PostImageSerializers(data=request.data)
        if serializer.is_valid():
            print(request.data)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        data = {}
        data["False"] = "Anything is wrong"
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET',])
def get_image(request, pk):
    try:
        contact = PostImage.objects.get(id=pk)
    except PostImage.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = PostImageSerializers(contact)
        return Response(serializer.data)


