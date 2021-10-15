from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from admin.crime.model import Crime
from admin.crime.models_old import CrimeCctvModel


@api_view(['GET'])
@parser_classes([JSONParser])
def create_crime_model(request):
    CrimeCctvModel().create_crime_model()
    return JsonResponse({'result':'Create Crime Model Success'})

@api_view(['GET'])
@parser_classes([JSONParser])
def create_police_position(request):
    CrimeCctvModel().create_police_position()
    return JsonResponse({'result':'Create Police Position Success'})

@api_view(['GET'])
@parser_classes([JSONParser])
def create_cctv_model(request):
    CrimeCctvModel().create_cctv_model()
    return JsonResponse({'result':'Create CCTV Model Success'})

@api_view(['GET'])
@parser_classes([JSONParser])
def create_population_model(request):
    CrimeCctvModel().create_population_model()
    return JsonResponse({'result':'Create Population Model Success'})

@api_view(['GET'])
@parser_classes([JSONParser])
def merge_cctv_pop(request):
    CrimeCctvModel().merge_cctv_pop()
    return JsonResponse({'result':'Create Population Model Success'})

@api_view(['GET'])
@parser_classes([JSONParser])
def sum_crime(request):
    CrimeCctvModel().sum_crime()
    return JsonResponse({'result':'Sum Crime Success'})

@api_view(['GET'])
@parser_classes([JSONParser])
def merge_cctv_crime(request):
    CrimeCctvModel().merge_cctv_crime()
    return JsonResponse({'result':'Merge Cctv Crime Success'})

@api_view(['GET'])
@parser_classes([JSONParser])
def process(request):
    Crime().process()
    return JsonResponse({'result': 'Process Success'})