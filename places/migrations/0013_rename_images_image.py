# Generated by Django 4.2.1 on 2023-06-04 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0012_alter_places_options_remove_places_sequence_number_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Images',
            new_name='Image',
        ),
    ]
