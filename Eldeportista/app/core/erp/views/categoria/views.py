from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic import ListView , CreateView , UpdateView , DeleteView
from core.erp.forms import categoryform
from core.erp.models import categoria


class CategoriaListView(ListView):
    model = categoria
    template_name = 'core/erp/templates/categoria/listcate.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
            return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['title'] = 'Listado de categorias '
            context['create_url_cate'] = reverse_lazy('erp:categoria_create')
            
            return context

class CreateCateView(CreateView):
    model = categoria
    form_class = categoryform
    template_name = 'core/erp/templates/categoria/create.html'
    success_url = reverse_lazy('erp:categoria_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Cargar categoria'
        return context

class UpdateCateView(UpdateView):
    model = categoria
    form_class = categoryform
    template_name = 'core/erp/templates/categoria/create.html'
    success_url = reverse_lazy('erp:categoria_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Categoria'
        return context

class DeleteCateView(DeleteView):
    model = categoria
    template_name = 'core/erp/templates/categoria/delete.html'
    success_url = reverse_lazy('erp:categoria_list')
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Borrar Productos'
        context['list_url'] = reverse_lazy('erp:producto_list')
        return context

