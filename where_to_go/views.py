from django.shortcuts import render
from places.models import Places

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
