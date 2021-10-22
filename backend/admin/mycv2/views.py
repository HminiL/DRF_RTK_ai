from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from admin.mycv2.models import MyCV2


@api_view(['GET'])
@parser_classes([JSONParser])
def lena(request):
    MyCV2().lena()
    return JsonResponse({'connection': 'Mycv2 SUCCESS'})


@api_view(['GET'])
@parser_classes([JSONParser])
def girl(request):
    MyCV2().girl()
    return JsonResponse({'connection': 'Girl SUCCESS'})

@api_view(['GET'])
@parser_classes([JSONParser])
def face_detect(request):
    MyCV2().face_detect()
    return JsonResponse({'connection': 'Girl SUCCESS'})

@api_view(['GET'])
@parser_classes([JSONParser])
def cat_mosaic(request):
    MyCV2().cat_mosaic()
    return JsonResponse({'connection': 'Cat Mosaic SUCCESS'})

@api_view(['GET'])
@parser_classes([JSONParser])
def face_detect_mosaic(request):
    MyCV2().face_detect_mosaic()
    return JsonResponse({'connection': 'Face Detect Mosaic SUCCESS'})



