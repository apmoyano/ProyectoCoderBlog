from django.urls import path
from blog.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [path('',index, name= 'inicio'),
path('login/',login_request, name= 'login'),
path('register/',register_request, name= 'register'),
path('logout/',LogoutView.as_view(template_name="blog/logout.html"), name= 'logout'),
path("profile/editar_usuario",editar_usuario,name="editar_usuario"),

path("profile/",ProfileView, name="profile"),
path("profile/cargar_imagen",CargarImagen,name="cargar_imagen"),
path("post/nuevo/", PostCrear.as_view(), name="post_create"),
path("post/list/", PostList.as_view(), name="post_list"),
path("post/detalle/<pk>/", PostDetalle.as_view(), name="post_detail"),

# path('viajes/', viajes, name='viajes'),
# path('buscarviaje/', buscar_viaje, name='buscar_viaje'),

# path('comidas/', comidas, name='comidas'),
# path('montanas/', montanas, name='montanas'),
# path('buscarmontana/', buscar_montana, name='buscar_montana'),

# path('borrarviaje/<destino_id>/',borrarviaje,name='borrarviaje'),
# path('updateviaje/<destino_id>/',actualizarviaje),





]
