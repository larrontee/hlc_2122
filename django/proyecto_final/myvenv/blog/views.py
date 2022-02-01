from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.


def auth(request):
    return HttpResponse("Esta es la página de auth")


def tareas(request):
    return HttpResponse("Esta es la página de tareas")
