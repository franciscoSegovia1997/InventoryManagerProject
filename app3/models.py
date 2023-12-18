from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class almacenSistema(models.Model):
    nombreAlmacen = models.CharField(max_length=32, blank=True, null=True)
    codigoAlmacen = models.CharField(max_length=32, blank=True, null=True)
    direccionAlmacen = models.CharField(max_length=32, blank=True, null=True)

class usuarioExtendido(models.Model):
    usuarioAsociado = models.OneToOneField(User, on_delete=models.CASCADE)
    codigoUsuario = models.CharField(max_length=32, blank=True, null=True)
    rolUsuario = models.CharField(max_length=32, blank=True, null=True)
    almacenUsuario = models.ForeignKey(almacenSistema,on_delete=models.SET_NULL, blank=True, null=True)

class productoSistema(models.Model):
    nombreProducto = models.CharField(max_length=64, blank=True, null=True)
    codigoProducto = models.CharField(max_length=32, blank=True, null=True)
    precioProducto = models.CharField(max_length=16, blank=True, null=True)
    cantidadProducto = models.CharField(max_length=16, blank=True, null=True)
    pesoProducto = models.CharField(max_length=16, blank=True, null=True)
    almacenProducto = models.ForeignKey(almacenSistema,on_delete=models.CASCADE, blank=True, null=True)

class cotizacionSistema(models.Model):
    nombreCliente = models.CharField(max_length=64, blank=True, null=True)
    documentoCliente = models.CharField(max_length=64, blank=True, null=True)

class productoAsociadoCoti(models.Model):
    cantidadProductoCoti = models.CharField(max_length=16, blank=True, null=True)
    precioProductoCoti = models.CharField(max_length=16, blank=True, null=True)
    cotizacionAsociada = models.ForeignKey(cotizacionSistema, on_delete=models.CASCADE, blank=True, null=True)
    productoAsociado = models.ForeignKey(productoSistema, on_delete=models.SET_NULL,blank=True, null=True)

