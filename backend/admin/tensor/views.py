from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from admin.tensor.models import Calculator, FashionClassification, TensorFunction


@api_view(['GET'])
@parser_classes([JSONParser])
def calculator(request):
    Calculator().process()
    return JsonResponse({'connection': 'Calculator Plus SUCCESS'})

@api_view(['GET'])
@parser_classes([JSONParser])
def fashion(request):
    FashionClassification().fashion()
    return JsonResponse({'connection': 'Fashion Classification SUCCESS'})

@api_view(['GET'])
@parser_classes([JSONParser])
def tensorFunction(request):
    TensorFunction().hook()
    return JsonResponse({'connection': 'Tensor Function Hook SUCCESS'})


from django.shortcuts import render

# Create your views here.
