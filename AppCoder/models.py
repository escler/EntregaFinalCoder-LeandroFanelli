from django.db.models import Model, ForeignKey, CASCADE, ImageField, TextField
from django.db.models.fields import CharField, DateTimeField
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Avatar(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    imagen = ImageField(upload_to='avatares', default='avatares/Default_Image.png')

class Page(Model):
    usuario = ForeignKey(User, on_delete=CASCADE)
    titulo = CharField(max_length=20)
    subtitulo = CharField(max_length=50)
    cuerpo = TextField(max_length=10000)
    autor = CharField(max_length=20)
    fecha = DateTimeField(default=datetime.now(), editable=True)
    imagen = ImageField(upload_to = 'blog_imagenes', blank = True)
    
    def __str__(self):
        return f'Titulo:{self.titulo} - Autor del blog:{self.autor}'
