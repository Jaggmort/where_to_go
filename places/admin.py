from django.contrib import admin

from .models import Places, Images

@admin.register(Places)
class PlacesAdmin(admin.ModelAdmin):
    list_display = ['title', 'lng', 'lat']


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['__str__']