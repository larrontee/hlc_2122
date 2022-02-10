from django.db import models


class Clientes(models.Model):
    nombre = models.CharField(
        max_length=50, verbose_name='Nombre completo del cliente')
    direccion = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=50)
    telefono = models.CharField(max_length=7)

    def __str__(self):
        return 'Cliente: {} '.format(self.nombre,)





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
