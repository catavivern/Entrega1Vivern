from django.db import models

# Create your models here.

class Seleccion(models.Model):
    pais=models.CharField(max_length=50)
    copasGanadas=models.IntegerField()
    def __str__(self):
        return f"{self.pais}"
        
class DT(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    clubActual= models.CharField(max_length=50)
    email=models.EmailField()
    nacimiento=models.DateField()
    pais=models.CharField(max_length=50)
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Jugador(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    clubActual= models.CharField(max_length=50)
    email=models.EmailField()
    nacimiento=models.DateField()
    pais=models.CharField(max_length=50)
    posicion=models.CharField(max_length=50)
    numero=models.IntegerField()
    def __str__(self):
        return f"{self.nombre} {self.apellido}"