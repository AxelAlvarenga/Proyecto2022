from sre_constants import SUCCESS
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView , CreateView , UpdateView , DeleteView
from core.erp.forms import ListForm,ListFormCli
from core.erp.models import cliente
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

class ClienteListView(ListView):
    model = cliente
    template_name = 'core/erp/templates/cliente/listcliente.html'
   
    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de clientes '
        context['create_url_cli'] = reverse_lazy('erp:cliente_create')
       
        
        return context

class CreateCliView(CreateView):
    model = cliente
    form_class = ListFormCli
    template_name = 'core/erp/templates/cliente/create.html'
    success_url = reverse_lazy('erp:cliente_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Cargar cliente  '
        return context

class UpdateCliView(UpdateView):
    model = cliente
    form_class = ListFormCli
    template_name = 'core/erp/templates/cliente/create.html'
    success_url = reverse_lazy('erp:cliente_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de clientes '
        return context

class DeleteCliView(DeleteView):
    model = cliente
    template_name = 'core/erp/templates/cliente/delete.html'
    success_url = reverse_lazy('erp:cliente_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Borrar Clientes'
        context['cliente_url'] = reverse_lazy('erp:cliente_list')
        return context