from django.contrib import admin

from .models import Cart, CartItem,CartItem2,CartItem3

class CartAdmin(admin.ModelAdmin):
    class Meta:
        model =Cart

admin.site.register(Cart,CartAdmin)
admin.site.register(CartItem)
admin.site.register(CartItem2)
admin.site.register(CartItem3)
