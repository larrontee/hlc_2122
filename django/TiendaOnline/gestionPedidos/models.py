from django.db import models

# Create your models here.
from django.db import models
# Create your models here.


class Clientes(models.Model):
    nombre: nombre = models.CharField(max_length=50)
    direccion: direccion = models.CharField(max_length=50)
    email: email = models.CharField(max_length=50)
    telefono: telefono = models.CharField(max_length=50)

    def __str__(self):
        return "nombre" + self.nombre + "direccion " + self.direccion + "email"+self.email + "telefono"+self.telefono


class Articulos(models.Model):
    nombre: nombre = models.CharField(max_length=50)
    seccion: seccion = models.CharField(max_length=50)
    telefono: telefono = models.CharField(max_length=50)

    def __str__(self):
        return "nombre" + self.nombre + "seccion" + self.seccion + "telefono"+self.telefono


class Pedidos(models.Model):
    numero: numero = models.CharField(max_length=50)
    fecha: fecha = models.CharField(max_length=50)
    entregado: entregado = models.CharField(max_length=50)

    def __str__(self):
        return "Num" + self.numero + "fecha" + self.fecha + "entregado"+self.entregado
