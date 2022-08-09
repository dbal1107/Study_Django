from django.http import HttpResponse, JsonResponse 

def 함수(request): 
	return HttpResponse("<h1><u>Hello~~~~</u></h1>")

def json(request):
    data={
        'name' : 'hong', 'age':30, 'address':'busan'
    }
    return JsonResponse(data)