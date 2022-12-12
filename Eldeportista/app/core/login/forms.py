
from django.forms import ModelForm
from core.erp.models import *
from django.forms import *


class ListForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
           form.field.widget.attrs['class']='form-control'
           form.field.widget.attrs['autocomplete']='off'
        self.fields['username'].widget.attrs['autofocus']=True
    class Meta:
        model = empleado
        fields = '__all__'
       