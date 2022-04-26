from django.shortcuts import render, redirect
# Autenticacion django
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from blog.models import Avatar
from registro.forms import *




# Create your views here.


def login_request(request):
     #Avatar
    if request.user.username:
                    
        avatar = Avatar.objects.filter(user=request.user)

        if len(avatar) > 0:
            imagen = avatar[0].imagen.url
        else:
            imagen = None   
    else: 
        imagen = None        
    #Avatar          

    if request.method == "POST":
        formulario = AuthenticationForm(request,data=request.POST)
        if formulario.is_valid():
            data= formulario.cleaned_data
            nombre_usuario=data.get('username')
            contraseña= data.get('password')
            

            usuario = authenticate(username=nombre_usuario,password=contraseña)

            if usuario is not None:
                login(request,usuario)
                
                return redirect('inicio')

            else:
                dict_ctx={"title":"Inicio","page":usuario, "errors":["El usuario no existe"],"imagen_url":imagen}
                return render(request,'blog/index.html',dict_ctx)
        else:
            dict_ctx={"title":"Inicio","page":"anonymous", "errors":["Revise los datos indicados en el formulario"],"imagen_url":imagen}
            return render(request,'blog/index.html',dict_ctx)

    else:
        form = AuthenticationForm()

        return render(request,'registro/login.html',{"form":form,"imagen_url":imagen})

def register_request(request):

    if request.method == "POST":

        form = UsuarioRegistroForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            form.save()
            dict_ctx={"title":"Inicio","page":usuario}

            return redirect("login")
        else:

            dict_ctx={"title":"Inicio","page":"anonymous", "errors":["Vuelva a intentar"]}
            return render(request,'blog/index.html',dict_ctx)
    else:
        form = UsuarioRegistroForm()
        return render(request,"registro/register.html",{"form":form})

@login_required()
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
            

            return render(request,"registro/editar_usuario.html",{"form":formulario,"errors":["Datos invalidos"]})
    else: 
        formulario = UsuarioEditForm()
        #Avatar
        if request.user.username:
            
            avatar = Avatar.objects.filter(user=request.user)

            if len(avatar) > 0:
                imagen = avatar[0].imagen.url
            else:
                imagen = None   
        else: 
            imagen = None        
        #Avatar
        

    return render(request,"registro/editar_usuario.html",{"form":formulario,"imagen_url":imagen})


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
        #Avatar
        if request.user.username:
            
            avatar = Avatar.objects.filter(user=request.user)

            if len(avatar) > 0:
                imagen = avatar[0].imagen.url
            else:
                imagen = None   
        else: 
            imagen = None        
        #Avatar

        return render(request,"registro/cargar_imagen.html",{"form":formulario,"imagen_url":imagen})        


@login_required()
def ProfileView(request):

    if request.user.username:
        avatar = Avatar.objects.filter(user=request.user)

        if len(avatar) > 0:
            imagen = avatar[0].imagen.url
        else:
            imagen = None   
    else: 
        imagen = None        
    dict_ctx={"title":"Inicio","page":"Inicio","imagen_url":imagen}
    return render(request,'registro/profile.html',dict_ctx)


def editar_password(request):
    pass