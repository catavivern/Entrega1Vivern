from django.urls import path
from .views import *

urlpatterns = [
    path("selecciones/", selecciones, name="selecciones"), #hice un for de todas las selecciones de mi db
    path("dts/", dts, name="dts"), # "
    path("jugadores/", jugadores, name="jugadores"), # "
    path("", inicio, name="inicio"),

    path("seleccionFormulario/", seleccionFormulario, name="seleccionFormulario"),
    path("dtFormulario/", dtFormulario, name="dtFormulario"),
    path("jugadorFormulario/", jugadorFormulario, name="jugadorFormulario"),

    path("busquedaSeleccion/", busquedaSeleccion, name="busquedaSeleccion"),
    path("buscar/", buscar, name="buscar"),
]

