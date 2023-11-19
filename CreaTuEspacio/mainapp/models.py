from django.db import models
from centrosmain.models import Centro

# Create your models here.
class usuariosCentro (models.Model):
    usuario = models.CharField(max_length=30)
    nombre = models.CharField(max_length=60)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    
