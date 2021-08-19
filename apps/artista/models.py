from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Genero (models.Model):
	nombre  = models.CharField(max_length=500)

	def __str__ (self):
		return self.nombre

class Musica (models.Model):
	nombre  = models.CharField(max_length=500)
	archivo = models.FileField(upload_to = 'musica', null=True, blank=True)
	foto    = models.ImageField(upload_to= 'fotos', null= True, blank= True)
	artista = models.ForeignKey(User, on_delete = models.PROTECT)
	generos = models.ManyToManyField(Genero, null=True, blank=True) 

	def __str__ (self):
		return self.nombre



