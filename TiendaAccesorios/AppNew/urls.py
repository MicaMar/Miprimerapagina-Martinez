from django.urls import path
from AppNew.views import *

urlpatterns = [
    path('inicio/', inicio, name = "inicio") ,
    path('lista_stock/', lista_stock, name = "lista_stock") ,
    path('busquedaproducto/', busquedaproducto, name = "busquedaproducto") ,
    path('stock/', producto_formulario, name = "producto_formulario") ,
    path('buscar/', buscar, name = "buscar") ,
    path('cliente/', cliente, name = "cliente") ,
    path('empleado/', empleado, name = "empleado") ,
]  