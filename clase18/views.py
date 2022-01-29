from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from clase18.forms import UserEditForm, UserRegisterForm
from django.contrib.auth.decorators import login_required

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
    return render(request, 'about.html')

def inicio(request):
    return render(request, 'AppCoder/inicio.html')

@login_required

def editProfile(request):
    
    usuario = request.user
    
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
            
            return render(request, 'AppCoder/Inicio.html')
        
    else:
        
        form = UserEditForm(initial={'email':usuario.email, 'first_name':usuario.first_name, 'last_name':usuario.last_name})
    
    return render(request, 'AppCoder/profile_edit.html', {'form':form, 'usuario': usuario})