from django.urls import path
from registro.views import *
from django.contrib.auth.views import LogoutView
urlpatterns = [
path('signup/',register_request, name= 'register'),


]

