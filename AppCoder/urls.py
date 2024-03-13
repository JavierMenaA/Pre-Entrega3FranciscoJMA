from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path("curso/", crear_curso),
    path("estudiantes/", crear_estudiantes),
    path("ver_cursos", ver_cursos),
    path("ver_estudiantes", ver_estudiantes),
    path("ver_profesores", ver_profesores),
    path("ver_entregables", ver_entregables),
    path("", inicio),
]