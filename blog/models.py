from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.urls import reverse

# Create your models here.

class Categoria(models.Model):
    nombre=models.CharField(max_length=255)

    def __str__(self):
        return self.nomnbre

class Post(models.Model):
    titulo= models.CharField(max_length=255)
    subtitulo= models.CharField(max_length=255)
    autor=models.ForeignKey(User,on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to='imagen_post', null= True, blank= True)
    body= RichTextField(blank=True , null=True)
    fecha_post=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo + '|' + str(self.autor)
    
  
  #Usuario

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null= True, blank= True)


#Viejos borrar

# class Viajes(models.Model):
#     destino = models.CharField(primary_key=True,max_length=100)
#     pais = models.CharField(max_length=100)
#     año = models.IntegerField()
#     post = RichTextField()

#     def __str__(self) -> str:
#         return f"{self.destino} - {self.pais} | {self. año}"


# class Comidas(models.Model):
   
#     nombre_comida = models.CharField(max_length=100)
#     pais_origen = models.CharField(max_length=100)
#     id = models.AutoField(primary_key=True)

#     def __str__(self) -> str:
#         return f"{self.nombre_comida} - {self.pais_origen}"


# class Montanas(models.Model):
#     nombre = models.CharField(max_length=100)
#     ubicacion = models.CharField(max_length=100)
#     dificultad= models.IntegerField()
#     id = models.AutoField(primary_key=True)
    
#     def __str__(self) -> str:
#         return f"{self.nombre} - {self.ubicacion} | Nvl de dificultad: {self.dificultad}"
