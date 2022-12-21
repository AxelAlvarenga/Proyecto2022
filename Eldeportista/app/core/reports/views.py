from django.shortcuts import render
from django.urls import reverse_lazy
from core.reports.forms import ReportForm

from django.views.generic import TemplateView

# Create your views here.

class ReportSaleView(TemplateView):
    template_name = 'core/reports/templates/sale/reports.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Reporte de Ventas'
        context['entity'] = 'Reportes'
        context['list_url'] = reverse_lazy('sale_report')
        context['form'] = ReportForm()
        return context