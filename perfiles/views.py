from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from blog.models import Avatar
from perfiles.forms import *
# Create your views here.


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
            

            return render(request,"perfiles/editar_usuario.html",{"form":formulario,"errors":["Datos invalidos"]})
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
        

    return render(request,"perfiles/editar_usuario.html",{"form":formulario,"imagen_url":imagen})


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

        return render(request,"perfiles/cargar_imagen.html",{"form":formulario,"imagen_url":imagen})        


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
    return render(request,'perfiles/profile.html',dict_ctx)