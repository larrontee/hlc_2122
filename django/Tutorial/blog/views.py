from django.shortcuts import render
from django.http.response import HttpResponse
import datetime

# Create your views here.


def saludo(request):
    return render(request, "saludo.html", {"nombre_persona": "Juan", "apellido_persona": "Pérez", "fecha_actual": datetime.datetime.now()})


def despedida(request):
    return HttpResponse("Esta es la página de despedida")
