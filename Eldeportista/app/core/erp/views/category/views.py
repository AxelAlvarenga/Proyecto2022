from unicodedata import category
from django.shortcuts import render
from django.views.generic import ListView
from core.erp.models import producto


    
class ProductoListView(ListView):
    model = producto
    template_name = 'producto/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de productos '
        return context
