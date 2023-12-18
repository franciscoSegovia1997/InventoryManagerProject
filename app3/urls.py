from django.urls import path
from . import views

app_name = 'app3'

urlpatterns = [
    path('',views.index,name='index'),
    path('consolaInicio',views.consolaInicio,name='consolaInicio'),
    path('cerrarSesion',views.cerrarSesion,name='cerrarSesion'),
    path('almacenes',views.almacenes,name='almacenes'),
    path('productos',views.productos,name='productos'),
    path('eliminarUsuario/<str:idUsuario>',views.eliminarUsuario,name='eliminarUsuario'),
    path('eliminarAlmacen/<str:idAlmacen>',views.eliminarAlmacen,name='eliminarAlmacen'),
    path('asignarAlmacen',views.asignarAlmacen,name='asignarAlmacen'),
    path('ejemploJavascript',views.ejemploJavascript,name='ejemploJavascript'),
    path('consultaAlmacen/<str:idAlmacen>',views.consultaAlmacen,name='consultaAlmacen'),
    path('consultaUsuario/<str:idUsuario>',views.consultaUsuario,name='consultaUsuario'),
    path('actualizarUsuario',views.actualizarUsuario,name='actualizarUsuario'),
    path('react',views.react,name='react'),
    path('cotizaciones',views.cotizaciones,name='cotizaciones'),
    path('crearCotizacion',views.crearCotizacion,name='crearCotizacion'),
    path('consultarProductos',views.consultarProductos,name='consultarProductos')
]