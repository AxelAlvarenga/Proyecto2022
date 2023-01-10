from tabnanny import verbose
from django.db import models
from django.forms import model_to_dict
from crum import get_current_user
from core.models import BaseModel
from datetime import datetime
from core.erp.choices import gender_choices, sale_choices
import decimal


from app.settings import MEDIA_URL, STATIC_URL

# Create your models here.
      


class categoria(models.Model):
    name_cat = models.CharField(max_length=150, verbose_name='Categoria')

    def __str__(self):
        return self.name_cat
    
    

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']

class proveedores(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Nombre')
    ruc = models.CharField(max_length=150, verbose_name='Ruc')
    telefono = models.IntegerField(verbose_name='Telefono')
    direccion = models.CharField(max_length=150, verbose_name='Direccion')


    def __str__(self):
        return self.nombre
    
    

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        ordering = ['id'] 

class Talla(models.Model):
    talla = models.CharField(max_length=150, verbose_name='Talla')
    cat = models.ForeignKey(categoria, on_delete=models.CASCADE, verbose_name='Categoría')
    def __str__(self):
        return self.talla
    
    

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Talla'
        verbose_name_plural = 'Tallas'
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


class producto(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    talla = models.ForeignKey(Talla, on_delete=models.CASCADE, verbose_name='Talla')
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Precio de venta')
    price_buy = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Precio de compra')
    cat = models.ForeignKey(categoria, on_delete=models.CASCADE, verbose_name='Categoría')
    gender = models.CharField(max_length=10, choices=gender_choices, default='male', verbose_name='Genero')
    cantidad=models.IntegerField(verbose_name='cantidad')
    
    def toJSON(self):
        item = model_to_dict(self)
        item['cat'] = self.cat.toJSON()
        item['full_name'] = '{} / {} '.format(self.name, self.cat)
        item['talla'] = self.talla.toJSON()
        item['gender'] = {'id': self.gender, 'name': self.get_gender_display()}
        item['price'] = format(self.price, '.2f')
        item['price_buy'] = format(self.price_buy, '.2f')
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
    Ruc = models.CharField(max_length=150, verbose_name='Ruc o CI ')
    direccion = models.CharField(max_length=150, verbose_name='direccion')
    

    def __str__(self):
         return self.name

    def get_full_name(self):
        return '{} / {}'.format(self.name,self.Ruc)

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
    metodo = models.CharField(max_length=10, choices=sale_choices, default='counted', verbose_name='Metodo de pago')

    def __str__(self):
        return self.cli.name

    

    def toJSON(self):
        item = model_to_dict(self)
        item['cli'] = self.cli.toJSON()
        return item 

    def delete(Self,using=None, keep_parements=False):
        for det in Self.detsale_set.all():
            det.prod.cantidad += det.cant
            det.prod.save()
        super(Sale, Self).delete()

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
 # type: ignore
    def __str__(self):
        return self.prod.name
        
    def toJSON(self):
        item = model_to_dict(self)
        item['prod'] = self.prod.toJSON()
        return item 

    class Meta:
        verbose_name = 'Detalle de Venta'
        verbose_name_plural = 'Detalle de Ventas'
        ordering = ['id']

    
class Buy(models.Model):
    prov = models.ForeignKey(proveedores, on_delete=models.CASCADE)
    date_joined = models.DateField(default=datetime.now)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    iva = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    comprobante = models.IntegerField(default=0)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.prov.nombre

    def toJSON(self):
        item = model_to_dict(self)
        item['prov'] = self.prov.toJSON()
        item['subtotal'] = format(self.subtotal, '.2f')
        item['iva'] = format(self.iva, '.2f')
        item['total'] = format(self.total, '.2f')
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        return item

    def delete(self, using=None, keep_parements=False):
        for det in self.detbuy_set.all():
            det.prod.stock -= (decimal.Decimal(det.cant))
            det.prod.save()
        super(Buy, self).delete()

    class Meta:
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'
        ordering = ['id']

class DetBuy(models.Model):
    buy = models.ForeignKey(Buy, on_delete=models.CASCADE)
    prod = models.ForeignKey(producto, on_delete=models.CASCADE)
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    cant = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name="Cantidad")
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.prod.name

    def toJSON(self):
        item = model_to_dict(self)
        item['cant'] = format(self.cant, '.2f')
        item['buy'] = self.buy.toJSON() 
        item['prod'] = self.prod.toJSON()
        item['price'] = format(self.price, '.2f')
        item['subtotal'] = format(self.subtotal, '.2f')
        return item

    class Meta:
        verbose_name = 'Detalle de Compra'
        verbose_name_plural = 'Detalle de Compras'
        ordering = ['id']






    
