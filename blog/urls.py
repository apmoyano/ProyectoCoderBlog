from django.urls import path
from django.views import *
from blog.views import *

from blog.views import Inicio

urlpatterns = [path('',Inicio, name= 'inicio'),
path('viajes/', ViajeView, name='viajes'),
path('buscarviaje/', buscar_viaje, name='buscar_viaje'),

path('comidas/', ComidasView, name='comidas'),
path('montanas/', MontanasView, name='montanas'),

]
