from django.shortcuts import render,redirect
from Clientes.models import Cliente
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import CreateView, TemplateView
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView, TemplateView
from .models import Perfil
from .forms import SignUpForm,UserPerfilForm
from django.contrib.auth.views import LoginView, LogoutView 

# Create your views here.
def Inicio(request):
    return render(request,'home.html')
@csrf_exempt #Esto permite enviar el mensaje al correo, si se quita da error :)
def Mensaje(request):
    if request.method=="POST":
        asunto=request.POST["asunto"]

        mensaje=request.POST["mensaje"]+ " "+ request.POST["email"]

        email_from=settings.EMAIL_HOST_USER
        destinatario=["dulcecaprichohelados@gmail.com"] #Correo destinatario

        send_mail(asunto, mensaje, email_from, destinatario)

        return render(request,'confirmaEnvio.html')

    return render(request,'mensaje.html')
def Bienvenida(request):
    return render(request,"header.html")
def Promo(request):
    return render(request,'promociones.html')  
#Es usado para poder hacer logout
class SignOutView(LogoutView):
    pass
#vista basada en clase para el login
class SignInView(LoginView):
    template_name = 'login.html'
#Formulario de registro
def SignUpView(request):
    if request.method=="POST":
        #Se extrae la información del formulario
        form=SignUpForm(request.POST)
        perfil=UserPerfilForm(request.POST)
        if form.is_valid() and perfil.is_valid():#Se verifica que el formulario sea válido
            '''
            En este parte, si el formulario es valido guardamos lo que se obtiene de él y usamos authenticate para que el usuario incie sesión luego de haberse registrado y lo redirigimos al index
            '''
            user=form.save()#Se guarda el formulario en la base de datos, en la tabla Clientes_user
            cli=Cliente(nombre=form.cleaned_data["username"],numero_contacto=perfil.cleaned_data["numero_contacto"],correo=form.cleaned_data["email"],cumpleanos=perfil.cleaned_data["cumpleaños"])
            cli.save()
            #Con esto auténtica el usuario para que pueda hacer login
            usuario = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            usuario = authenticate(username=usuario, password=password)
            login(request, usuario)
            return redirect('/Bienvenido/')
    else:
        form=SignUpForm()
        perfil=UserPerfilForm()
    return render(request,"formulario.html",{"form":form,"perfil_form":perfil})


  
  

  