from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



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
