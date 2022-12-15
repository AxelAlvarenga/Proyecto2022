from django.forms import *
from core.erp.models import producto, cliente ,categoria,colores



class categoryform(ModelForm):
    class Meta:
        model = categoria
        fields = '__all__'
        widgets = {
            'name_cat': TextInput(attrs={'placeholder': 'Ingrese el nombre de la categoria',}),
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

class ListFormCli(ModelForm):
    class Meta:
        model = cliente
        fields = '__all__'

class ListForm(ModelForm):
    def init(self, args, **kwargs):
        super().init(args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = producto
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Ingrese el nombre del prodcto',}),
            'talla': TextInput(attrs={'placeholder': 'Ingrese la talla',}),
            'price': TextInput(attrs={'placeholder': 'Ingrese el precio de venta',}),
            'cat': Select(attrs={'placeholder': 'Ingrese la categoria',}),
            'cantidad': TextInput(attrs={'placeholder': 'Ingrese su cantidad',}),

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
        'class': 'form-control select2',
        'style': 'width: 100%'
    }))

    products = ModelChoiceField(queryset=producto.objects.none(), widget=Select(attrs={
        'class': 'form-control select2',
        'style': 'width: 100%'
    }))

    search = CharField(widget=TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ingrese una descripción'
    }))        

      