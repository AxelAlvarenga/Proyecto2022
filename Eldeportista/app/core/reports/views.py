from django.shortcuts import render
from django.urls import reverse_lazy
from core.reports.forms import ReportForm

from django.views.generic import TemplateView

# Create your views here.

from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from core.erp.models import Sale, Buy
from core.reports.forms import ReportForm,cliForm,provForm
from django.db.models.functions import Coalesce
from django.db.models import Sum,DecimalField 
from django.contrib.auth.mixins import LoginRequiredMixin


class ReportSaleView(LoginRequiredMixin,TemplateView):
    template_name = 'core/reports/templates/sale/reports.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_report':
                data = []
                start_date = request.POST.get('start_date', '')
                end_date = request.POST.get('end_date', '')
                cli = request.POST['cli']
                search = Sale.objects.all()
                if len(start_date) and len(end_date):
                    search = search.filter(date_joined__range=[start_date, end_date])
                if len(cli):
                    search = search.filter(cli_id=cli)
                for s in search:
                    data.append([
                        s.id,
                        s.cli.name,
                        s.date_joined.strftime('%Y-%m-%d'),
                        format(s.subtotal, '.2f'),
                        format(s.iva, '.2f'),
                        format(s.total, '.2f'),
                    ])
                subtotal = search.aggregate(r=Coalesce(Sum('subtotal'), 0, output_field=DecimalField())).get('r') 
                iva = search.aggregate(r=Coalesce(Sum('iva'), 0, output_field=DecimalField())).get('r') 
                total = search.aggregate(r=Coalesce(Sum('total'), 0, output_field=DecimalField())).get('r') 
                
                data.append([
                    '---',
                    '---',
                    '---',
                    format(subtotal, '.2f'),
                    format(iva, '2f'),
                    format(total, '2f'),
                ])   
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Reporte de Ventas'
        context['entity'] = 'Reportes'
        context['list_url'] = reverse_lazy('sale_report')
        context['form'] = ReportForm()
        context['forms'] = cliForm()
        return context

class ReportBuyView(LoginRequiredMixin,TemplateView):
    template_name = 'core/reports/templates/buy/reports.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'report_buy':
                data = []
                start_date = request.POST.get('start_date', '')
                end_date = request.POST.get('end_date', '')
                prov = request.POST['prov']
                search = Buy.objects.all()
                if len(start_date) and len(end_date):
                    search = search.filter(date_joined__range=[start_date, end_date])
                if len(prov):
                    search = search.filter(prov_id=prov)
                for s in search:
                    data.append([
                        s.id,
                        s.prov.nombre,
                        s.date_joined.strftime('%Y-%m-%d'),
                        format(s.subtotal, '.2f'),
                        format(s.iva, '.2f'),
                        format(s.total, '.2f'),
                    ])
                subtotal = search.aggregate(r=Coalesce(Sum('subtotal'), 0, output_field=DecimalField())).get('r') 
                iva = search.aggregate(r=Coalesce(Sum('iva'), 0, output_field=DecimalField())).get('r') 
                total = search.aggregate(r=Coalesce(Sum('total'), 0, output_field=DecimalField())).get('r') 
                
                data.append([
                    '---',
                    '---',
                    '---',
                    format(subtotal, '.2f'),
                    format(iva, '2f'),
                    format(total, '2f'),
                ])   
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Reporte de Compras'
        context['entity'] = 'Reportes'
        context['list_url'] = reverse_lazy('buy_report')
        context['form'] = ReportForm()
        context['forms'] = provForm()
        return context
