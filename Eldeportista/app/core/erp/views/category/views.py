

<<<<<<< HEAD
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView , CreateView , UpdateView,FormView
=======
from django.views.generic import ListView , CreateView , UpdateView , DeleteView
>>>>>>> 817f7a422b5529a8df9d0e1588778bc4d382b10c
from core.erp.forms import ListForm
from core.erp.models import producto
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login




class ProductoListView(ListView):
    model = producto
    template_name = 'core/erp/templates/producto/list.html'
    success_url = reverse_lazy('erp:producto_create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de productos '
        context['create_url'] = reverse_lazy('erp:producto_create')
        
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

<<<<<<< HEAD

=======
class DeleteListView(DeleteView):
    model = producto
    form_class = ListForm
    template_name = 'core/erp/templates/producto/delete.html'
    success_url = reverse_lazy('erp:producto_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Borrar Productos'
        context['list_url'] = reverse_lazy('erp:producto_list')
        return context
>>>>>>> 817f7a422b5529a8df9d0e1588778bc4d382b10c
