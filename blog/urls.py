from django.urls import path
from blog.views import *


urlpatterns = [path('',index, name= 'inicio'),
path('viajes/', viajes, name='viajes'),
path('buscarviaje/', buscar_viaje, name='buscar_viaje'),

path('comidas/', comidas, name='comidas'),

path('montanas/', montanas, name='montanas'),
path('buscarmontana/', buscar_montana, name='buscar_montana'),
path('borrarviaje/<destino_id>/',borrarviaje,name='borrarviaje'),
path('updateviaje/<destino_id>/',actualizarviaje),

]
