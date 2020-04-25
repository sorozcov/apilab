from django.db import models
from django.contrib.auth.models import User


#Clase Parent que tiene una relacion uno a uno con un usuario de Django
class Parent(models.Model):
    name = models.CharField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
   


    
