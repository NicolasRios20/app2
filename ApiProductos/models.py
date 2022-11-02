from distutils.command.upload import upload
from django.db import models

class Producto(models.Model):
  nombre=models.CharField(max_length=20)
  precio=models.FloatField()
  descripcion=models.TextField(max_length=200)
  stock=models.IntegerField()
  marca=models.CharField(max_length=100)
  modelo=models.CharField(max_length=100)
  fechaVenta=models.DateField(auto_now_add=True)
  horaVenta=models.TimeField(auto_now_add=True)
  iva=models.DecimalField(max_digits=5, decimal_places=2)
  imagen=models.ImageField(upload_to='files/covers')
