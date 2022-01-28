from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from AppCoder.models import Page
    
@login_required
def buscarCurso(request):
    return render(request, 'AppCoder/buscarCurso.html')

@login_required
def resultadoBuscarCurso(request):
    
    if request.GET["camada"]:
        
        camada = request.GET['camada']
        #cursos = Curso.objects.filter(camada__icontains=camada)
        
        #return render(request, 'AppCoder/resultadoBusquedaCurso.html', {'cursos':cursos, 'camada':camada})
    
    else:
        respuesta = 'No enviaste datos'

    return HttpResponse(respuesta)
    
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
    template_name = 'AppCoder/Formulario.html'
    
class Page_UpdateView(LoginRequiredMixin, UpdateView):
    model = Page
    success_url = reverse_lazy('pages')
    fields = ['titulo', 'subtitulo', 'cuerpo', 'autor']
    template_name = 'AppCoder/Formulario.html'
    
class Page_DeleteView(LoginRequiredMixin, DeleteView):
    model = Page
    success_url = reverse_lazy('pages')