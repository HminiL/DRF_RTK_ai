from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.parsers import JSONParser
from admin.MyNLP.models import MyImdb, NaverMovie


@api_view(['GET'])
@parser_classes([JSONParser])
def imdb_process(request):
    MyImdb().process()
    return JsonResponse({'connection': 'IMDB SUCCESS'})

@api_view(['GET'])
@parser_classes([JSONParser])
def web_scraping(request):
    NaverMovie().web_scraping()
    return JsonResponse({'connection': 'Naver Movie SUCCESS'})

@api_view(['GET'])
@parser_classes([JSONParser])
def naver_process(request):
    NaverMovie().model_fit()
    return JsonResponse({'connection': 'Naver Process SUCCESS'})
