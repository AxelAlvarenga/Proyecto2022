from django.forms import *
from core.erp.models import *

class ReportForm(Form):
    
    date_range = CharField(widget=TextInput(attrs={
        'class': 'form-control',
        'autocomplete': 'off'
    }))

class cliForm(ModelForm):
    

    class Meta:
        model = Sale
        fields = '__all__'
        widgets = {
            'cli': Select(attrs={
                'class': 'form-control select2',
                'style': 'width: 100%'
        })
        }

class provForm(ModelForm):
    

    class Meta:
        model = Buy
        fields = '__all__'
        widgets = {
            'prov': Select(attrs={
                'class': 'form-control select2',
                'style': 'width: 100%'
        })
        }
   
    
