from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_image, name='create_image'),
    path('get/<int:pk>/', views.get_image, name='get_image'),
]
