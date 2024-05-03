from django.db import models

## Criacao do Usuario
class Usuario(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=50)    
