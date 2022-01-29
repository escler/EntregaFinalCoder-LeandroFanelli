from sqlite3 import Time
from django.db.models import Model
from django.db.models.fields import CharField, DateTimeField

from datetime import datetime

# Create your models here.

class Page(Model):
    titulo = CharField(max_length=20)
    subtitulo = CharField(max_length=50)
    cuerpo = CharField(max_length=10000)
    autor = CharField(max_length=20)
    fecha = DateTimeField(default=datetime.now(), editable=True)
    
    def __str__(self):
        return f'Titulo:{self.titulo} - Autor del blog:{self.autor}'