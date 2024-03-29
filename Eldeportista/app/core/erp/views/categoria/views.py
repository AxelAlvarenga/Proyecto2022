from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic import ListView 
from core.erp.forms import categoryform
from core.erp.models import categoria
from django.forms.models import model_to_dict
from core.erp.forms import categoryform
from core.erp.mixins import IsSuperuserMixin


class CategoriaListView(LoginRequiredMixin,ListView):
    model = categoria
    template_name = 'core/erp/templates/categoria/listcate.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
            return super().dispatch(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in categoria.objects.all():
                    data.append(model_to_dict(i))
            elif action =='add':
                cli = categoria()
                cli.name_cat = request.POST['name_cat']
                cli.save()
            elif action == 'edit':
                cli = categoria.objects.get(pk=request.POST['id'])
                cli.name_cat = request.POST['name_cat']
                cli.save()
            elif action == 'delete':
                cli = categoria.objects.get(pk=request.POST['id'])
                cli.delete()          
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            
            data['error'] = str(e)

        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['title'] = 'Listado de categorias '
            context['create_url'] = reverse_lazy('erp:categoria_create')
            context['form'] = categoryform()
            return context



