from tabnanny import verbose
from django.db import models

# Create your models here.

class empleado(models.Model):
    ci= models.CharField(max_length=150, verbose_name='ci')
    nombre= models.CharField(max_length=20, verbose_name='nombre')
    
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'empleado'
        verbose_name_plural = 'empleados'
        db_table='empleado'
        ordering=['id']


class producto(models.Model):
    name = models.CharField(max_length=150,verbose_name='Nombre')
    color = models.CharField(max_length=150,verbose_name='Color')
    talla = models.CharField(max_length=150,verbose_name='Talla')
    price = models.FloatField(max_length=150,verbose_name='Precio')
    def __str__(self):
         return self.name

    class Meta:
         verbose_name= 'Producto'
         verbose_name_plural='Productos'
         ordering=['id']

class cliente(models.Model):
    name = models.CharField(max_length=150,verbose_name='Nombre')
    correo = models.CharField(max_length=150,verbose_name='correo')
    telefono = models.CharField(max_length=150,verbose_name='telefono')
    cedula = models.IntegerField(verbose_name='cedula')
    def __str__(self):
         return self.name

    class Meta:
         verbose_name= 'Cliente'
         verbose_name_plural='Clientes'
         ordering=['id']
    






    
