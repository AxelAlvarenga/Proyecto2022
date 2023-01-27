from django.forms import *
from core.erp.models import *



class categoryform(ModelForm):
    class Meta:
        model = categoria
        fields = '__all__'
        widgets = {
            'name_cat': TextInput(attrs={'placeholder': 'Ingrese el nombre de la categoria',}),
        }
        exclude=['user_update','user_creation']
        
        
    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class colorform(ModelForm):
    class Meta:
        model = colores
        fields = '__all__'
        widgets = {
            'name_color': TextInput(attrs={'placeholder': 'Ingrese el nombre del color',}),
        }
        
        
    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class ListForm(ModelForm):
    def init(self, args, **kwargs):
        super().init(args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = producto
        fields = 'name', 'cat', 'cantidad', 'talla', 'price','price_buy','gender','user_create','user_update'
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Ingrese el nombre del prodcto',}),
            'talla': Select(attrs={'placeholder': 'Ingrese la talla',}),
            'price': TextInput(attrs={'placeholder': 'Ingrese el precio de venta',}),
            'cat': Select(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese la categoria'
                }),
            'cantidad': TextInput(attrs={'placeholder': 'Ingrese su cantidad',}),
            'user_create': TextInput(
                attrs={
                    'type' : 'hidden',
                    'readonly': True
                }
            ),
            'user_update': TextInput(
                attrs={
                    'type' : 'hidden',
                    'readonly': True
                }
            ),

        }
        
        
    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class TestForm(Form):
    categories = ModelChoiceField(queryset=categoria.objects.all(), widget=Select(attrs={
        'class': 'form-control ',
        'style': 'width: 100%'
    }))
    

    products = ModelChoiceField(queryset=Talla.objects.none(), widget=Select(attrs={
        'class': 'form-control ',
        'style': 'width: 100%'
    }))

    search = CharField(widget=TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ingrese una descripción'
    }))

class ClientForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = cliente
        fields = '__all__' 
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Ingrese su nombre',}),
            'correo': TextInput(attrs={'placeholder': 'Ingrese su correo',}),
            'telefono': TextInput(attrs={'placeholder': 'Ingrese su telefono',}),
            'Ruc': TextInput(attrs={'placeholder': 'Ingrese su Ruc',}),
            'direccion': TextInput(attrs={'placeholder': 'Ingrese su direccion',}),
        }
        
        
    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class CreditForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['price'].widget.attrs['autofocus'] = True

    class Meta:
        model = CreditSale
        fields = '__all__' 
        widgets = {
            'price': NumberInput(attrs={'placeholder': 'Ingrese el monto a descontar',}),
        }
        exclude = [ 'sale']
        
        
    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
        

class SaleForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cli'].queryset =  cliente.objects.none()

    class Meta:
        model = Sale
        fields = '__all__'
        widgets = {
            'cli': Select(attrs={
                'class': 'form-control select2',
                # 'style': 'width: 100%'
            }),
            'metodo': Select(attrs={
                'class': 'form-control select2',
                'style': 'width: 100%'
            }),
            'date_joined': DateInput(
                format='%Y-%m-%d',
                attrs={
                    'value': datetime.now().strftime('%Y-%m-%d'),
                    'autocomplete': 'off',
                    'class': 'form-control datetimepicker-input',
                    'id': 'date_joined',
                    'data-target': '#date_joined',
                    'data-toggle': 'datetimepicker',
                    'readonly': True


                }
            ),
            'iva': TextInput(attrs={
                'class': 'form-control',
            }),
            'subtotal': TextInput(attrs={
                'readonly': True,
                'class': 'form-control',
            }),
            'total': TextInput(attrs={
                'readonly': True,
                'class': 'form-control',
            })
        }

class BuyForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Buy
        fields = '__all__'
        widgets = {
            'comprobante': NumberInput(attrs={
                'class': 'form-control',
            }),
            'prov': Select(attrs={
                'class': 'form-control select2',
                'style': 'width: 100%'
            }),
            'date_joined': DateInput(
                format='%Y-%m-%d',
                attrs={
                    'value': datetime.now().strftime('%Y-%m-%d'),
                    'autocomplete': 'off',
                    'class': 'form-control datetimepicker-input',
                    'id': 'date_joined',
                    'data-target': '#date_joined',
                    'data-toggle': 'datetimepicker',
                    'readonly': True
                }
            ),
            'iva': TextInput(attrs={
                'class': 'form-control',
            }),
            'subtotal': TextInput(attrs={
                'readonly': True,
                'class': 'form-control',
            }),
            'total': TextInput(attrs={
                'readonly': True,
                'class': 'form-control',
            }),
            

        }

class SupplierForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['nombre'].widget.attrs['autofocus'] = True
    
    class Meta:
        model = proveedores
        fields = '__all__'

        widgets = {
            'nombre': TextInput(
                attrs={
                    'placeholder' : 'Ingrese nombre del proveedor'
                }
            ),
            'ruc': TextInput(
                attrs={
                    'placeholder' : 'Ingrese ruc del proveedor'
                }
            ),'telefono': TextInput(
                attrs={
                    'placeholder' : 'Ingrese telefono del proveedor'
                }
            ),
            'direccion': TextInput(attrs={'placeholder': 'Ingrese su direccion',}
            ),
            'user_create': TextInput(
                attrs={
                    'type' : 'hidden',
                    'readonly': True
                }
            ),
            'user_update': TextInput(
                attrs={
                    'type' : 'hidden',
                    'readonly': True
                }
            ),


        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                instance = form.save()
                data = instance.toJSON()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data



           