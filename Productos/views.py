from django.shortcuts import render, Http404

# Create your views here.
from .models import Producto,CopasHelados,Malteada


def Wensaladas(request):
    context = {'Productos': Producto.objects.all()} # toma todos los productos que estan en la BD
    template = 'Helados.html'
    return render (request,template,context)


def Chelados(request):
    context = {'Productos': CopasHelados.objects.all()} # toma todos los productos que estan en la BD
    template = 'Helados.html'
    return render (request,template,context)

def malteadas(request):
    context = {'Productos': Malteada.objects.all()} # toma todos los productos que estan en la BD
    template = 'Helados.html'
    return render (request,template,context)