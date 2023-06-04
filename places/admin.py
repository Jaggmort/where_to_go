from django.contrib import admin
from django.utils.html import format_html

from adminsortable2.admin import SortableTabularInline, SortableAdminBase, SortableStackedInline

from .models import Places, Image


class ImageStackedInline(SortableStackedInline):
    model = Image
    fields = ('image', 'pl_image')
    readonly_fields = ('pl_image', )
    extra = 0

    def pl_image(self, image_object):
        return format_html(
            '<img src="{}" height="200px" width="200px" />',
            image_object.image.url
        )


@admin.register(Places)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ['title', 'lng', 'lat']

    inlines = [
        ImageStackedInline,
    ]


admin.site.site_header = 'Панель управления'
admin.site.site_title = '"Афиша"'