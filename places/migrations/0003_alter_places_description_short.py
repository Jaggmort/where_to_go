# Generated by Django 4.2 on 2023-06-01 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_alter_places_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='places',
            name='description_short',
            field=models.CharField(blank=True, max_length=400, verbose_name='Короткое описание'),
        ),
    ]