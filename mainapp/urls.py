from django.urls import path, include
from . import views
# from .router import router

urlpatterns = [
    path('', views.index, name='index'),
    path('create/image/', views.create_image, name='create_image'),
    path('get/image/<int:pk>/', views.get_image, name='get_image'),
    path('delete/image/<int:pk>/', views.delete_image, name='delete_image'),


    path('create/color/', views.create_color, name='create_color'),
    path('get/color/<int:pk>/', views.get_color, name='get_color'),
    path('delete/color/<int:pk>/', views.delete_color, name='delete_color'),


    path('create/brend/', views.create_brend, name='create_brend'),
    path('get/brend/<int:pk>/', views.get_brend, name='get_brend'),
    path('delete/brend/<int:pk>/', views.delete_brend, name='delete_brend'),


    path('create/car/', views.CreateCarView.as_view(), name='create_car'),
    path('get/car/<int:pk>/', views.CarRetrieveUpdateDestroyAPIView.as_view(), name='get_car'),
    path('delete/car/<int:pk>/', views.delete_car, name='delete_car'),
    # path('create/car/view', include(router.urls))
]
