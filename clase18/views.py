from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from AppCoder.models import Avatar
from clase18.forms import UserEditForm, UserRegisterForm
from django.contrib.auth.decorators import login_required
from clase18.forms import EditAvatar

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data['username']
            contrasena = form.cleaned_data['password']
            user = authenticate(username=usuario, password=contrasena)
            
            if user is not None:
                login(request, user)
                return redirect('Inicio')
            else:
                return render(request, 'login.html', {'form': form})
            
        else: return render(request, 'login.html', {'form': form})
    
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
    
def register(request):
    
    if request.method == 'POST':
        
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            
            username = form.cleaned_data['username']
            form.save()
            return render(request, 'registroCompletado.html')
        
    else:
        form = UserRegisterForm()
            
    return render(request,'registro.html', {'form': form})

@login_required
def about(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    if avatares.count() == 0:
        return render(request, 'about.html', {'avatar_url':'/media/avatares/Default_Image.png'})
    else:
        return render(request, 'about.html', {'avatar_url':avatares[0].imagen.url})

def inicio(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    if avatares.count() == 0:
        return render(request, 'AppCoder/inicio.html', {'avatar_url': '/media/avatares/Default_Image.png'})
    else:
        print(Avatar.objects.count())
        return render(request, 'AppCoder/inicio.html', {'avatar_url':avatares[0].imagen.url})

@login_required

def editProfile(request):
    
    usuario = request.user
    
    avatares = Avatar.objects.filter(user=request.user.id)
    
    if request.method == 'POST':
        
        form = UserEditForm(request.POST)
        
        if form.is_valid():
            
            data = form.cleaned_data
            
            usuario.email = data['email']
            usuario.set_password(data['password1'])
            usuario.password2 = data['password2']             
            usuario.first_name = data['first_name']
            usuario.last_name = data['last_name']
            
            usuario.save()
            
            return render(request, 'edit_profile_success.html')
        
    else:
        if avatares.count() == 0:
            form = UserEditForm(initial={'email':usuario.email, 'first_name':usuario.first_name, 'last_name':usuario.last_name, 'avatar_url':'/media/avatares/Default_Image.png'})
        else:
            form = UserEditForm(initial={'email':usuario.email, 'first_name':usuario.first_name, 'last_name':usuario.last_name, 'avatar_url':avatares[0].imagen.url}) 
            
    if avatares.count() == 0:       
        return render(request, 'AppCoder/profile_edit.html', {'form':form, 'usuario': usuario, 'avatar_url':'/media/avatares/Default_Image.png'}) 
    else:
        return render(request, 'AppCoder/profile_edit.html', {'form':form, 'usuario': usuario, 'avatar_url':avatares[0].imagen.url})

@login_required
def agregar_avatar(request):
    
    if request.method == 'POST':
        formulario = EditAvatar(request.POST, request.FILES)

        if formulario.is_valid():
            avatar = Avatar(user=request.user, imagen=formulario.cleaned_data['imagen'])
            avatar.save()
            return redirect('Inicio')
    else:
        formulario = EditAvatar()

    return render(request, 'AppCoder/editAvatar.html', {'form': formulario})