from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from admin.crime.models import CrimeCctvModel


@api_view(['GET'])
@parser_classes([JSONParser])
def create_crime_model(request):
    CrimeCctvModel().create_crime_model()
    return JsonResponse({'result':'Create Crime Model Success'})

def create_police_position(request):
    CrimeCctvModel().create_police_position()
    return JsonResponse({'result':'Create Police Position Success'})