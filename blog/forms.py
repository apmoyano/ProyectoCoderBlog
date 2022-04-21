from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin



class UsuarioRegistroForm(UserCreationForm):
    email= forms.EmailField()
    password1=forms.CharField(label='Contraseña 1', widget=forms.PasswordInput)
    password2=forms.CharField(label='Contraseña 2', widget=forms.PasswordInput)
    
    class Meta:
        model= User
        fields=['username','email','password1','password2']
        help_text={k:"" for k in fields}



class UsuarioEditForm(UserCreationForm):
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    email= forms.EmailField(label="Modificar e-mail")
    password1=forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2=forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model= User
        fields=['first_name','last_name','email','password1','password2']
        help_text={k:"" for k in fields}


class AvatarFormulario(forms.Form):
    imagen = forms.ImageField()


