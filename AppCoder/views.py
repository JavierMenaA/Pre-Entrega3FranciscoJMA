from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso, Estudiantes

# Create your views here.

def inicio(request):
    
    return render(request, "inicio.html")

def ver_estudiantes(request):
    
    return render(request, "ver_estudiante.html")

def ver_cursos(request):
    
    return render(request, "ver_cursos.html")

def ver_profesores(request):
    
    return render(request, "ver_profesores.html")

def ver_entregables(request):
    
    return render(request, "ver_entregables.html")

def crear_curso(request):
    
    curso_1 = Curso(nombre="Desarrollo movil", comision=555555)
    
    curso_1.save()
    
    return HttpResponse(f"Se ha creado un Curso {curso_1.nombre}!!")


def crear_estudiantes(request):
    
    est_1 = Estudiantes(nombre="Diego", apellido="De La Fuente", email="studiante@ch.com", edad=28)
    
    est_2 = Estudiantes(nombre="Belen", apellido="Ulloa", email="studiante2@ch.com", edad=38)
    
    est_1.save()
    est_2.save()  
    
    info = {"nombre1":est_1.nombre, 'nombre2':est_2.nombre}
    
    return render(request, "crear_estudiantes.html", info)  
    