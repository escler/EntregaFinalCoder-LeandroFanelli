from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import EmailField, CharField, PasswordInput

class UserRegisterForm(UserCreationForm):
    email = EmailField()
    password1 = CharField(label='Contraseña', widget=PasswordInput)
    password2 = CharField(label='Repetir la contraseña', widget=PasswordInput)
    first_name = CharField(label='Nombre')
    last_name = CharField(label='Apellido')
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name','password1', 'password2']
        help_texts = {k:'' for k in fields}
        
class UserEditForm(UserCreationForm):
    email = EmailField()
    password1 = CharField(label='Contraseña', widget=PasswordInput)
    password2 = CharField(label='Repetir la contraseña', widget=PasswordInput)
    first_name = CharField(label='Nombre')
    last_name = CharField(label='Apellido')
    
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name','password1', 'password2']
        help_texts = {k:'' for k in fields}