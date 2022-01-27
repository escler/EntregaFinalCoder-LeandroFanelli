from sqlite3 import Time
from django.db.models import Model
from django.db.models.fields import CharField, EmailField, IntegerField, TimeField, DateTimeField

from datetime import datetime

# Create your models here.
class Curso(Model):
    nombre = CharField(max_length=40)
    camada = IntegerField()
    
    def __str__(self):
        return f'Curso:{self.nombre}'
    
class Estudiante(Model):
    nombre = CharField(max_length=30)
    apellido = CharField(max_length=30)
    email = EmailField()
    
    def __str__(self):
        return f'Nombre:{self.nombre} {self.apellido} Email: {self.email}'
    
class Profesor(Model):
    nombre = CharField(max_length=30)
    apellido = CharField(max_length=30)
    email = EmailField()
    profesion = CharField(max_length=30)
    
    def __str__(self):
        return f'Profesor:{self.nombre} {self.apellido} Email: {self.email} Profesion: {self.profesion} '
    
class Page(Model):
    titulo = CharField(max_length=20)
    subtitulo = CharField(max_length=50)
    cuerpo = CharField(max_length=500)
    autor = CharField(max_length=20)
    fecha = DateTimeField(default=datetime.now(), editable=True)
    
    def __str__(self):
        return f'Titulo:{self.titulo} - Autor del blog:{self.autor}'