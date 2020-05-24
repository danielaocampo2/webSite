from django.contrib import admin

# Register your models here.
from .models import Producto, CopasHelados, Malteada # conecto el modelo con el admin

class ProductoAdmin(admin.ModelAdmin):
    list_display= ("nombre","precio") # LOS CAMPOS QUE QUIERO VER
    search_fields=['nombre','descripcion'] # busca con estos dos atributos
    list_filter=("precio",)
    prepopulated_fields ={"slug": ("nombre",)} # convierte el titulo en slug o sea le quita los espacios y mayusculas
    
    class Meta:
        model = Producto
admin.site.register(Producto,ProductoAdmin)
class CopasHeladosAdmin(admin.ModelAdmin):
    list_display= ("nombre","precio") # LOS CAMPOS QUE QUIERO VER
    search_fields=['nombre','descripcion'] # busca con estos dos atributos
    list_filter=("precio",)
    prepopulated_fields ={"slug": ("nombre",)} # convierte el titulo en slug o sea le quita los espacios y mayusculas
    
    class Meta:
        model = CopasHelados

admin.site.register(CopasHelados,CopasHeladosAdmin)

class MalteadaAdmin(admin.ModelAdmin):
    list_display= ("nombre","precio") 
    search_fields=['nombre','descripcion'] 
    list_filter=("precio",)
    prepopulated_fields ={"slug": ("nombre",)} 
    
    class Meta:
        model = Malteada
admin.site.register(Malteada,MalteadaAdmin)




