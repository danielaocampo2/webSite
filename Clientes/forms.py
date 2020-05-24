from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from .models import Cliente
from .models import Perfil

"""
https://www.it-swarm.dev/es/django/como-mostrar-el-calendario-de-datepicker-en-datefield/1072060141/
"""
class Formulario(forms.Form):
    usuario=forms.CharField(max_length=30)
    nombre=forms.CharField(max_length=30)
    apellido=forms.CharField(max_length=30)
    numero_contacto=forms.IntegerField()
    correo=forms.EmailField()
    cumpleaños=forms.DateField(widget=forms.DateTimeInput(attrs={'class': 'datetime-input'}))
    contraseña=forms.CharField(widget=forms.PasswordInput())
    confirme_contraseña=forms.CharField(widget=forms.PasswordInput())

#Formulario básico
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=140, required=True)
    last_name = forms.CharField(max_length=140, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        #Tabla de la base de datos
        model = User
        #Campos requeridos
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        ]
        #Como se van a nombrar los campos en el template.
        labels={
            'username':'Username',
            'email':'Correo electronico',
            'first_name':'Nombre',
            'last_name':'Apellido',
            'password1':'Contraseña',
            'password2':'Confirme Contraseña',
        }
#Formulario con el cuál se piden los dato adiciónales
class UserPerfilForm(forms.ModelForm):
    cumpleaños=forms.DateField(widget=forms.DateTimeInput(attrs={'class': 'datetime-input'}),required=True)
    numero_contacto=forms.IntegerField()
    class Meta:
        model=Perfil
        fields=['cumpleaños','numero_contacto']
        labels={
            'cumpleaños':'Cumpleaños',
            'numero_contacto':'Número de Contacto',
        }
