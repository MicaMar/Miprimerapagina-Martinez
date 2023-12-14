from django.urls import path
from AppNew.views import *

urlpatterns = [
    path('inicio/', inicio, name = "inicio") ,
    path('lista_stock/', lista_stock, name = "lista_stock") ,
    path('busquedaproducto/', busquedaproducto, name = "busquedaproducto") ,
    path('stock/', producto_formulario, name = "producto_formulario") ,
    path('buscar/', buscarP, name = "buscar") ,
    path('cliente/', cliente, name = "cliente") ,
    path('empleado/', empleado, name = "empleado") ,
    
    path('crear_cliente/', crear_cliente, name='crear cliente'),
    path('leer_clientes/', leer_clientes, name='leer clientes'),
    path('eliminar_cliente/<nombre_cliente>', eliminar_cliente, name='eliminar cliente'),
    path('editar_cliente/<nombre_cliente>', editar_cliente, name='editar cliente'),
    
    path('productos_lista/', ProductoListView.as_view(), name='productos lista'),
    path('producto_crear/', ProductoCreateView.as_view(), name='producto crear'),
    path('<pk>/eliminar/', ProductoDeleteView.as_view(), name='producto eliminar'),
    path('<pk>/editar/', ProductoUpdateView.as_view(), name='producto editar'),
    path('<pk>/detalle/', ProductoDetailView.as_view(), name='producto detalle'),
    
    path('empleados_lista/',EmpleadoListView.as_view(), name='empleados lista'),
    path('empleado_crear/', EmpleadoCreateView.as_view(), name='empleado crear'),
    path('<pk>/eliminar/',EmpleadoDeleteView.as_view(), name='empleado eliminar'),
    path('<pk>/editar/', EmpleadoUpdateView.as_view(), name='empleado editar'),
    path('<pk>/detalle/', EmpleadoDetailView.as_view(), name='empleado detalle'),
]  