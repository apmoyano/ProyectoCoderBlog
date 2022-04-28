from django.urls import path
from login.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [path('login/',login_request, name= 'login'),
path('logout/',LogoutView.as_view(template_name="login/logout.html"), name= 'logout'),
]
