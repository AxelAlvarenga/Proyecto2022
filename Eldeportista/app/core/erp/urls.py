
from django.urls import path
from core.erp.views.category.views import *
from core.erp.views.clientes.views import *
from core.erp.views.categoria.views import *
from core.erp.views.color.views import *
from core.erp.views.test.views import *
from core.erp.views.sale.views import *
from core.erp.views.proveedores.views import *

app_name='erp'
urlpatterns = [
    path('producto/list', ProductoListView.as_view() , name='producto_list'),
    path('producto/create', CreateListView.as_view() , name='producto_create'),
    path('producto/edit/<int:pk>/',  UpdateListView.as_view() , name='producto_edit'),
    path('producto/delete/<int:pk>/',  DeleteListView.as_view() , name='producto_delete'),

    path('proveedores/listproveedores', ProveedorListView.as_view() , name='proveedor_list'),
    
    path('cliente/listcliente', ClienteListView.as_view() , name='cliente_list'),

    
    path('categoria/listcate', CategoriaListView.as_view() , name='categoria_list'),

    path('color/listcolor', ColorListView.as_view() , name='color_list'),
    # sale
    path('sale/create', SaleCreateView.as_view(), name='sale_create'),
    path('sale/list/', SaleListView.as_view(), name='sale_list'),
    # test
    path('test/test', TestView.as_view(), name='test'),
    #reportsale
    path('sale/invoice/pdf/<int:pk>/', SaleInvoicePdfView.as_view(), name='sale_invoice_pdf'),

]