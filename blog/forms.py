from django import forms

class ViajesFormulario(forms.Form):

    destino = forms.CharField()
    pais= forms.CharField()
    anio= forms.IntegerField()

class ComidasFormulario(forms.Form):

    nombre_comida = forms.CharField(max_length=100)
    pais_origen = forms.CharField(max_length=100)
    
class MontanasFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    ubicacion = forms.CharField(max_length=100)
    dificultad= forms.IntegerField()