from django.contrib import admin

# Register your models here.
from .models import Header, Post

@admin.register(Header)
class HeaderAdmin(admin.ModelAdmin):
    list_display = ['id']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id']