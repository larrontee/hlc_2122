from django.db import models

# Create your models here.


class Tarea(models.Model):
    user_id = models.IntegerField(blank=False, null=False, default=-1)
    fecha = models.DateField(blank=False, null=False)
    horas = models.DecimalField(max_digits=4, decimal_places=2)
    descripcion = models.CharField(max_length=250, blank=False, null=False)

    def __str__(self):
        return "id_user {}".format(self.user_id)
