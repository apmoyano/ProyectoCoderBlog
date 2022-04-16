from django.shortcuts import render, redirect
from django.template import Template, Context
from blog.forms import *
from blog.models import *

# Autenticacion django
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin  #esto lo puedo agregar a las clases y me va a solicitar hacer login para poder verla
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    
    if request.user.username:
        avatar = Avatar.objects.filter(user=request.user)

        if len(avatar) > 0:
            imagen = avatar[0].imagen.url
        else:
            imagen = None   
    else: 
        imagen = None        
        dict_ctx={"title":"Inicio","page":"Inicio","imagen_url":imagen}
    return render(request,'blog/index.html',dict_ctx)

#@login_required()
def viajes(request):
    viajes= Viajes.objects.all()
    if request.method == 'POST':
        form_viaje = ViajesFormulario(request.POST)
        
        if form_viaje.is_valid():
            data = form_viaje.cleaned_data
            viaje= Viajes(data['destino'],data['pais'],data['año'])
            viaje.save()

            form_viaje = ViajesFormulario()
            return redirect('inicio')
            #render(request, 'blog/viajes.html',{'viajes': viajes, "title": "Viajes", "page": "Viajes", "formulario": form_viaje})
            
    else:
        form_viaje = ViajesFormulario()

        return render(request, 'blog/viajes.html',{'viajes': viajes,'formulario':form_viaje})

#@login_required()
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



def login_request(request):

    if request.method == "POST":
        formulario = AuthenticationForm(request,data=request.POST)
        if formulario.is_valid():
            data= formulario.cleaned_data
            nombre_usuario=data.get('username')
            contraseña= data.get('password')
            

            usuario = authenticate(username=nombre_usuario,password=contraseña)

            if usuario is not None:
                login(request,usuario)
                dict_ctx={"title":"Inicio","page":usuario}
                return render(request,'blog/index.html',dict_ctx)

            else:
                dict_ctx={"title":"Inicio","page":usuario, "errors":["El usuario no existe"]}
                return render(request,'blog/index.html',dict_ctx)
        else:
            dict_ctx={"title":"Inicio","page":"anonymous", "errors":["Revise los datos indicados en el form"]}
            return render(request,'blog/index.html',dict_ctx)


    else:
        form = AuthenticationForm()
        return render(request,'blog/login.html',{"form":form})

def register_request(request):

    if request.method == "POST":

        form = UsuarioRegistroForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            form.save()
            dict_ctx={"title":"Inicio","page":usuario}

            return render(request,"blog/index.html",dict_ctx)
        else:

            dict_ctx={"title":"Inicio","page":"anonymous", "errors":["No paso validacion"]}
            return render(request,'blog/index.html',dict_ctx)
    else:
        form = UsuarioRegistroForm()
        return render(request,"blog/register.html",{"form":form})

#@login_required()
def editar_usuario(request):

    usuario = request.user

    if request.method == "POST":
        formulario = UsuarioEditForm(request.POST)

        if formulario.is_valid():
            data= formulario.cleaned_data
            
            usuario.first_name = data['first_name']
            usuario.last_name = data['last_name']
            usuario.email = data['email']
            usuario.password1 = data['password1']
            usuario.password2 = data['password2']

            usuario.save()

            return redirect("inicio")

        else:

            formulario = UsuarioEditForm(initial={'email':usuario.email})

            return render(request,"blog/editar_usuario.html",{"form":formulario,"errors":["Datos invalidos"]})

    else: 
        formulario = UsuarioEditForm()


    return render(request,"blog/editar_usuario.html",{"form":formulario})

@login_required()
def CargarImagen(request):

    if request.method == "POST":
        formulario = AvatarFormulario(request.POST,request.FILES)

        if formulario.is_valid():
            usuario= request.user

            avatar= Avatar.objects.filter(user=usuario)

            if len(avatar) > 0:
                avatar = avatar[0]
                avatar.imagen = formulario.cleaned_data["imagen"]
                avatar.save()

            else: 
                avatar = Avatar(user=usuario,imagen=formulario.cleaned_data["imagen"])
                avatar.save()

        return redirect("inicio")
    else:
        formulario = AvatarFormulario()
        return render(request,"blog/cargar_imagen.html",{"form":formulario})        


            