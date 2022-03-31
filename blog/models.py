from django.db import models

# Create your models here.


class Viajes(models.Model):
   
    destino = models.CharField( primary_key=True,max_length=100)
    pais = models.CharField(max_length=100)
    anio = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.destino} - {self.pais} | {self. año}"


class Comidas(models.Model):
   
    nombre_comida = models.CharField(max_length=100)
    pais_origen = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)

    def __str__(self) -> str:
        return f"{self.nombre_comida} - {self.pais_origen}"


class Montanas(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    dificultad= models.IntegerField()
    id = models.AutoField(primary_key=True)
    
    def __str__(self) -> str:
        return f"{self.nombre} - {self.ubicacion} - {self.pais}| {self.dificultad}"