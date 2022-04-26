from django.urls import path
from registro.views import *
from django.contrib.auth.views import LogoutView
urlpatterns = [path('login/',login_request, name= 'login'),
path('register/',register_request, name= 'register'),
path('logout/',LogoutView.as_view(template_name="registro/logout.html"), name= 'logout'),
path("profile/editar_usuario",editar_usuario,name="editar_usuario"),
path("profile/",ProfileView, name="profile"),
path("profile/cargar_imagen",CargarImagen,name="cargar_imagen"),  
]

