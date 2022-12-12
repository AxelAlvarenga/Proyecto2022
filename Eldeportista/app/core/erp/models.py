from tabnanny import verbose
from django.db import models

from app.settings import MEDIA_URL, STATIC_URL

# Create your models here.

class categoria(models.Model):
    name_cat = models.CharField(max_length=150, verbose_name='Nombre_cat', unique=True)

    def __str__(self):
         return self.name_cat

    class Meta:
         verbose_name= 'Categoria'
         verbose_name_plural='Categorias'
         ordering=['id']

class color(models.Model):
    name_color = models.CharField(max_length=150, verbose_name='Nombre_color', unique=True)
    image_color= models.ImageField(upload_to='product/%Y/%m/%d', null=True,blank=True )
    def __str__(self):
         return self.name_color
    def get_image(self):
        if self.image_color:
            return '{}{}'.format(MEDIA_URL, self.image_color)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')
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
    color = models.ForeignKey(color, on_delete=models.CASCADE, verbose_name='color')
    talla = models.CharField(max_length=150, verbose_name='Talla')
    price = models.FloatField(max_length=150, verbose_name='Precio')
    cat = models.ForeignKey(categoria, on_delete=models.CASCADE, verbose_name='Categoría')
    cantidad=models.IntegerField(verbose_name='cantidad')
    image= models.ImageField(upload_to='product/%Y/%m/%d',blank=True,verbose_name='Imagen' )

    def __str__(self):
         return self.name
    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')

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

    class Meta:
         verbose_name= 'Cliente'
         verbose_name_plural='Clientes'
         ordering=['id']


    






    
