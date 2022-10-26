

from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView , CreateView , UpdateView,FormView
from core.erp.forms import ListForm
from core.erp.models import producto
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login




class ProductoListView(ListView):
    model = producto
    template_name = 'core/erp/templates/producto/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de productos '
        
        return context

class CreateListView(CreateView):
    model = producto
    form_class = ListForm
    template_name = 'core/erp/templates/producto/create.html'
    success_url = reverse_lazy('erp:producto_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Cargar Productos'
        return context

class UpdateListView(UpdateView):
    model = producto
    form_class = ListForm
    template_name = 'core/erp/templates/producto/create.html'
    success_url = reverse_lazy('erp:producto_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Productos'
        return context


