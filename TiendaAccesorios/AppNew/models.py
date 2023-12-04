from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.IntegerField ()
    cantidad_en_stock = models.IntegerField()
    
    
class Cliente (models.Model):
    nombre = models.CharField(max_length=50)
    producto = models.CharField(max_length=50)
    DNI = models.IntegerField()
    email = models.EmailField()
    
       
    def __str__(self):
        return self.nombre + ", DNI: " + str(self.DNI)


class Empleado (models.Model):
    nombre = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)
    DNI = models.IntegerField()

   
    def __str__(self):
        return self.nombre + ", DNI: " + str(self.DNI)