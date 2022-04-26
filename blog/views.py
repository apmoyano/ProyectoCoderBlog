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


class PostList(ListView):

    model = Post
    template_name = "blog/post_list.html"
    

class PostDetalle(DetailView):

    model = Post
    template_name = "blog/post_detalle.html"


class PostCrear(LoginRequiredMixin,CreateView):

    model = Post
    success_url = "/pages/"
    fields = ['titulo', 'subtitulo','picture','body']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class PostActualizar(LoginRequiredMixin,UpdateView):

    model = Post
    success_url = "/pages/"
    fields = ['titulo','subtitulo','picture','body']


class PostBorrar(LoginRequiredMixin,DeleteView):

    model = Post
    success_url = "/pages/"

