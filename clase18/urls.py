"""clase18 URL Configuration

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
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from clase18.views import login_request, register, about, inicio, editProfile, agregar_avatar
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls, name='Admin'),
    path('', include('AppCoder.urls')), 
    path('accounts/login/', login_request, name='login'),
    path('accounts/signup/', register, name='registro'),
    path('logout/', LogoutView.as_view(template_name='logout.html'),name = 'logout'),
    path('accounts/editprofile', editProfile, name='profile_edit'),
    path('accounts/editavatar', agregar_avatar, name='edit_avatar'),
    path('about/', about, name = 'about'),
    path('', inicio, name='Inicio'),
]

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
