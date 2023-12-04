from django import forms 

#Formularios

class ProductoFormulario(forms.Form):
    nombre = forms.CharField (required=True)
    descripción = forms.CharField (required=True)
    precio = forms.IntegerField (required=True)
    cantidad_en_stock = forms.IntegerField (required=True)
    
class ClienteFormulario(forms.Form):
     nombre = forms.CharField(required=True)
     producto = forms.CharField(required=True)
     DNI = forms.IntegerField(required=True)
     email = forms.EmailField(required=True)
     
class EmpleadoFormulario(forms.Form):
     nombre = forms.CharField(required=True)
     cargo = forms.CharField(required=True)
     DNI = forms.IntegerField(required=True)    