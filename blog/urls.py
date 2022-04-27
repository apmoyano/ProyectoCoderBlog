from django.urls import path
from blog.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [path('',index, name= 'inicio'),
path("post/nuevo/",PostCrear.as_view() , name="post_create"),
path("pages/", PostList.as_view(), name="post_list"),
path("post/detalle/<pk>/", PostDetalle.as_view(), name="post_detail"),
path("post/editar/<pk>/", PostActualizar.as_view(), name="post_update"),
path("post/borrar/<pk>/", PostBorrar.as_view(), name="post_delete"),
path("post/upload_picture/",PictureUploadView,name='upload_picture'),
path("about_me/",sobre_mi,name="about_me"),
]
