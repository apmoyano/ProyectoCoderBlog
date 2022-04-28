from django.shortcuts import render, redirect
from blog.models    import Avatar
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate

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

        return render(request,'login/login.html',{"form":form,"imagen_url":imagen})