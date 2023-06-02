from django.contrib import admin

from .models import Places, Images

class BookInline(admin.TabularInline):
    model = Images

@admin.register(Places)
class PlacesAdmin(admin.ModelAdmin):
    list_display = ['title', 'lng', 'lat']
    inlines = [
        BookInline,
    ]


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['__str__']