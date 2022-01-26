from django.db.models import Model
from django.db.models.fields import CharField, EmailField, IntegerField

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