from django.db import models

from Productos.models import Producto,CopasHelados,Malteada

class Cart(models.Model): # este es el de waffles
    #items = models.ManyToManyField(CartItem)
    #Productos=models.ManyToManyField(Producto)
    #Producto2=models.ManyToManyField(CopasHelados)
    #Producto3=models.ManyToManyField(Malteada)
    total=models.IntegerField(default=0)
    active=models.BooleanField(default=True)

    def __str__(self):
        return "Cart id: %s"  % (self.id) # lo que nos va aparecer

class CartItem(models.Model): # esto es para que me deje agregar mas de un solo producto al carrito de compra
    cart=models.ForeignKey(Cart, on_delete=models.CASCADE,null=True,blank=True)
    Producto1= models.ForeignKey(Producto, on_delete=models.CASCADE,)
    quantity= models.IntegerField(default=1) # comienza en 1 pero se ira agregando mas 
    line_total= models.IntegerField(default=10)

    def __str__(self):
        try:
            return str(self.cart.id)
        except:
            return self.Producto1.titel   

class CartItem2(models.Model): # esto es para que me deje agregar mas de un solo producto al carrito de compra
    cart=models.ForeignKey(Cart, on_delete=models.CASCADE,null=True,blank=True)
    Producto2= models.ForeignKey(CopasHelados, on_delete=models.CASCADE,)
    quantity= models.IntegerField(default=1) # comienza en 1 pero se ira agregando mas 
    line_total= models.IntegerField(default=10)

    def __str__(self):
        try:
            return str(self.cart.id)
        except:
            return self.Producto2.titel  

class CartItem3(models.Model): # esto es para que me deje agregar mas de un solo producto al carrito de compra
    cart=models.ForeignKey(Cart, on_delete=models.CASCADE,null=True,blank=True)
    Producto3= models.ForeignKey(Malteada, on_delete=models.CASCADE,)
    quantity= models.IntegerField(default=1) # comienza en 1 pero se ira agregando mas 
    line_total= models.IntegerField(default=10)

    def __str__(self):
        try:
            return str(self.cart.id)
        except:
            return self.Producto3.titel  
    
   