
from django.contrib.auth.mixins import LoginRequiredMixin
import json
from django.db import transaction
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from core.erp.mixins import ValidatePermissionRequiredMixin

from core.erp.forms import SaleForm , ClientForm , CreditForm
from django.views.generic import CreateView,ListView,View
from django.contrib.auth.models import Group
from core.erp.models import *
import os
from django.conf import settings
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect
from django.template import Context
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.db.models import Q
from nlt import numlet as nl


class SaleListView(LoginRequiredMixin,ListView):
    model = Sale
    template_name = 'core/erp/templates/sale/list.html'
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Sale.objects.all():
                   data.append(i.toJSON())
            elif action == 'search_details_prod':
                data = []
                for i in DetSale.objects.filter(sale_id=request.POST['id']):
                    data.append(i.toJSON())
            elif action == 'delete':
                if request.session['group']== Group.objects.get(pk=1):
                    cli = Sale.objects.get(pk=request.POST['id'])
                    cli.delete()
                else:
                    data['error'] = 'No tienes permiso para esto'
            elif action == 'estado':
                cred= Sale.objects.get(pk=request.POST['id'])
                cli = CreditSale()
                cli.price = request.POST['price']
                cli.sale_id = cred.id
                if (cred.estado >= decimal.Decimal(cli.price)) & (cli.price >'0'):
                    cli.save()    
                    cli.sale.estado -= (decimal.Decimal(cli.price))
                    cli.sale.save()
                else:
                    data['error'] = 'Ingrese un monto valido'
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Ventas'
        context['create_url'] = reverse_lazy('erp:sale_create')
        context['list_url'] = reverse_lazy('erp:sale_list')
        context['entity'] = 'Ventas'
        context['form'] = CreditForm()
        
        

        return context

class SaleCreditListView(LoginRequiredMixin,ListView):
    model = CreditSale
    template_name = 'core/erp/templates/sale/creditlist.html'
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in CreditSale.objects.all():
                   data.append(i.toJSON())
            elif action == 'search_details_prod':
                data = []
                
                for i in DetSale.objects.filter(sale_id=request.POST['id']):
                    data.append(i.toJSON())
            elif action == 'delete':
                if request.session['group']== Group.objects.get(pk=1):
                    cli = CreditSale.objects.get(pk=request.POST['id'])
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
        context['title'] = 'Listado de Recibos'
        context['create_url'] = reverse_lazy('erp:sale_create')
        context['list_url'] = reverse_lazy('erp:sale_credit')
        context['entity'] = 'Recibos'
        context['form'] = CreditForm()
        return context


class SaleCreateView(LoginRequiredMixin, CreateView):
    model = Sale
    form_class = SaleForm
    template_name = 'core/erp/templates/sale/create.html'
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
                ids_exclude = json.loads(request.POST['ids'])
                term = request.POST['term'].strip()
                products = producto.objects.all()
                if len(term):
                    products = products.filter(name__icontains=term)
                for i in products.exclude(id__in=ids_exclude)[0:10]:
                    item = i.toJSON()
                    item['text'] = i.name
                    # item['text'] = i.name
                    data.append(item)
            elif action == 'add':
                with transaction.atomic():
                    vents = json.loads(request.POST['vents'])
                    sale = Sale()
                    sale.date_joined = vents['date_joined']
                    sale.cli_id = vents['cli']
                    sale.subtotal = float(vents['subtotal'])
                    sale.iva = float(vents['iva'])
                    sale.total = float(vents['total'])
                    sale.metodo= vents['metodo']
                    if sale.metodo == 'Credito':
                        sale.estado= sale.total
                    else: 
                        sale.estado= 0
                    sale.user_create = request.user.username    
                    sale.save()
                    for i in vents['products']:
                        det = DetSale()
                        det.sale_id = sale.id
                        det.prod_id = i['id']
                        det.cant = int(i['cant'])
                        det.price = float(i['price'])
                        det.subtotal = float(i['subtotal'])
                        det.save()
                        det.prod.cantidad -= (det.cant)
                        det.prod.user_update = request.user.username 
                        det.prod.save()
                    data = {'id': sale.id}
            elif action =='search_clients':
                data = []
                term = request.POST['term']
                prods = cliente.objects.filter(Q(name__icontains=term) | Q(Ruc__icontains=term))[0:10]
                for i in prods:
                    item = i.toJSON()
                    item['text'] = i.get_full_name()
                    data.append(item)
            elif action == 'create_client':
                with transaction.atomic():
                    frmClient = ClientForm(request.POST)
                    data = frmClient.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de una Venta'
        context['entity'] = 'Ventas'
        context['create_url'] = reverse_lazy('erp:sale_create')
        context['list_url'] = self.success_url
        context['action'] = 'add'
        context['frmClient'] = ClientForm()
        return context

class SaleInvoicePdfView(View):
    def link_callback(self, uri, rel):
        """
        Convert HTML URIs to absolute system paths so xhtml2pdf can access those
        resources
        """
        # use short variable names
        sUrl = settings.STATIC_URL  # Typically /static/
        sRoot = settings.STATIC_ROOT  # Typically /home/userX/project_static/
        mUrl = settings.MEDIA_URL  # Typically /static/media/
        mRoot = settings.MEDIA_ROOT  # Typically /home/userX/project_static/media/

        # convert URIs to absolute system paths
        if uri.startswith(mUrl):
            path = os.path.join(mRoot, uri.replace(mUrl, ""))
        elif uri.startswith(sUrl):
            path = os.path.join(sRoot, uri.replace(sUrl, ""))
        else:
            return uri  # handle absolute uri (ie: http://some.tld/foo.png)

        # make sure that file exists
        if not os.path.isfile(path):
            raise Exception(
                'media URI must start with %s or %s' % (sUrl, mUrl)
            )
        return path

    def get(self, request, *args, **kwargs):
        try:
            template = get_template('sale/invoice.html')
            context = {
                'sale': Sale.objects.get(pk=self.kwargs['pk']),
                'comp': {'name': 'EL DEPORTISTA', 'ruc': '1234567', 'address': 'Circuito comercial, Encarnacion'},
                #'icon': '{}{}'.format(STATIC_URL, 'img/IconoEldeportista.png')
            }
            html = template.render(context)
            response = HttpResponse(content_type='application/pdf')
            #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
            pisaStatus = pisa.CreatePDF(
                html, dest=response,
                link_callback=self.link_callback
            )
            return response
        except:
            pass
        return HttpResponseRedirect(reverse_lazy('erp:sale_list'))

class CreditInvoicePdfView(View):
    def link_callback(self, uri, rel):
        """
        Convert HTML URIs to absolute system paths so xhtml2pdf can access those
        resources
        """
        # use short variable names
        sUrl = settings.STATIC_URL  # Typically /static/
        sRoot = settings.STATIC_ROOT  # Typically /home/userX/project_static/
        mUrl = settings.MEDIA_URL  # Typically /static/media/
        mRoot = settings.MEDIA_ROOT  # Typically /home/userX/project_static/media/

        # convert URIs to absolute system paths
        if uri.startswith(mUrl):
            path = os.path.join(mRoot, uri.replace(mUrl, ""))
        elif uri.startswith(sUrl):
            path = os.path.join(sRoot, uri.replace(sUrl, ""))
        else:
            return uri  # handle absolute uri (ie: http://some.tld/foo.png)

        # make sure that file exists
        if not os.path.isfile(path):
            raise Exception(
                'media URI must start with %s or %s' % (sUrl, mUrl)
            )
        return path

    def get(self, request, *args, **kwargs):
        try:
            template = get_template('sale/invoiceCredito.html')
            context = {
                'sale': CreditSale.objects.get(pk=self.kwargs['pk']),
                'comp': {'name': 'EL DEPORTISTA', 'ruc': '1234567', 'address': 'Circuito comercial, Encarnacion'},
                
                #'icon': '{}{}'.format(STATIC_URL, 'img/IconoEldeportista.png')
            }
            html = template.render(context)
            response = HttpResponse(content_type='application/pdf')
            #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
            pisaStatus = pisa.CreatePDF(
                html, dest=response,
                link_callback=self.link_callback
            )
            return response
        except:
            pass
        return HttpResponseRedirect(reverse_lazy('erp:sale_credit'))