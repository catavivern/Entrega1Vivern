from django import forms

class SeleccionForm(forms.Form):
    pais=forms.CharField(label="País", max_length=50)
    copasGanadas=forms.IntegerField(label="Copas del mundo ganadas")

class DTForm(forms.Form):
    nombre= forms.CharField(label="Nombre de DT", max_length=50)
    apellido= forms.CharField(label="Apellido de DT", max_length=50)
    clubActual= forms.CharField(label="Club actual de DT", max_length=50)
    email= forms.EmailField(label="Email de DT")
    nacimiento=forms.DateField(label="Fecha de nacimiento de DT")
    pais=forms.CharField(label="País de DT", max_length=50)

class JugadorForm(forms.Form):
    nombre= forms.CharField(label="Nombre de jugador", max_length=50)
    apellido= forms.CharField(label="Apellido de jugador", max_length=50)
    clubActual= forms.CharField(label="Club actual de jugador", max_length=50)
    email= forms.EmailField(label="Email de jugador")
    nacimiento=forms.DateField(label="Fecha de nacimiento de jugador")
    pais=forms.CharField(label="País de jugador", max_length=50)
    posicion=forms.CharField(label="Posición de jugador", max_length=50)
    numero=forms.IntegerField(label="Número de jugador")