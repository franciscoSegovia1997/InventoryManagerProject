from django.db import models

# Create your models here.
class estudianteInfo(models.Model):
    nombreEstudiante = models.CharField(max_length=32, blank=True, null=True)
    apellidoEstudiante = models.CharField(max_length=32, blank=True, null=True)

class datosContacto(models.Model):
    numeroCelular = models.CharField(max_length=32, blank=True, null=True)
    emailEstudiante = models.CharField(max_length=32, blank=True, null=True)
    estudianteRelacionado = models.ForeignKey(estudianteInfo,blank=True,null=True,on_delete=models.SET_NULL)