from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
# Create your views here.
from .models import Cart,CartItem,CartItem2,CartItem3
from  Productos.models import Producto,CopasHelados,Malteada


def view(request):
     try:
          the_id = request.session['cart_id'] # si ya existe lo toma ese carrito
     except:
          the_id= None
     if the_id:
          cart =Cart.objects.get(id=the_id) # por ahora esta trabajando con el id del carrito 1 
          context = {"cart":cart}
     else:
          empty_message= " No tienes nada en el carrito por favor, vuelve a domicilios para hacer tu pedido"
          context ={"empty":True, "empty_message":empty_message}
     return render(request,'carrito.html',context)



def updatecart(request,slug):
     request.session.set_expiry(1000)  # con este se controla el tiempo en el que se vence el carrito ejmplo 300.. segundo
     try:
          qty = request.GET.get('qty')
          update_qty = True
     except:
          qty = ''
          update_qty = False


     try:
          the_id = request.session['cart_id'] # si ya existe lo toma ese carrito
     except: # sino crea un nuevo carrito
          new_cart=Cart()
          new_cart.save()
          request.session['cart_id'] =new_cart.id
          the_id = new_cart.id
     cart = Cart.objects.get(id=the_id) # arma el carro con la misma id del la base de datos cart 
     if Producto.objects.filter(slug=slug).exists(): # verifica en que categoria esta
          producto=Producto.objects.get(slug=slug)
          cart_item,created =CartItem.objects.get_or_create(cart=cart,Producto1=producto) 
          if update_qty and qty: # qty es la cantidad de productos por tanto si es cero lo elimina 
               if int(qty)==0:
                    cart_item.delete()
               else:
                    cart_item.quantity=qty
                    cart_item.save()
          else:
               pass
     if CopasHelados.objects.filter(slug=slug).exists():
          producto=CopasHelados.objects.get(slug=slug)
          cart_item2,created =CartItem2.objects.get_or_create(cart=cart,Producto2=producto) 
          if update_qty and qty:
               if int(qty)==0:
                    cart_item2.delete()
               else:
                    cart_item2.quantity=qty 
                    cart_item2.save()
          else:
               pass
     if Malteada.objects.filter(slug=slug).exists():
          producto=Malteada.objects.get(slug=slug)
          cart_item3,created =CartItem3.objects.get_or_create(cart=cart,Producto3=producto) 
          if update_qty and qty:
               if int(qty)==0:
                    cart_item3.delete()
               else:
                    cart_item3.quantity=qty
                    cart_item3.save()
          else:
               pass
          
     sumaTotal=0
     # hace la sumatoria de todas la categorias que esten en el carrito
     for item in cart.cartitem_set.all():
          line_total=  item.Producto1.precio *item.quantity
          sumaTotal+= line_total # producto
     cart.total = sumaTotal
     cart.save()
     sumaTotal=0

     for item in cart.cartitem2_set.all():
          line_total=  item.Producto2.precio *item.quantity # multiplica la cantidad por el precio del producto
          sumaTotal+= line_total 
     cart.total += sumaTotal
     cart.save()

     sumaTotal=0

     for item in cart.cartitem3_set.all():
          line_total=  item.Producto3.precio *item.quantity
          sumaTotal+= line_total 
     cart.total += sumaTotal
     cart.save()
     
     request.session['items_total'] = cart.cartitem3_set.count()+cart.cartitem2_set.count()+cart.cartitem_set.count() # con esto sabemos cuantos  productos hay en el carrito 
     print (cart.cartitem_set.count() ) 
     return HttpResponseRedirect("/cart/") # no me quiere leer el nombre de la vista entonces lo deje asi

