from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Message(models.Model):
    emisor=models.ForeignKey(User,on_delete=models.CASCADE, related_name='emisor')
    receptor=models.ForeignKey(User,on_delete=models.CASCADE, related_name='receptor')
    titulo=models.CharField(max_length=255)
    cuerpo=models.TextField()
    fecha=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.emisor}\ mensaje para {self.receptor}' 




