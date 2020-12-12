from datetime import timezone

from django.contrib.auth.decorators import login_required
from django.contrib.gis.geos import Point
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from opencage.geocoder import OpenCageGeocode

from users.models import Profile

locations = [
    {
        'author': 'CoreyMS',
        'title': 'location 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'location 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]


@login_required()
def home(request):
    context = {
        'locations': locations
    }
    return render(request, 'world/home.html', context)

def geocode(request):
    try:
        with open('OpenCageAPI.txt') as o:
            apikey = o.read().strip()
        search = request.POST["search"]
        geocoder = OpenCageGeocode(apikey)

        results = geocoder.geocode(search)

        if len(results) > 0:
            formatted_response = results[0]["geometry"]
            return JsonResponse(formatted_response, status=200)
        else:
            response = {"location": "not found"}
            return JsonResponse(response, status=200)
    except Exception as e:
        return JsonResponse({"message": str(e)}, status=400)
