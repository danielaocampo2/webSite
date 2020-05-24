from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from Clientes.views import Bienvenida,Inicio, Mensaje, Promo,SignUpView,SignOutView,SignInView
from carts.views import  view, updatecart
from Productos.views import Wensaladas, Chelados, malteadas


urlpatterns=[
    path('Home/',Inicio,name="inicio"),
    path('Mensaje/',Mensaje,name="mensaje"),
    path('Registro/',SignUpView, name='sign_up'),
    path('Login/',SignInView.as_view(), name='sign_in'),
    path('Logout/',SignOutView.as_view(), name='sign_out'),
    path('Promociones/',Promo, name="promo"),
    path('Malteadas/',malteadas,name="malteadas"),
     path('Bienvenido/',Bienvenida,name="bienvenida"),
    path('cart/',view, name="cart"),
    path('cart/<slug:slug>/',updatecart , name="updatecart"),
    path('Waffles/',Wensaladas, name="single_ho"),
    path('CopasHelado/',Chelados, name="Chelados"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)