from django.urls import path
from perfiles.views import *

urlpatterns = [path("profile/editar_usuario",editar_usuario,name="editar_usuario"),
path("profile/",ProfileView, name="profile"),
path("profile/cargar_imagen",CargarImagen,name="cargar_imagen"),  
    
]

