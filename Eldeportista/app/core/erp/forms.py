
from django.forms import ModelForm
from core.erp.models import producto, cliente

        
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

      