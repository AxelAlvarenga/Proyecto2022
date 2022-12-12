
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView , CreateView , UpdateView , DeleteView
from core.erp.forms import ListForm
from core.erp.models import producto
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse




class ProductoListView(ListView):
    model = producto
    template_name = 'core/erp/templates/producto/list.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de productos '
        context['create_url'] = reverse_lazy('erp:producto_create')
        context['create_url_cate'] = reverse_lazy('erp:categoria_create')
        context['create_url_color'] = reverse_lazy('erp:color_create')
        
        return context
    
class CreateListView(CreateView):
    model = producto
    form_class = ListForm
    template_name = 'core/erp/templates/producto/create.html'
    success_url = reverse_lazy('erp:producto_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Cargar Productos'
        return context

class UpdateListView(UpdateView):
    model = producto
    form_class = ListForm
    template_name = 'core/erp/templates/producto/create.html'
    success_url = reverse_lazy('erp:producto_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Productos'
        return context

class DeleteListView(DeleteView):
    model = producto
    template_name = 'core/erp/templates/producto/delete.html'
    success_url = reverse_lazy('erp:producto_list')
    
    @method_decorator(login_required)
    
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data=[]
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Borrar Productos'
        context['list_url'] = reverse_lazy('erp:producto_list')
        return context

