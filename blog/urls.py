from django.urls import path
from blog.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [path('',index, name= 'inicio'),
path("pages/nuevo/",PostCrear.as_view() , name="post_create"),
path("pages/", PostList.as_view(), name="post_list"),
path("pages/<pk>/", PostDetalle.as_view(), name="post_detail"),
path("pages/editar/<pk>/", PostActualizar.as_view(), name="post_update"),
path("pages/borrar/<pk>/", PostBorrar.as_view(), name="post_delete"),
path("pages/upload_picture/<pk>",PictureUploadView,name='upload_picture'),
path("about/",sobre_mi,name="about_me"),
]
