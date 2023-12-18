from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import estudianteInfo

# Create your views here.
def index(request):
    return HttpResponse("Bienvenidos a la aplicacion 2")

def inicio(request):
    return render(request,'inicio.html',{
        'lista_usuarios':estudianteInfo.objects.all()
    })

def ingresoUsuario(request):
    if request.method == 'POST':
        nombreUsuario = request.POST.get('nombreUsuario')
        apellidoUsuario = request.POST.get('apellidoUsuario')
        print(nombreUsuario)
        print(apellidoUsuario)
        estudianteInfo.objects.create(
            nombreEstudiante=nombreUsuario,
            apellidoEstudiante=apellidoUsuario
        )
        return HttpResponseRedirect(reverse('app2:inicio'))
    return HttpResponse("Los datos han sido recibidos")

def mostrarDatos(request,idEstudiante):
    objEstudiante = estudianteInfo.objects.get(id=idEstudiante)
    datos_estudiante = objEstudiante.datoscontacto_set.all()
    return render(request,'datosEstudiante.html',{
        'objEstudiante':objEstudiante,
        'datos_estudiante':datos_estudiante
    })