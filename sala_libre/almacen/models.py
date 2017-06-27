from django.db import models

class Laboratorio(models.Model):
	n=models.IntegerField()
	dia=models.IntegerField()
	hora=models.IntegerField()
	libre=models.BooleanField()
	clases=models.CharField(max_length=50)

	def __str__(self):
		return str(self.n)

# Create your models here.
class App(models.Model):
	hoy=models.BooleanField()
	dia=models.IntegerField()
	hora=models.IntegerField()

	def __str__(self):
		return "hola"