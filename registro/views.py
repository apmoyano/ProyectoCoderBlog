from django.shortcuts import render, redirect
# Autenticacion django

from registro.forms import *




# Create your views here.




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

