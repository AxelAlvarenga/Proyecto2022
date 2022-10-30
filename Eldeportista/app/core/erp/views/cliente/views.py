from sre_constants import SUCCESS
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView , CreateView , UpdateView , DeleteView
from core.erp.forms import ListForm
from core.erp.models import cliente
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

class ClienteListView(ListView):
    model = cliente
    template_name = 'core/erp/templates/cliente/list_cliente.html'
   
    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de clientes '
        context['create_url'] = reverse_lazy('erp:cliente_create')
       
        
        return context