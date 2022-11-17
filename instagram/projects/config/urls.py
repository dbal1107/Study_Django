from django.contrib import admin
from django.urls import path
from mtv.views import SUB

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", SUB.as_view()),
]
