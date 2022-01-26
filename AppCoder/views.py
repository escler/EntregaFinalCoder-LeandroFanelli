from msilib.schema import ListView
from typing import List
from django.http import HttpResponse, HttpResponseRedirect, request
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from AppCoder.models import Curso, Estudiante, Profesor

def inicio(request):
    return render(request, 'AppCoder/inicio.html')


class Curso_ListView(ListView):
    model = Curso
    template_name = 'AppCoder/cursos.html'
    context_object_name = 'cursos'
    
class Curso_DetailView(DetailView):
    model = Curso
    template_name = 'AppCoder/ver_curso.html'

class Curso_CreateView(CreateView):
    model = Curso
    success_url = reverse_lazy('cursos')
    fields = ['nombre', 'camada']
    template_name = 'AppCoder/cursoFormulario.html'
    
class Curso_UpdateView(UpdateView):
    model = Curso
    success_url = reverse_lazy('cursos')
    fields = ['nombre', 'camada']
    template_name = 'AppCoder/cursoFormulario.html'
    
class Curso_DeleteView(DeleteView):
    model = Curso
    success_url = reverse_lazy('cursos')
    
def buscarCurso(request):
    return render(request, 'AppCoder/buscarCurso.html')

def resultadoBuscarCurso(request):
    
    if request.GET["camada"]:
        
        camada = request.GET['camada']
        cursos = Curso.objects.filter(camada__icontains=camada)
        
        return render(request, 'AppCoder/resultadoBusquedaCurso.html', {'cursos':cursos, 'camada':camada})
    
    else:
        respuesta = 'No enviaste datos'

    return HttpResponse(respuesta)

class Estudiante_ListView(ListView):
    model = Estudiante
    template_name = 'AppCoder/estudiantes.html'
    context_object_name = 'estudiantes'
    
class Estudiante_DetailView(DetailView):
    model = Estudiante
    template_name = 'AppCoder/ver_estudiante.html'

class Estudiante_CreateView(CreateView):
    model = Estudiante
    success_url = reverse_lazy('estudiantes')
    fields = ['nombre', 'apellido', 'email']
    template_name = 'AppCoder/cursoFormulario.html'
    
class Estudiante_UpdateView(UpdateView):
    model = Estudiante
    success_url = reverse_lazy('estudiantes')
    fields = ['nombre', 'apellido', 'email']
    template_name = 'AppCoder/cursoFormulario.html'
    
class Estudiante_DeleteView(DeleteView):
    model = Estudiante
    success_url = reverse_lazy('estudiantes')
    
class Profesor_ListView(ListView):
    model = Profesor
    template_name = 'AppCoder/profesores.html'
    context_object_name = 'profesores'
    
class Profesor_DetailView(DetailView):
    model = Profesor
    template_name = 'AppCoder/ver_profesores.html'

class Profesor_CreateView(CreateView):
    model = Profesor
    success_url = reverse_lazy('profesores')
    fields = ['nombre', 'apellido', 'email', 'profesion']
    template_name = 'AppCoder/cursoFormulario.html'
    
class Profesor_UpdateView(UpdateView):
    model = Profesor
    success_url = reverse_lazy('profesores')
    fields = ['nombre', 'apellido', 'email', 'profesion']
    template_name = 'AppCoder/cursoFormulario.html'
    
class Profesor_DeleteView(DeleteView):
    model = Profesor
    success_url = reverse_lazy('profesores')