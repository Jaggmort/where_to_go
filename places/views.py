from django.shortcuts import render
from places.models import Place
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.urls import reverse


def show_places(request):
    places = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.lng, place.lat]
                },
                "properties": {
                    "title": place.title,
                    "placeId": place.pk,
                    "detailsUrl": reverse('place_view', args=[place.id])
                }
            } for place in Place.objects.all()
        ]
    }
    return render(request, 'index.html', {'places': places})


def place_view(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    place_parameters = {
        'title': place.title,
        'imgs': [image.image.url for image in place.images.all()],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordingates': {
            'lat': place.lat,
            'lng': place.lng
        }

    }
    return JsonResponse(place_parameters, json_dumps_params={
        'indent': 2,
        'ensure_ascii': False
      })
