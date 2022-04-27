from pyexpat import model
from django.shortcuts import render, redirect
from blog.forms import *
from blog.models import *
from blog.models import Avatar
#Vistas basadas en clases
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Autenticacion django

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

def sobre_mi(request):
    if request.user.username:
        avatar = Avatar.objects.filter(user=request.user)

        if len(avatar) > 0:
            imagen = avatar[0].imagen.url
        else:
            imagen = None   
    else: 
        imagen = None
    dict_ctx={"title":"Inicio","page":"Inicio","imagen_url":imagen}

    return render(request, "blog/about_me.html",{"imagen_url":imagen})


class PostList(ListView):

    model = Post
    template_name = "blog/post_list.html"
    

class PostDetalle(DetailView):

    model = Post
    template_name = "blog/post_detalle.html"


class PostCrear(LoginRequiredMixin,CreateView):

    model = Post
    success_url = "/post/upload_picture/"
    fields = ['titulo', 'subtitulo','body']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class PostActualizar(LoginRequiredMixin,UpdateView):

    model = Post
    success_url = "/pages/"
    fields = ['titulo','subtitulo','body']
    template_name = "blog/update_post.html"


class PostBorrar(LoginRequiredMixin,DeleteView):

    model = Post
    success_url = "/pages/"


def PictureUploadView(request):

    if request.user.username:
        avatar = Avatar.objects.filter(user=request.user)

        if len(avatar) > 0:
            imagen = avatar[0].imagen.url
        else:
            imagen = None   
    else: 
        imagen = None
    dict_ctx={"title":"Inicio","page":"Inicio","imagen_url":imagen}

    if request.method == "POST":

        formulario = PhotoUploadForm(request.POST,request.FILES)

        if formulario.is_valid():

            usuario = request.user

            imagen_post=Post.objects.filter(autor=usuario)

            if len(imagen_post) > 0:
                imagen_post = imagen_post[0]
                imagen_post.picture = formulario.cleaned_data['picture']
                imagen_post.save()
            else:
                imagen_post = Post(autor = usuario, picture = formulario.cleaned_data['picture'])
                imagen_post.save()

        return redirect('post_list')
    else:
        formulario = PhotoUploadForm()
        return render(request, 'blog/upload_picture.html', {"form":formulario,"imagen_url":imagen })
