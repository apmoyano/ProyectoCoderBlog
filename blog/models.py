from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.urls import reverse

# Create your models here.

# class Categoria(models.Model):
#     nombre=models.CharField(max_length=255)

#     def __str__(self):
#         return self.nomnbre

class Post(models.Model):
    picture=models.ImageField(upload_to='imagen_post', null= True, blank= True)
    titulo= models.CharField(max_length=255)
    subtitulo= models.CharField(max_length=255)
    autor=models.ForeignKey(User,on_delete=models.CASCADE)
    body= RichTextField(blank=True , null=True)
    fecha_post=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo + '|' + str(self.autor)


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', default='blog/assets/default.png', null= True, blank= True, )

