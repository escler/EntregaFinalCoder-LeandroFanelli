from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from AppCoder.models import Avatar
from django.shortcuts import redirect
from clase18.forms import CreateBlog
from datetime import datetime
from AppCoder.models import Page

class AvatarView:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        avatares = Avatar.objects.filter(user=self.request.user.id)
        if avatares.count() == 0:
            context["avatar_url"] = '/media/avatares/Default_Image.png'
        else:
            context["avatar_url"] = Avatar.objects.filter(user=self.request.user).last().imagen.url
        
        return context
    
class Page_ListView(LoginRequiredMixin, AvatarView, ListView):
    model = Page
    context_object_name = 'pages'
    template_name = 'AppCoder/pages.html'

    
class Page_DetailView(LoginRequiredMixin, AvatarView, DetailView):
    model = Page
    template_name = 'AppCoder/ver_pages.html'
    
class Page_UpdateView(LoginRequiredMixin, AvatarView, UpdateView):
    model = Page
    success_url = reverse_lazy('pages')
    fields = ['titulo', 'subtitulo', 'cuerpo', 'autor', 'imagen']
    template_name = 'AppCoder/Formulario.html'
    
class Page_DeleteView(LoginRequiredMixin, AvatarView, DeleteView):
    model = Page
    success_url = reverse_lazy('pages')
    
@login_required
def create_page(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    
    if request.method == 'POST':
        formulario = CreateBlog(request.POST, request.FILES)

        if formulario.is_valid():
            data = formulario.cleaned_data
            page = Page(usuario=request.user, titulo=data['titulo'], subtitulo=data['subtitulo'], cuerpo=data['cuerpo'], autor=data['autor'], fecha=datetime.now(), imagen=data['imagen'])
            page.save()
            return redirect('pages')
    else:
        formulario = CreateBlog()
        
    if avatares.count() == 0:       
        return render(request, 'AppCoder/Formulario.html', {'form': formulario, 'avatar_url':'/media/avatares/Default_Image.png'})
    else:
        return render(request, 'AppCoder/Formulario.html', {'form': formulario, 'avatar_url':avatares[0].imagen.url} )