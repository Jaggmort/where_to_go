from django.db import models
from tinymce.models import HTMLField

class Places(models.Model):
    title = models.CharField('Заголовок', max_length=80)
    description_short = models.CharField('Короткое описание', max_length=400, blank=True)
    description_long = HTMLField('Длинное описание', blank=True)
    lng = models.FloatField('Долгота', blank=True)
    lat = models.FloatField('Широта', blank=True)

    class Meta:
        verbose_name = 'Интересное место'
        verbose_name_plural = 'Интересные места'

    def __str__(self):
        return f'{self.title}'

class Images(models.Model):
    place = models.ForeignKey(Places, on_delete=models.CASCADE, verbose_name='Интересное место', related_name='place_images')
    image = models.ImageField('Изображени', blank=True, null=True)
    sequence_number = models.PositiveIntegerField('Индекс в списке интересного места', default=0, blank=True, null=True)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        ordering = ['place']

    def __str__(self):
        return f'{self.place.pk} {self.place}'
