from sre_constants import SUCCESS
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView , CreateView , UpdateView , DeleteView
from core.erp.forms import ClientForm,ListFormCli
from core.erp.models import cliente
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.forms.models import model_to_dict


class ClienteListView(ListView):
    model = cliente
    template_name = 'core/erp/templates/cliente/listcliente.html'
   
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in cliente.objects.all():
                    data.append(model_to_dict(i))
            elif action =='add':
                cli= cliente()
                cli.name= request.POST['name']
                cli.correo= request.POST['correo']  
                cli.telefono= request.POST['telefono']  
                cli.Ruc= request.POST['Ruc'] 
                cli.save()      
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

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)
        

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Borrar Clientes'
        context['cliente_url'] = reverse_lazy('erp:cliente_list')
        return context
    
