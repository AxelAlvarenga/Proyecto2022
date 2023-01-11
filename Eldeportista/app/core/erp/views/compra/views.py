from django.contrib.auth.mixins import LoginRequiredMixin
import json
from django.db import transaction
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import Group
from core.erp.forms import  BuyForm
from django.views.generic import CreateView,ListView,View

from core.erp.models import *
import os
from django.conf import settings
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect
from django.template import Context
from django.template.loader import get_template
from xhtml2pdf import pisa


class BuyListView(LoginRequiredMixin,ListView):
    model = Buy
    template_name = 'core/erp/templates/compra/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Buy.objects.all():
                   data.append(i.toJSON())
            elif action == 'search_details_prod':
                data = []
                for i in DetBuy.objects.filter(buy_id=request.POST['id']):
                    data.append(i.toJSON())
            elif action == 'delete':
                if request.session['group']== Group.objects.get(pk=1):
                    cli = Buy.objects.get(pk=request.POST['id'])
                    cli.delete()
                else:
                    data['error'] = 'No tienes permiso para esto'
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de compras'
        context['create_url'] = reverse_lazy('erp:sale_create')
        context['list_url'] = reverse_lazy('erp:buy_list')
        context['entity'] = 'Compras'
        return context

class BuyCreateView(LoginRequiredMixin, CreateView):
    model = Buy
    form_class = BuyForm
    template_name = 'core/erp/templates/compra/create.html'
    success_url = reverse_lazy('index')
    url_redirect = success_url
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_products':
                data = []
                prods = producto.objects.filter(name__icontains=request.POST['term'])[0:10]
                for i in prods:
                    item = i.toJSON()
                    item['value'] = i.name
                    data.append(item)
            elif action == 'add':
                with transaction.atomic():
                    vents = json.loads(request.POST['vents'])
                    sale = Buy()
                    sale.date_joined = vents['date_joined']
                    sale.prov_id = vents['prov']
                    sale.comprobante = vents['comprobante']
                    sale.subtotal = float(vents['subtotal'])
                    sale.iva = float(vents['iva'])
                    sale.total = float(vents['total'])
                    sale.save()
                    for i in vents['products']:
                        det = DetBuy()
                        det.buy_id = sale.id
                        det.prod_id = i['id']
                        det.cant = int(i['cant'])
                        det.price = float(i['price'])
                        det.subtotal = float(i['subtotal'])
                        det.save()
                        det.prod.cantidad += det.cant
                        det.prod.save()
                    data = {'id': sale.id}
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de una Compra'
        context['entity'] = 'Compras'
        context['create_url'] = reverse_lazy('erp:buy_create')
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context

