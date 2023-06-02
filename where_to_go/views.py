from django.shortcuts import render
from places.models import Places
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

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
            "detailsUrl": place.places_json
          }
        } for place in Places.objects.all()
      ]
    }
    return render(request, 'index.html', {'places': places})

def place_view(request, place_id):
    place = get_object_or_404(Places, pk=place_id)
    return HttpResponse(place)