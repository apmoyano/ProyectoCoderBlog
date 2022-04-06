from django.shortcuts import render, HttpResponse
from django.template import Template, Context
from blog.forms import *
from blog.models import *

# Create your views here.

def index(request):

    return render(request,'blog/index.html')

def viajes(request):
    viajes= Viajes.objects.all()
    if request.method == 'POST':
        form_viaje = ViajesFormulario(request.POST)
        
        if form_viaje.is_valid():
            data = form_viaje.cleaned_data
            viaje= Viajes(data['destino'],data['pais'],data['año'])
            viaje.save()

            form_viaje = ViajesFormulario()
            return render(request, 'blog/viajes.html',{'viajes': viajes, "title": "Viajes", "page": "Viajes", "formulario": form_viaje})
            
    else:
        form_viaje = ViajesFormulario()

        return render(request, 'blog/viajes.html',{'viajes': viajes,'formulario':form_viaje})


def buscar_viaje(request):

    data = request.GET.get('destino', "")
    error = ""

    if data:
        try:
            viajes = Viajes.objects.get(destino=data)
            return render(request, 'blog/buscar_viaje.html', {"viajes": viajes, "id": data})

        except Exception as exc:
            print(exc)
            error = "No existe ese destino"
    return render(request, 'blog/buscar_viaje.html', {"error": error})


def comidas(request):
    comida= Comidas.objects.all()
    if request.method == 'POST':
        comida = ComidasFormulario(request.POST)
        
        if comida.is_valid():
            data = comida.cleaned_data
            comida_nuevo= Comidas(data['nombre_comida'],data['pais_origen'])
            comida_nuevo.save()

        
            return render(request, 'blog/comidas.html')
            
    else:
        comida_form = ComidasFormulario()

        return render(request, 'blog/comidas.html',{'formulario':comida_form})


def montanas(request):
    montanas= Montanas.objects.all()
    if request.method == 'POST':
        form_mont = MontanasFormulario(request.POST)
        
        if form_mont.is_valid():
            data = form_mont.cleaned_data
            montana= Montanas(data['nombre'],data['ubicacion'],data['dificultad'])
            montana.save()
            form_mont = MontanasFormulario()
        
            return render(request, 'blog/montanas.html',{'montanas': montanas, "title": "Montañas", "page": "Montañas", "formulario": form_mont})
            
    else:
        form_mont = MontanasFormulario()

        return render(request, 'blog/montanas.html',{'montanas': montanas,'formulario':form_mont})


def buscar_montana(request):

    data = request.GET.get('nombre', "")
    error = ""

    if data:
        try:
            montanas = Montanas.objects.get(nombre=data)
            return render(request, 'blog/buscar_montana.html', {"monatanas": montanas, "id": data})

        except Exception as exc:
            print(exc)
            error = "No existe ese destino"
    return render(request, 'blog/buscar_montana.html', {"error": error})



def borrarviaje(request, destino_id): #de la url viene un parametro que tiene que ser viaje_id
    
    try:
        destino= Viajes.objects.get(destino=destino_id)
        destino.delete()

        return render(request,"blog/index.html")

    except Exception as exc:
        return render(request,"blog/index.html")

def actualizarviaje(request,destino_id):
    viajes = Viajes.objects.get(destino=destino_id)

    if request.method == "POST":
        form_viaje = ViajesFormulario(request.POST)

        if form_viaje.is_valid():
            informacion = form_viaje.cleaned_data
            #viajes= Viajes(informacion['destino'],informacion['pais'],informacion['año'])

            viajes.destino = informacion["destino"]
            viajes.pais = informacion["pais"]
            viajes.año = informacion["año"]
            viajes.save()

            return render(request,'blog/index.html')

    else:
        form_viaje =ViajesFormulario(initial={"destino":viajes.destino,"pais":viajes.pais,"año":viajes.año})

        return render(request, 'blog/actualizar_viaje.html',{"formulario":form_viaje, "destino_id":destino_id})