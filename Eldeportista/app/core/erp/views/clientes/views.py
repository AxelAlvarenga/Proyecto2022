from sre_constants import SUCCESS
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from core.erp.forms import ClientForm
from core.erp.models import cliente
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin


class ClienteListView(LoginRequiredMixin,ListView):
    model = cliente
    template_name = 'core/erp/templates/cliente/listcliente.html'

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
                for i in cliente.objects.all():
                    data.append(i.toJSON())
            elif action == 'add':
                cli = cliente()
                cli.name = request.POST['name']
                cli.correo = request.POST['correo']
                cli.telefono = request.POST['telefono']
                cli.direccion= request.POST['direccion']
                cli.Ruc = request.POST['Ruc']
                cli.user_create = request.user.username
                cli.save()
            elif action == 'edit':
                cli = cliente.objects.get(pk=request.POST['id'])
                cli.name = request.POST['name']
                cli.correo = request.POST['correo']
                cli.telefono = request.POST['telefono']
                cli.direccion= request.POST['direccion']
                cli.Ruc = request.POST['Ruc']
                cli.user_update = request.user.username
                cli.save()
            elif action == 'delete':
                cli = cliente.objects.get(pk=request.POST['id'])
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
        context['title'] = 'Listado de clientes '
        context['create_url'] = reverse_lazy('erp:cliente_create')
        context['form'] = ClientForm()
        return context

    
