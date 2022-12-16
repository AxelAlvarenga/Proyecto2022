
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView , CreateView , UpdateView , DeleteView
from core.erp.forms import ListForm
from core.erp.models import producto,colores,categoria
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

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                
                for i in producto.objects.all():
                    
                    data.append(i.toJSON())
            elif action =='add':
                cli = producto()
                cli.name = request.POST['name']
                cli.talla_id = request.POST['talla']
                cli.price = request.POST['price']
                cli.cat_id = request.POST['cat']
                cli.cantidad = request.POST['cantidad']
                cli.save()
            elif action == 'edit':
                cli = producto.objects.get(pk=request.POST['id'])
                cli.name = request.POST['name']
                cli.talla_id = request.POST['talla']
                cli.price = request.POST['price']
                cli.cat_id = request.POST['cat']
                cli.cantidad = request.POST['cantidad']
                cli.save()
            elif action == 'delete':
                cli = producto.objects.get(pk=request.POST['id'])
                cli.delete()          
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            
            data['error'] = str(e)

        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de productos '
        context['create_url'] = reverse_lazy('erp:producto_create')
        context['form'] = ListForm()
        
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
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data={}
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

