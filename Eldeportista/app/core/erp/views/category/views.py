from math import prod
from unicodedata import category
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView , CreateView
from core.erp.forms import ListForm
from core.erp.models import producto


    
class ProductoListView(ListView):
    model = producto
    template_name = 'templatesproducto/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de productos '
        context['create_url'] = reverse_lazy('erp:product_create')
        return context

class CreateListView(CreateView):
    model = producto
    form_class = ListForm
    template_name = 'templates/producto/create.html'
    success_url = reverse_lazy('erp:producto_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Cargar Productos'
        return context