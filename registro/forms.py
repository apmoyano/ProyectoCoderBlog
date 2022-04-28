from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UsuarioRegistroForm(UserCreationForm):
    email= forms.EmailField()
    password1=forms.CharField(label='Contraseña 1', widget=forms.PasswordInput)
    password2=forms.CharField(label='Contraseña 2', widget=forms.PasswordInput)
    
    class Meta:
        model= User
        fields=['username','email','password1','password2']
        help_text={k:"" for k in fields}