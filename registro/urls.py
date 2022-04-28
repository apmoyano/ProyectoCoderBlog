from django.urls import path
from registro.views import *
from django.contrib.auth.views import LogoutView
urlpatterns = [
path('register/',register_request, name= 'register'),


]

