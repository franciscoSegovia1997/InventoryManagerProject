from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Bienvenidos a django")

def ejemplo(request):
    return HttpResponse("Bienvenidos a la pucp")

# Ruta : 127.0.0.1:8000/app1
# Ruta : 127.0.0.1:8000/app1/ejemplo