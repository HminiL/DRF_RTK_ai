from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from admin.iris.models import Iris


@api_view(['GET'])
@parser_classes([JSONParser])
def iris(request):
    Iris().base()
    return JsonResponse({'connection': 'Iris SUCCESS'})

@api_view(['GET'])
@parser_classes([JSONParser])
def advanced(request):
    Iris().advanced()
    return JsonResponse({'connection' : 'Iris Advenced SUCCESS'})

@api_view(['GET'])
@parser_classes([JSONParser])
def iris_by_tf(request):
    Iris().iris_by_tf()
    return JsonResponse({'connection' : 'Iris By Tf SUCCESS'})
