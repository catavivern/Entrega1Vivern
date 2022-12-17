from django.shortcuts import render
from .models import Seleccion, DT, Jugador
from django.http import HttpResponse

from django.urls import reverse_lazy

from AppEquipos.forms import SeleccionForm, DTForm, JugadorForm

# Create your views here.

#views de las templates para ver los objetos

def inicio(request):
    return render (request, "AppEquipos/inicio.html")

def selecciones(request):
    return render (request, "AppEquipos/selecciones.html")

def dts(request):
    return render (request, "AppEquipos/dts.html")

def jugadores(request):
    return render (request, "AppEquipos/jugadores.html")

#views para leer los objetos de las clases. (?)Despues me va a servir para los for de las templates

def leerSelecciones(request):
    selecciones=Seleccion.objects.all()
    return render(request, "AppEquipos/selecciones.html", {"selecciones":selecciones})

def leerDts(request):
    dts=DT.objects.all()
    return(request, "AppEquipos/dts.html", {"dts":dts})

def leerJugadores(request):
    jugadores=Jugador.objects.all()
    return render( request, "AppEquipos/jugadores.html", {"jugadores":jugadores })

#views de las templates para agregar objetos de cada uno

def seleccionFormulario(request):
    if request.method=="POST":
            form= SeleccionForm(request.POST)
            print("-------------------------------")  #esto despues lo tengo que SACAR
            print(form)
            print("-------------------------------")
            if form.is_valid():
                informacion=form.cleaned_data #convierte de la info en modo formulario a un diccionario
                print(informacion)
                pais= informacion["pais"]
                copasGanadas=informacion["copasGanadas"]
                seleccion= Seleccion(pais=pais, copasGanadas=copasGanadas)
                seleccion.save()
                return render(request, "AppEquipos/inicio.html" ,{"mensaje": "Seleccion guardada correctamente"})
            else:
                return render(request, "AppEquipos/seleccionFormulario.html" ,{"form": form, "mensaje": "Informacion no válida"})
            
    else:
        formulario= SeleccionForm()
        return render (request, "AppEquipos/seleccionFormulario.html", {"form": formulario})

def dtFormulario(request):
    if request.method=="POST":
        form= DTForm(request.POST)
        print("-------------------------------")  #esto despues lo tengo que SACAR
        print(form)
        print("-------------------------------")
        if form.is_valid():
            informacion=form.cleaned_data #convierte de la info en modo formulario a un diccionario
            print(informacion)
            nombre=informacion["nombre"]
            apellido=informacion["apellido"]
            clubActual=informacion["clubActual"]
            email=informacion["email"]
            nacimiento=informacion["nacimiento"]
            pais=informacion["pais"]
            
            dt= DT(nombre=nombre, apellido=apellido, clubActual=clubActual, email=email, nacimiento=nacimiento, pais=pais,  )
            dt.save()
            return render(request, "AppEquipos/inicio.html" ,{"mensaje": "DT guardado correctamente"})
        else:
            return render(request, "AppEquipos/dtFormulario.html" ,{"form": form, "mensaje": "Informacion no válida"})
            
    else:
        formulario= DTForm()
        return render (request, "AppEquipos/dtFormulario.html", {"form": formulario})

def jugadorFormulario(request):
    if request.method=="POST":
        form= DTForm(request.POST)
        print("-------------------------------")  #esto despues lo tengo que SACAR
        print(form)
        print("-------------------------------")
        if form.is_valid():
            informacion=form.cleaned_data #convierte de la info en modo formulario a un diccionario
            print(informacion)
            nombre=informacion["nombre"]
            apellido=informacion["apellido"]
            clubActual=informacion["clubActual"]
            email=informacion["email"]
            nacimiento=informacion["nacimiento"]
            pais=informacion["pais"]
            posicion=informacion["posicion"]
            numero=informacion["numero"]
            jugador= Jugador(nombre=nombre, apellido=apellido, clubActual=clubActual, email=email, nacimiento=nacimiento, pais=pais, posicion=posicion, numero=numero)
            jugador.save()
            return render(request, "AppEquipos/inicio.html" ,{"mensaje": "Jugador guardado correctamente"})
        else:
            return render(request, "AppEquipos/jugadorFormulario.html" ,{"form": form, "mensaje": "Informacion no válida"})
            
    else:
        formulario= JugadorForm()
        return render (request, "AppEquipos/jugadorFormulario.html", {"form": formulario})

#view q busque las selecciones que tengan determinada cantidad de copas ganadas

def busquedaSeleccion(request):
    return render(request, "AppEquipos/busquedaSeleccion.html")

def buscar(request):
    
    copasGanadas= request.GET["copasGanadas"]
    if copasGanadas!="":
        selecciones= Seleccion.objects.filter(copasGanadas__icontains=copasGanadas)
        return render(request, "AppEquipos/resultadosBusqueda.html", {"selecciones": selecciones})
    else:
        return render(request, "AppEquipos/busquedaSeleccion.html", {"mensaje": "Ingrese una cantidad de copas para buscar las selecciones"})


