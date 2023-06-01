from django.contrib import admin

from .models import Places

@admin.register(Places)
class PlacesAdmin(admin.ModelAdmin):
    list_display = ['title', 'lng', 'lat']