from django.urls import path
from . import views

app_name = 'app2'

urlpatterns = [
    path('',views.index,name='index'),
    path('inicio',views.inicio,name='inicio'),
    path('ingresoUsuario',views.ingresoUsuario,name='ingresoUsuario'),
    path('mostrarDatos/<str:idEstudiante>',views.mostrarDatos,name='mostrarDatos')
]