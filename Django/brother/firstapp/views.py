from django.http import HttpResponse

def index1 (request):
    return HttpResponse("<h1> response </h1>")