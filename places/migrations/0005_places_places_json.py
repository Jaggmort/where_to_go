# Generated by Django 4.2 on 2023-06-02 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='places',
            name='places_json',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Расшоложение json-файла'),
        ),
    ]
