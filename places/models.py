from django.db import models

class Places(models.Model):
    title = models.CharField('Заголовок', max_length=80)
    description_short = models.CharField('Короткое описание', max_length=400, blank=True)
    description_long = models.TextField('Длинное описание', blank=True)
    lng = models.FloatField('Долгота', blank=True)
    lat = models.FloatField('Широта', blank=True)

    class Meta:
        verbose_name = 'Интересное место'
        verbose_name_plural = 'Интересные места'

    def __str__(self):
        return f'{self.title}'