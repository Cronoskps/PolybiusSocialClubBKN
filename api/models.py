from django.db import models

# Create your models here.

class Game(models.Model):
    
    # id_game = models.BigAutoField(auto_created=True, primary_key=True, max_length=6, verbose_name='Id Game')
    title = models.CharField(max_length=80, verbose_name='Titulo')
    release_date = models.DateField(null=True, verbose_name='Fecha de lanzamiento')
    developer = models.CharField(max_length=50, null=True, blank=True, verbose_name='Desarollador')
    banner = models.ImageField(upload_to='imagenes/', null=True, blank=True,  verbose_name="Portada")

    def __str__(self):
        return self.title
    
# class Review(models.Model):
#     pass