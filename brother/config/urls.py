from django.contrib import admin
from django.urls import include, path
from firstapp import views as fview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index1/',fview.index1),
    path('first/',include('firstapp.urls'))
]
