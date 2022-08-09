from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

def 함수(request):
    return HttpResponse("Hello~~~~")

def json(request):
    data={
        'name' : 'hong','age':30,
        'address': 'busan'
    }
    return JsonResponse(data)