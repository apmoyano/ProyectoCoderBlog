from django.shortcuts import render
from blog.forms import *
from blog.models import *

# Create your views here.

def Inicio(request):
    return render(request,'blog/index.html')

def ViajeView(request):
    viaje= Viajes.objects.all()
    if request.method == 'POST':
        viaje = ViajesFormulario(request.POST)
        
        if viaje.is_valid():
            data = viaje.cleaned_data
            viaje_nuevo= Viajes(data['destino'],data['pais'],data['anio'])
            viaje_nuevo.save()

        
            return render(request, 'blog/viajes.html')
            
    else:
        viaje_form = ViajesFormulario()

        return render(request, 'blog/viajes.html',{'formulario':viaje_form})


def buscar_viaje(request):

    data = request.GET.get('destino', "")
    error = ""

    if data:
        try:
            viaje = Viajes.objects.get(destino=data)
            return render(request, 'blog/buscar_viaje.html', {"viaje": viaje, "id": data})

        except Exception as exc:
            print(exc)
            error = "No existe ese destino"
    return render(request, 'blog/buscar_viaje.html', {"error": error})


def ComidasView(request):
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


def MontanasView(request):
    montanas= Montanas.objects.all()
    if request.method == 'POST':
        montanas = MontanasFormulario(request.POST)
        
        if montanas.is_valid():
            data = montanas.cleaned_data
            montana= Montanas(data['nombre'],data['ubicacion'],data['dificultad'])
            montana.save()

        
            return render(request, 'blog/montanas.html')
            
    else:
        montana_form = MontanasFormulario()

        return render(request, 'blog/montanas.html',{'formulario':montana_form})