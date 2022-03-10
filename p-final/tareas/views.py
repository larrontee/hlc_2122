from datetime import datetime
from django.shortcuts import render
from django.contrib.auth.models import User
from tareas.models import Tarea

# Create your views here.


def insertar_tareas(request):
    if (request.method == 'POST' and request.user.id != None):
        tarea = Tarea()
        tarea.user_id = request.user.id
        tarea.fecha = request.POST["fecha"]
        tarea.horas = request.POST["horas"]
        tarea.descripcion = request.POST["descripcion"]
        tarea.save()
        return render(request, 'mostrar_tarea.html', {'tarea': tarea})
    else:
        tarea = Tarea()
        tarea.user_id = request.user.id
        tarea.fecha = datetime.now()
        tarea.horas = 0
        tarea.descripcion = ""
        return render(request, 'insertar_tareas.html', {'tarea': tarea, 'action': '/insertar_tarea/'})


def listar_tareas(request):
    tareas = Tarea.objects.filter(user_id=request.user.id)
    return render(request, 'listar_tareas.html', {'tareas': tareas})


def mostrar_tarea(request):
    if (request.method == 'POST' and request.user.id != None):
        tarea = Tarea.objects.get(id=request.POST["id"])
        return render(request, 'mostrar_tarea.html', {'tarea': tarea})


def editar_tarea(request, tarea_id):
    if (request.method == 'POST' and request.user.id != None):
        tarea = Tarea.objects.get(id=tarea_id)
        tarea.fecha = request.POST["fecha"]
        tarea.horas = request.POST["horas"]
        tarea.descripcion = request.POST["descripcion"]
        tarea.save()
        print("salvando tarea editada")
        print(tarea)
        return render(request, 'mostrar_tarea.html', {'tarea': tarea})
    else:
        print("editando tarea")
        tarea = Tarea.objects.get(id=tarea_id)
        return render(request, 'insertar_tareas.html', {'tarea': tarea, 'action': '/editar_tarea/{}/'.format(tarea_id)})


def borrar_tarea(request, tarea_id):
    tarea = Tarea.objects.get(id=tarea_id)
    tarea.delete()
    return render(request, 'borrar_tarea.html', {'tarea': tarea})
