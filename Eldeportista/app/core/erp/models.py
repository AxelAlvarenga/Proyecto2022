from tabnanny import verbose
from django.db import models
from django.forms import model_to_dict
from crum import get_current_user
from core.models import BaseModel
from datetime import datetime

from app.settings import MEDIA_URL, STATIC_URL

# Create your models here.

class categoria(models.Model):
    name_cat = models.CharField(max_length=150, verbose_name='Nombre_cat', unique=True)


    def __str__(self):
        return self.name_cat
    
    

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']

class colores(models.Model):
    
    name_color = models.CharField(max_length=150, verbose_name='Nombre_color', unique=True)
    def __str__(self):
         return self.name_color


    def toJSON(self):
        item = model_to_dict(self)

        return item

    class Meta:
         verbose_name= 'color'
         verbose_name_plural='colores'
         ordering=['id']

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
    name = models.CharField(max_length=150, verbose_name='Nombre')
    talla = models.CharField(max_length=150, verbose_name='Talla')
    price = models.FloatField(max_length=150, verbose_name='Precio')
    cat = models.ForeignKey(categoria, on_delete=models.CASCADE, verbose_name='Categoría')
    cantidad=models.IntegerField(verbose_name='cantidad')
    
    def toJSON(self):
        item = model_to_dict(self)
        item['cat'] = self.cat.toJSON()
        return item

    def __str__(self):
         return self.name


    class Meta:
         verbose_name= 'Producto'
         verbose_name_plural='Productos'
         ordering=['id']

class cliente(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    correo = models.CharField(max_length=150, verbose_name='correo')
    telefono = models.CharField(max_length=150, verbose_name='telefono')
    Ruc = models.CharField(max_length=150, verbose_name='Ruc')

    def __str__(self):
         return self.name

    def toJSON(self):
        item = model_to_dict(self)
        return item     

    class Meta:
         verbose_name= 'Cliente'
         verbose_name_plural='Clientes'
         ordering=['id']

class Sale(models.Model):
    cli = models.ForeignKey(cliente, on_delete=models.CASCADE)
    date_joined = models.DateField(default=datetime.now)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    iva = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.cli.name

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ['id']


class DetSale(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    prod = models.ForeignKey(producto, on_delete=models.CASCADE)
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    cant = models.IntegerField(default=0)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.prod.name

    class Meta:
        verbose_name = 'Detalle de Venta'
        verbose_name_plural = 'Detalle de Ventas'
        ordering = ['id']

    






    
