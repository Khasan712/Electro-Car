from django.urls import path, include
from . import views
# from .router import router

urlpatterns = [
    path('create/car/', views.CreateCarView.as_view(), name='create_car'),
    path('get/car/<int:pk>/', views.CarRetrieveUpdateDestroyAPIView.as_view(), name='get_car'),
]
