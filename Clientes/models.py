from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Cliente(models.Model):
    nombre=models.CharField(max_length=30)
    numero_contacto=models.IntegerField()
    correo=models.EmailField()
    cumpleanos=models.DateField()
    ##contrasena=models.CharField(max_length=20)

class Perfil(models.Model):
    usuario= models.OneToOneField(User, on_delete=models.CASCADE,blank=True,null=True)
    cumpleaños=models.DateField(blank=True,null=True)
    numero_contacto=models.IntegerField(blank=True,null=True)


    @receiver(post_save, sender=User)
    def crear_usuario_perfil(sender, instance, created, **kwargs):
        if created:
            Perfil.objects.create(usuario=instance)

    @receiver(post_save, sender=User)
    def guardar_usuario_perfil(sender, instance, **kwargs):
        instance.perfil.save()
    