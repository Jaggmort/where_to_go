from django.contrib import admin
from .models import Places, Images
from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableTabularInline, SortableAdminBase

class BookTabularInline(SortableTabularInline):
    model = Images
    fields = ('image', 'pl_image', 'sequence_number')
    readonly_fields = ('pl_image', )
    extra = 0

    def pl_image(self, image_object):
        return format_html('<img src="{}" height="200px" width="200px" />', image_object.image.url)

@admin.register(Places)
class PlacesAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ['title', 'lng', 'lat']

    inlines = [
        BookTabularInline,
    ]



@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['place', 'sequence_number']

admin.site.site_header = 'Панель управления'
admin.site.site_title = '"Афиша"'
    