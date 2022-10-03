
from django.forms import ModelForm
from core.erp.models import producto


class ListForm(ModelForm):
    class Meta:
        model = producto
        fields = '__all__'