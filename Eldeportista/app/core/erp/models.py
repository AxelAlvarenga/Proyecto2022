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
    name = models.CharField(max_length=150,verbose_name='Nombre',unique=True)
    color = models.CharField(max_length=150,verbose_name='Color',unique=True)
    talla = models.CharField(max_length=150,verbose_name='Talla',unique=True)
    price = models.FloatField(max_length=150,verbose_name='Precio',unique=True)
    def __str__(self):
         return self.name

    class Meta:
         verbose_name= 'Producto'
         verbose_name_plural='Productos'
         ordering=['id']
    






    
