from django.contrib import admin
from django.utils.html import format_html

from adminsortable2.admin import SortableAdminBase, SortableStackedInline

from .models import Place, Image


class ImageStackedInline(SortableStackedInline):
    model = Image
    fields = ('image', 'preview_image')
    readonly_fields = ('preview_image', )
    extra = 0

    def preview_image(self, image):
        return format_html(
            '<img src="{}" height="200px"/>',
            image.image.url
        )


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ['title', 'lng', 'lat']

    inlines = [
        ImageStackedInline,
    ]


admin.site.site_header = 'Панель управления'
admin.site.site_title = '"Афиша"'
