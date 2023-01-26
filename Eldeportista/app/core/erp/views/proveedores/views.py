from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic import ListView 
from core.erp.forms import SupplierForm
from core.erp.models import proveedores
from django.forms.models import model_to_dict
from core.erp.mixins import IsSuperuserMixin


class ProveedorListView(LoginRequiredMixin,ListView):
    model = proveedores
    template_name = 'core/erp/templates/proveedores/listproveedores.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
            return super().dispatch(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in proveedores.objects.all():
                    data.append(model_to_dict(i))
            elif action =='add':
                cli = proveedores()
                cli.nombre = request.POST['nombre']
                cli.ruc= request.POST['ruc']
                cli.telefono= request.POST['telefono']
                cli.direccion= request.POST['direccion']
                cli.user_create = request.user.username
                cli.save()
            elif action == 'edit':
                cli = proveedores.objects.get(pk=request.POST['id'])
                cli.nombre = request.POST['nombre']
                cli.ruc= request.POST['ruc']
                cli.telefono= request.POST['telefono']
                cli.direccion= request.POST['direccion']
                cli.user_update = request.user.username
                cli.save()
            elif action == 'delete':
                cli = proveedores.objects.get(pk=request.POST['id'])
                cli.user_update = request.user.username
                cli.save()
                cli.delete()          
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            
            data['error'] = str(e)

        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['title'] = 'Listado de proveedores '
            context['create_url'] = reverse_lazy('erp:proveedor_list')
            context['form'] = SupplierForm()
            return context