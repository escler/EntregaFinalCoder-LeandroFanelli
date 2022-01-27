from typing import List
from django.http import HttpResponse, HttpResponseRedirect, request
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from AppCoder.models import Curso, Estudiante, Profesor, Page


class Curso_ListView(LoginRequiredMixin, ListView):
    model = Curso
    template_name = 'AppCoder/cursos.html'
    context_object_name = 'cursos'
    
class Curso_DetailView(LoginRequiredMixin, DetailView):
    model = Curso
    template_name = 'AppCoder/ver_curso.html'

class Curso_CreateView(LoginRequiredMixin, CreateView):
    model = Curso
    success_url = reverse_lazy('cursos')
    fields = ['nombre', 'camada']
    template_name = 'AppCoder/cursoFormulario.html'
    
class Curso_UpdateView(LoginRequiredMixin, UpdateView):
    model = Curso
    success_url = reverse_lazy('cursos')
    fields = ['nombre', 'camada']
    template_name = 'AppCoder/cursoFormulario.html'
    
class Curso_DeleteView(LoginRequiredMixin, DeleteView):
    model = Curso
    success_url = reverse_lazy('cursos')
    
@login_required
def buscarCurso(request):
    return render(request, 'AppCoder/buscarCurso.html')

@login_required
def resultadoBuscarCurso(request):
    
    if request.GET["camada"]:
        
        camada = request.GET['camada']
        cursos = Curso.objects.filter(camada__icontains=camada)
        
        return render(request, 'AppCoder/resultadoBusquedaCurso.html', {'cursos':cursos, 'camada':camada})
    
    else:
        respuesta = 'No enviaste datos'

    return HttpResponse(respuesta)

class Estudiante_ListView(LoginRequiredMixin, ListView):
    model = Estudiante
    template_name = 'AppCoder/estudiantes.html'
    context_object_name = 'estudiantes'
    
class Estudiante_DetailView(LoginRequiredMixin, DetailView):
    model = Estudiante
    template_name = 'AppCoder/ver_estudiante.html'

class Estudiante_CreateView(LoginRequiredMixin, CreateView):
    model = Estudiante
    success_url = reverse_lazy('estudiantes')
    fields = ['nombre', 'apellido', 'email']
    template_name = 'AppCoder/cursoFormulario.html'
    
class Estudiante_UpdateView(LoginRequiredMixin, UpdateView):
    model = Estudiante
    success_url = reverse_lazy('estudiantes')
    fields = ['nombre', 'apellido', 'email']
    template_name = 'AppCoder/cursoFormulario.html'
    
class Estudiante_DeleteView(LoginRequiredMixin, DeleteView):
    model = Estudiante
    success_url = reverse_lazy('estudiantes')
    
class Profesor_ListView(LoginRequiredMixin, ListView):
    model = Profesor
    template_name = 'AppCoder/profesores.html'
    context_object_name = 'profesores'
    
class Profesor_DetailView(LoginRequiredMixin, DetailView):
    model = Profesor
    template_name = 'AppCoder/ver_profesores.html'

class Profesor_CreateView(LoginRequiredMixin, CreateView):
    model = Profesor
    success_url = reverse_lazy('profesores')
    fields = ['nombre', 'apellido', 'email', 'profesion']
    template_name = 'AppCoder/cursoFormulario.html'
    
class Profesor_UpdateView(LoginRequiredMixin, UpdateView):
    model = Profesor
    success_url = reverse_lazy('profesores')
    fields = ['nombre', 'apellido', 'email', 'profesion']
    template_name = 'AppCoder/cursoFormulario.html'
    
class Profesor_DeleteView(LoginRequiredMixin, DeleteView):
    model = Profesor
    success_url = reverse_lazy('profesores')
    
class Page_ListView(LoginRequiredMixin, ListView):
    model = Page
    context_object_name = 'pages'
    template_name = 'AppCoder/pages.html'

    
class Page_DetailView(LoginRequiredMixin, DetailView):
    model = Page
    template_name = 'AppCoder/ver_pages.html'

class Page_CreateView(LoginRequiredMixin, CreateView):
    model = Page
    success_url = reverse_lazy('pages')
    fields = ['titulo', 'subtitulo', 'cuerpo', 'autor']
    template_name = 'AppCoder/cursoFormulario.html'
    
class Page_UpdateView(LoginRequiredMixin, UpdateView):
    model = Page
    success_url = reverse_lazy('pages')
    fields = ['titulo', 'subtitulo', 'cuerpo', 'autor']
    template_name = 'AppCoder/cursoFormulario.html'
    
class Page_DeleteView(LoginRequiredMixin, DeleteView):
    model = Page
    success_url = reverse_lazy('pages')