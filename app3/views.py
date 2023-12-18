from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import usuarioExtendido, almacenSistema, productoSistema, cotizacionSistema, productoAsociadoCoti
import json

# Create your views here.
def index(request):
    if request.method == 'POST':
        nombreUsuario = request.POST.get('nombreUsuario')
        contraUsuario = request.POST.get('contraUsuario')
        usuarioInfo = authenticate(request,username=nombreUsuario,password=contraUsuario)
        if usuarioInfo is not None:
            login(request,usuarioInfo)
            return HttpResponseRedirect(reverse('app3:consolaInicio'))
        else:
            return HttpResponseRedirect(reverse('app3:index'))
    return render(request,'ingresoUsuario.html')

@login_required(login_url='/')
def consolaInicio(request):
    if request.method == 'POST':
        nuevoUsername = request.POST.get('nuevoUsername')
        nuevoPassword = request.POST.get('nuevoPassword')
        nuevoNombre = request.POST.get('nuevoNombre')
        nuevoApellido = request.POST.get('nuevoApellido')
        nuevoEmail = request.POST.get('nuevoEmail')
        rolUsuario = request.POST.get('rolUsuario')
        nuevoUsuario = User.objects.create(
            username=nuevoUsername,
            email=nuevoEmail
        )
        nuevoUsuario.set_password(nuevoPassword)
        nuevoUsuario.first_name = nuevoNombre
        nuevoUsuario.last_name = nuevoApellido
        nuevoUsuario.is_staff = True
        nuevoUsuario.save()

        nuevoCodigo = str(nuevoUsuario.id)
        while len(nuevoCodigo) < 4:
            nuevoCodigo = '0' + nuevoCodigo
        nuevoCodigo = 'USR-' + nuevoCodigo
        usuarioExtendido.objects.create(
            usuarioAsociado=nuevoUsuario,
            codigoUsuario=nuevoCodigo,
            rolUsuario=rolUsuario,
        )
        return HttpResponseRedirect(reverse('app3:consolaInicio'))
    return render(request,'opcionesConsola.html',{
        'usuariosTotales':User.objects.all().order_by('id'),
        'almacenesTotales':almacenSistema.objects.all().order_by('id')
    })

@login_required(login_url='/')
def almacenes(request):
    if request.method == 'POST':
        nombreAlmacen = request.POST.get('nombreAlmacen')
        codigoAlmacen = request.POST.get('codigoAlmacen')
        direccionAlmacen = request.POST.get('direccionAlmacen')
        almacenSistema.objects.create(
            nombreAlmacen=nombreAlmacen,
            codigoAlmacen=codigoAlmacen,
            direccionAlmacen=direccionAlmacen
        )
        return HttpResponseRedirect(reverse('app3:almacenes'))
    return render(request,'almacenes.html',{
        'listaAlmacenes':almacenSistema.objects.all().order_by('id')
    })

@login_required(login_url='/')
def productos(request):
    if request.method == 'POST':
        nombreProducto = request.POST.get('nombreProducto')
        codigoProducto = request.POST.get('codigoProducto')
        precioProducto = request.POST.get('precioProducto')
        cantidadProducto = request.POST.get('cantidadProducto')
        pesoProducto = request.POST.get('pesoProducto')
        almacenProducto = request.POST.get('almacenProducto')
        almacenObj = almacenSistema.objects.get(id=almacenProducto)
        productoSistema.objects.create(
            nombreProducto=nombreProducto,
            codigoProducto=codigoProducto,
            precioProducto=precioProducto,
            cantidadProducto=cantidadProducto,
            pesoProducto=pesoProducto,
            almacenProducto=almacenObj,
        )
        return HttpResponseRedirect(reverse('app3:productos'))
    return render(request,'productos.html',{
        'almacenesTotales':almacenSistema.objects.all().order_by('id'),
        'productosTotales':productoSistema.objects.all().order_by('id')
    })

@login_required(login_url='/')
def eliminarUsuario(request,idUsuario):
    objUsuario = User.objects.get(id=idUsuario)
    objUsuarioExtendido = usuarioExtendido.objects.get(usuarioAsociado=objUsuario)
    objUsuarioExtendido.delete()
    objUsuario.delete()
    return HttpResponseRedirect(reverse('app3:consolaInicio'))

@login_required(login_url='/')
def eliminarAlmacen(request,idAlmacen):
    objAlmacen = almacenSistema.objects.get(id=idAlmacen)
    objAlmacen.delete()
    return HttpResponseRedirect(reverse('app3:almacenes'))

@login_required(login_url='/')
def asignarAlmacen(request):
    if request.method == 'POST':
        idUsuario = request.POST.get('usuarioSeleccionado')
        idAlmacen = request.POST.get('almacenSeleccionado')
        objUsuario = User.objects.get(id=idUsuario)
        objAlmacen = almacenSistema.objects.get(id=idAlmacen)
        objUsuarioExtendido = usuarioExtendido.objects.get(usuarioAsociado=objUsuario)
        objUsuarioExtendido.almacenUsuario = objAlmacen
        objUsuarioExtendido.save()
        return HttpResponseRedirect(reverse('app3:consolaInicio'))

@login_required(login_url='/')
def cerrarSesion(request):
    logout(request)
    return HttpResponseRedirect(reverse('app3:index'))

def ejemploJavascript(request):
    return render(request,'ejemploJavascript.html')

def consultaAlmacen(request,idAlmacen):
    objAlmacen = almacenSistema.objects.get(id=idAlmacen)
    usuariosRelacionados = objAlmacen.usuarioextendido_set.all()
    lista_usuarios = []
    for usuarioInfo in usuariosRelacionados:
        lista_usuarios.append([
            usuarioInfo.usuarioAsociado.first_name,
            usuarioInfo.usuarioAsociado.last_name,
            usuarioInfo.codigoUsuario
        ])
    print(usuariosRelacionados)
    return JsonResponse({
        'nombreAlmacen':objAlmacen.nombreAlmacen,
        'codigoAlmacen':objAlmacen.codigoAlmacen,
        'lista_usuarios':lista_usuarios
    })

def consultaUsuario(request,idUsuario):
    usuarioObj = User.objects.get(id=idUsuario)
    return JsonResponse({
        'idUsuario':usuarioObj.id,
        'usernameUsuario':usuarioObj.username,
        'nombreUsuario':usuarioObj.first_name,
        'apellidoUsuario':usuarioObj.last_name,
        'emailUsuario':usuarioObj.email,
        'rolUsuario':usuarioObj.usuarioextendido.rolUsuario,
    })

def actualizarUsuario(request):
    if request.method == 'POST':
        editarId = request.POST.get('editarId')
        editarNombre = request.POST.get('editarNombre')
        editarApellido = request.POST.get('editarApellido')
        editarEmail = request.POST.get('editarEmail')

        usuarioObj = User.objects.get(id=editarId)
        usuarioObj.first_name = editarNombre
        usuarioObj.last_name = editarApellido
        usuarioObj.email = editarEmail
        usuarioObj.save()
        return HttpResponseRedirect(reverse('app3:consolaInicio'))

def react(request):
    return render(request,'react.html')


def cotizaciones(request):
    return render(request,'cotizaciones.html',{
        'cotizacionesTotales':cotizacionSistema.objects.all().order_by('id')
    })

def consultarProductos(request):
    listaProductos = []
    productosTotales = productoSistema.objects.all().order_by('id')
    for productoInfo in productosTotales:
        listaProductos.append([
            str(productoInfo.id),
            productoInfo.nombreProducto,
            productoInfo.codigoProducto,
            productoInfo.precioProducto
        ])
    return JsonResponse({
        'listaProductos':listaProductos,
    })

def crearCotizacion(request):
    if request.method == 'POST':
        datos = json.load(request)
        documentoCliente = datos.get('documentoCliente')
        nombreCliente = datos.get('nombreCliente')
        productosCoti = datos.get('productosCoti')
        cotiCreada = cotizacionSistema.objects.create(
            nombreCliente=nombreCliente,
            documentoCliente=documentoCliente
        )
        for productoSeleccionado in productosCoti:
            productoObj = productoSistema.objects.get(id=productoSeleccionado['id'])
            productoAsociadoCoti.objects.create(
                cantidadProductoCoti=productoSeleccionado['cantidad'],
                precioProductoCoti=productoSeleccionado['precio'],
                cotizacionAsociada=cotiCreada,
                productoAsociado=productoObj
            )
        return JsonResponse({
            'resp':'ok'
        })
    return render(request,'crearCotizacion.html',)