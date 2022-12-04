from django.contrib import admin
from django.urls import path

from football.views import contato, home, sobre

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('contato/', contato),
    path('sobre/', sobre)
]
