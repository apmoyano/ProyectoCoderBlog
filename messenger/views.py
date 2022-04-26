
from .models import Message
from django.views.generic.edit import CreateView,DeleteView
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin  #esto lo puedo agregar a las clases y me va a solicitar hacer login para poder verla


# Create your views here.


class MensajeList(ListView):

    model =  Message
    template_name = "messenger/message_list.html"

class CrearMenssage(LoginRequiredMixin,CreateView):

    model = Message
    success_url = "/messenger/"
    fields = ['emisor','receptor', 'titulo','cuerpo']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class DetalleMensaje(DetailView):

    model = Message
    template_name = "messenger/message_detalle.html"

class BorrarMensaje(LoginRequiredMixin,DeleteView):

    model = Message
    success_url = "/messenger/"




