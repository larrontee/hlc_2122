from django.shortcuts import render
from django.http.response import HttpResponse
import datetime

# Create your views here.


def saludo(request):
    persona = Persona("Chema", "Durán")
    temas_del_curso = ["Formularios", "Modelos", "Vistas", "Despliegue"]
    fecha_actual = datetime.datetime.now()
    return render(request, "saludo.html", {"nombre_persona": persona.nombre, "apellido_persona": persona.apellido, "fecha_actual": fecha_actual, "temas": temas_del_curso})


def despedida(request):
    return HttpResponse("Esta es la página de despedida")


def curso_django(request):
    fecha_actual = datetime.datetime.now()
    return render(request, "curso_django.html", {"fecha_actual": fecha_actual})


def curso_python(request):
    fecha_actual = datetime.datetime.now()
    return render(request, "curso_python.html", {"fecha_actual": fecha_actual})


class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
