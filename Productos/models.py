from django.urls import reverse
from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre=models.CharField(max_length=120, unique=True)
    descripcion=models.TextField(null= True, blank= True)
    precio=models.IntegerField()
    image=models.ImageField(upload_to='Productos/images', null=True)
    active=models.BooleanField(default=True)
    slug= models.SlugField(unique=True, null=True)
    
    class Meta:
        unique_together = [['nombre','slug']]

    def __str__(self):
        return self.nombre  # lo que nos va aparecer
     
    
class CopasHelados(models.Model):
    nombre=models.CharField(max_length=120, unique=True)
    descripcion=models.TextField(null= True, blank= True)
    precio=models.IntegerField()
    image=models.ImageField(upload_to='CopasHelados/images', null=True)
    active=models.BooleanField(default=True)
    slug= models.SlugField(unique=True, null=True)
    
    
    class Meta:
        unique_together = [['nombre','slug']]

    def __str__(self):
        return self.nombre 

class Malteada(models.Model):
    nombre=models.CharField(max_length=120, unique=True)
    descripcion=models.TextField(null= True, blank= True)
    precio=models.IntegerField()
    image=models.ImageField(upload_to='Malteada/images', null=True)
    active=models.BooleanField(default=True)
    slug= models.SlugField(unique=True, null=True)
    
    class Meta:
        unique_together = [['nombre','slug']]

    def __str__(self):
        return self.nombre