from django.shortcuts import render, redirect
from .models import *
from django.http import HttpRequest
from .forms import ProductoFormulario, ClienteFormulario,EmpleadoFormulario
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy


# Create your views here.

def inicio (request):
    return render(request, "inicio.html")

@login_required(login_url="login")
def crear_producto(request): 
    print("Mostrar request.post:")
    print(request.POST)
    
    if request.method == "POST":
        nuevo_producto = Producto(
            nombre = request.POST["nombre"],
            descripcion = request.POST["descripcion"],
            cantidad_en_stock = request.POST["cantidad_en_stock"]
        )
        nuevo_producto.save()
        return render(request, "inicio.html")
    
    return render(request, 'producto_formulario.html')

def lista_stock(req):
    lista = Producto.objects.all()
    return render(req, "lista_stock.html", {"lista_stock" : lista})

def busquedaproducto (req):
    return render(req,"busqueda.html")

def buscarP(req):
    return render (req, "busqueda.html")

def producto_formulario(req :HttpRequest):
    print('method' , req.method)
    print('post', req.POST)

    if req.method == "POST":
        miformulario = ProductoFormulario(req.POST) 

        if miformulario.is_valid ():
            print (miformulario.cleaned_data)
            data = miformulario.cleaned_data
            stock= Stock(producto= data["producto"], cantidad=data["cantidad"] ,precio = data["precio"])
            stock.save()
            return render (req,"inicio.html",{"mensaje" : "Producto agregado al stock"})
        else : 
            return render (req, "inicio.html", {"mensaje" : "Formulario invalido"})
    else: 
        miformulario = ProductoFormulario()
        return render(req, "producto_formulario.html", {"miformulario": miformulario})
           

def cliente (request):
  if request.method == "POST":
        miformularioc = ClienteFormulario(request.POST) 

        if miformularioc.is_valid ():
            print (miformularioc.cleaned_data)
            data = miformularioc.cleaned_data
            cliente= Cliente(nombre= data["nombre"], producto=data["producto"], DNI = data["DNI"], email = data ["email"] )
            cliente.save()
            return render (request,"inicio.html",{"mensaje" : "El Cliente ha realizado su compra."})
        else : 
            return render (request, "inicio.html", {"mensaje" : "Formulario invalido"})
  else: 
        miformularioc = ClienteFormulario()
        return render(request, "cliente.html", {"miformularioc": miformularioc})
    
def empleado (request):
     if request.method == "POST":
        miformularioE = EmpleadoFormulario(request.POST) 

        if miformularioE.is_valid ():
            print (miformularioE.cleaned_data)
            data = miformularioE.cleaned_data
            empleado= Empleado(nombre= data["nombre"], cargo=data["cargo"], DNI = data["DNI"])
            empleado.save()
            return render (request,"inicio.html",{"mensaje" : "¡El Empleado ha sido registrado!"})
        else : 
            return render (request, "inicio.html", {"mensaje" : "Formulario inválido"})
     else: 
        miformularioE = EmpleadoFormulario()
        return render(request, "empleado.html", {"miformularioE": miformularioE})
    
    # CRUD CLIENTES #
    
def crear_cliente(request):
    if request.method == "POST":
        mi_formulario = ClienteFormulario(request.POST) 
        
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            cliente = Cliente (
                nombre=informacion["nombre"],
                producto =informacion["producto"],
                dni=informacion["dni"],
                email=informacion["email"]
                )
            cliente.save()
            return render(request, "inicio.html")
        else:
            return render(request, 'Appnew/crear_cliente.html', {"errors": mi_formulario.errors})
    else:
        mi_formulario = ClienteFormulario()
        return render(request, "AppNew/crear_cliente.html", {"mi_formulario": mi_formulario})
    
def leer_clientes(request):
    lista_clientes = Cliente.objects.all()
    return render(request, "AppNew/leer_clientes.html", {"clientes": lista_clientes})

def eliminar_cliente(request, nombre_cliente):
    cliente = Cliente.objects.get(nombre=nombre_cliente)
    cliente.delete()
    return redirect ('leer clientes')

def editar_cliente(request, nombre_cliente):
    cliente = Cliente.objects.get(nombre=nombre_cliente)
    
    if request.method == "POST":
        mi_formulario = ClienteFormulario(request.POST) 

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            cliente.nombre = informacion['nombre']
            cliente.producto = informacion ['producto']
            cliente.DNI = informacion['DNI']
            cliente.email = informacion['email']
            cliente.save()
            return render(request, "inicio.html")
    else:
        mi_formulario = ClienteFormulario()
        return render(request, "AppNew/editar_cliente.html", {"mi_formulario": mi_formulario})
    
    # CRUD PRODUCTOS #
    
class ProductoListView(ListView):
     model = Producto
     context_object_name = "productos"
     template_name = "AppNew/productos_lista.html"
     
class ProductoDetailView(DetailView):
    model = Producto
    template_name = "AppNew/producto_detalle.html"
    success_url = reverse_lazy("productos lista")
    template_name = "AppNew/productos_lista.html"

class ProductoCreateView(CreateView):
    model = Producto
    template_name = "AppNew/producto_crear.html"
    success_url = reverse_lazy('productos lista')
    fields = ['nombre', 'descripcion', 'precio', 'cantidad']
    
class ProductoUpdateView(UpdateView):
    model = Producto
    template_name = "AppNew/producto_editar.html"
    success_url = reverse_lazy("productos lista")
    fields = ['nombre', 'descripcion', 'precio', 'cantidad']
    
class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = "AppNew/producto_eliminar.html"
    success_url = reverse_lazy("ventas lista")
    
# CRUD EMPLEADOS #

class EmpleadoListView(ListView):
     model = Empleado
     context_object_name = "empleados"
     template_name = "AppNew/empleados_lista.html"
     
class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "AppNew/empleado_detalle.html"
    success_url = reverse_lazy("empleados lista")
    template_name = "AppNew/empleados_lista.html"

class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "AppNew/empleado_crear.html"
    success_url = reverse_lazy('empleados lista')
    fields = ['nombre', 'descripcion', 'precio', 'cantidad']
    
class EmpleadoUpdateView(UpdateView):
    model = Producto
    template_name = "AppNew/empleado_editar.html"
    success_url = reverse_lazy ('empleados lista')
    fields = ['nombre', 'cargo', 'DNI']
    
class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "AppNew/empleado_eliminar.html"
    success_url = reverse_lazy("empleados lista")




