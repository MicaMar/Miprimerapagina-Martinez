from django.contrib import admin

# Register your models here.

from AppNew.models import Producto, Cliente, Empleado

admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Empleado)
