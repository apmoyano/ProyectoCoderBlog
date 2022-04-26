from django import forms


class PhotoUploadForm(forms.Form):
    picture = forms.ImageField()
    

