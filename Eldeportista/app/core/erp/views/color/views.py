from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic import ListView 
from core.erp.forms import colorform
from core.erp.models import colores
from django.forms.models import model_to_dict


class ColorListView(ListView):
    model = colores
    template_name = 'core/erp/templates/color/listcolor.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
            return super().dispatch(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in colores.objects.all():
                    data.append(i.toJSON())
            elif action == 'add':
                cli = colores()
                cli.name_color = request.POST['name_color']
                cli.save()
            elif action == 'edit':
                cli = colores.objects.get(pk=request.POST['id'])
                cli.name_color = request.POST['name_color']
                cli.save()
            elif action == 'delete':
                cli = colores.objects.get(pk=request.POST['id'])
                cli.delete()
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)  

    


    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['title'] = 'Listado de colores '
            context['create_url'] = reverse_lazy('erp:color_create')
            context['form'] = colorform()
            return context
