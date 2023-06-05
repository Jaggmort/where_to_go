from pathlib import Path

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from urllib.parse import urlparse

from places.models import Place, Image

class Command(BaseCommand):
    help = 'Добавить место на карту'

    def add_arguments(self, parser):
        parser.add_argument(
            'place_url',
            nargs='?',
            type=str,
            help='Добавить место на карту',
        )

    def handle(self, *args, **options):
        response = requests.get(options['place_url'])
        response.raise_for_status()
        prepared_place = response.json()
        lng = prepared_place['coordinates']['lng']
        lat = prepared_place['coordinates']['lat']

        place, place_created = Place.objects.get_or_create(
            title=prepared_place['title'],
            lng=lng,
            lat=lat,
            description_short=prepared_place['description_short'],
            description_long=prepared_place['description_long'],
        )

        if not place_created:
            print(f'Место "{prepared_place["title"]}" было добавленно ранее.')
            return
        print(f'Добавлено место "{prepared_place["title"]}".')

        for image_num, image_url in enumerate(prepared_place.get('imgs', [])):
            response = requests.get(image_url)
            response.raise_for_status()
            image_name = Path(urlparse(image_url).path).name
            image_file = ContentFile(response.content, name=image_name)
            image = Image.objects.create(
                image=image_file,
                place_id=place.id,
                sequence_number=image_num,
            )
            print(f'Добавлена фотография "{image.image}".')
