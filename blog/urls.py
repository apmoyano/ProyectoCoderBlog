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

path("post/nuevo/",PostCrear.as_view() , name="post_create"),
path("pages/", PostList.as_view(), name="post_list"),
path("post/detalle/<pk>/", PostDetalle.as_view(), name="post_detail"),
path("post/editar/<pk>/", PostActualizar.as_view(), name="post_update"),
path("post/borrar/<pk>/", PostBorrar.as_view(), name="post_delete"),
]
