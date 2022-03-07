from django.urls import path
from . import views


urlpatterns = [
    path('create/header', views.create_header, name='create_header'),
    path('get/header', views.get_header, name='get_header'),
    path('delete/header', views.delete_header, name='delete_header'),
    path('create/post', views.create_post, name='create_post'),
    path('get/post', views.get_post, name='get_post'),
    path('delete/post', views.delete_post, name='delete_post'),
]
