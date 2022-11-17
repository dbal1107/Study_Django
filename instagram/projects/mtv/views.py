from django.shortcuts import render
from rest_framework.views import APIView

class SUB(APIView):
    def get(self, request):
        print('GET으로 호출')
        return render(request, "main.html")
    
    def post(self, request):
        print('POST로 호출')
        return render(request, 'main.html')