"""tareas_fct URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from tareas.views import insertar_tareas, listar_tareas, mostrar_tarea, editar_tarea, borrar_tarea
from oauth_app.views import login_bootstrap

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listar_tareas),
    path('accounts/', include('allauth.urls')),
    path('logout', LogoutView.as_view()),
    path('insertar_tarea/', insertar_tareas),
    path('listar_tareas/', listar_tareas),
    path('mostrar_tarea/', mostrar_tarea),
    path('editar_tarea/<int:tarea_id>/', editar_tarea),
    path('borrar_tarea/<int:tarea_id>/', borrar_tarea),

]
