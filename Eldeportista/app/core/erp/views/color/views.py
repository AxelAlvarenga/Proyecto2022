from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic import ListView , CreateView , UpdateView , DeleteView
from core.erp.forms import colorform
from core.erp.models import color


class ColorListView(ListView):
    model = color
    template_name = 'core/erp/templates/color/listcolor.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
            return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['title'] = 'Listado de colores '
            context['create_url'] = reverse_lazy('erp:color_create')
            
            return context

class CreateColorView(CreateView):
    model = color
    form_class = colorform
    template_name = 'core/erp/templates/color/create.html'
    success_url = reverse_lazy('erp:color_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Cargar color'
        return context

class UpdateColorView(UpdateView):
    model = color
    form_class = colorform
    template_name = 'core/erp/templates/color/create.html'
    success_url = reverse_lazy('erp:color_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Color'
        return context

class DeleteColorView(DeleteView):
    model = color
    template_name = 'core/erp/templates/color/delete.html'
    success_url = reverse_lazy('erp:color_list')
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Borrar color'
        context['list_url'] = reverse_lazy('erp:color_list')
        return context