from django.contrib import admin
from .models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'img', 'category')
    search_fields = ('name', 'category')
