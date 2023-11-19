from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    name = models.CharField( max_length=50 , verbose_name='Nombre')
    description = models.CharField(max_length=255 , verbose_name='Descripción')
    created_at = models.DateTimeField(auto_now_add=True , verbose_name='Creado el')

    class Meta:
        verbose_name='Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.name
    
class Centro(models.Model):

    name = models.CharField(max_length=150 , verbose_name='Nombre')
    address = models.CharField(max_length=100 , verbose_name="Dirección")
    number = models.IntegerField(verbose_name="Número de contacto")
    email = models.EmailField (verbose_name="Correo" , null=True)
    image = models.ImageField(default='null' , verbose_name="Imagen" , upload_to="centros")
    user = models.ForeignKey(User , verbose_name='Usuario' , on_delete=models.CASCADE)
    description = RichTextField(verbose_name="Descripcion" , null=True)
    categories = models.ManyToManyField(Category , verbose_name="Categorías" ,  blank = True , related_name="articles")
    created_at = models.DateTimeField(auto_now_add=True , verbose_name="Creado el")
    updated_at = models.DateTimeField(auto_now=True , verbose_name="Editado el")

    class Meta:
        verbose_name='Centro'
        verbose_name_plural = 'Centros'

    def __str__(self):
        return self.name
    

class ImagenCentro(models.Model):
    image = models.ImageField(upload_to="centrosImagen")
    centro = models.ForeignKey(Centro, on_delete=models.CASCADE , related_name="imagenes" , null="true")

   