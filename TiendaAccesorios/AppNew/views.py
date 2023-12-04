from django.shortcuts import render
from .models import *
from django.http import HttpResponse, HttpRequest
from .forms import ProductoFormulario, ClienteFormulario,EmpleadoFormulario

# Create your views here.

def inicio (request):
    return render(request, "inicio.html")

def lista_stock(req):
    lista = Producto.objects.all()
    return render(req, "lista_stock.html", {"lista_stock" : lista})


def buscarP(req):
    return render (req, "buscarP.html")

def producto_formulario(req :HttpRequest):
    print('method' , req.method)
    print('post', req.POST)

    if req.method == "POST":
        miformulario = ProductoFormulario(req.POST) 

        if miformulario.is_valid ():
            print (miformulario.cleaned_data)
            data = miformulario.cleaned_data
            stock= Producto (producto= data["producto"], cantidad=data["cantidad"] ,precio = data["precio"])
            stock.save()
            return render (req,"inicio.html",{"mensaje" : "Producto agregado al stock"})
        else : 
            return render (req, "inicio.html", {"mensaje" : "Formulario invalido"})
    else: 
        miformulario = ProductoFormulario()
        return render(req, "producto_formulario.html", {"miformulario": miformulario})

def busquedaproducto (req):
    return render(req,"busqueda.html")

def buscar (req):
     if req.GET["producto"]:
          productostock = req.GET["producto"]
        
          try: 
             producto =Producto.objects.get (producto=productostock)
             if producto.cantidad > 0 :
                return render (req,"resultado.html" , {"producto" : producto})
             else: 
                return render(req,"inicio.html" , {"mensaje" : "No hay Stock disponible"})
          
          except Producto.DoesNotExist:
             
              return render(req,"inicio.html" , {"mensaje" : "El producto no existe"})
                 

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


