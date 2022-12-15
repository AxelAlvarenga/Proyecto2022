from tabnanny import verbose
from django.db import models
from django.forms import model_to_dict
from crum import get_current_user
from core.models import BaseModel

from app.settings import MEDIA_URL, STATIC_URL

# Create your models here.

class categoria(BaseModel):
    name_cat = models.CharField(max_length=150, verbose_name='Nombre_cat', unique=True)

    def __str__(self):
        return self.name_cat
    
    def save(self, force_insert=False, force_update=False,using=None,update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.user_creation = user
            else:
                self.user_update = user
        super(categoria,self).save()

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


    






    
