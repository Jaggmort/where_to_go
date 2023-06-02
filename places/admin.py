from django.contrib import admin
from .models import Places, Images
from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

class BookInline(admin.TabularInline):
    model = Images
    fields = ['image', 'pl_image', 'sequence_number']
    readonly_fields = ('pl_image', )

    def pl_image(self, image_object):
        return format_html('<img src="{}" height="200px" width="200px" />', image_object.image.url)

@admin.register(Places)
class PlacesAdmin(admin.ModelAdmin):
    list_display = ['title', 'lng', 'lat']

    inlines = [
        BookInline,
    ]



@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['__str__']