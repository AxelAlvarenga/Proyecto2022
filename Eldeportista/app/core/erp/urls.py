
from django.urls import path
from core.erp.views.category.views import *
from core.erp.views.clientes.views import *

app_name='erp'
urlpatterns = [
    path('producto/list', ProductoListView.as_view() , name='producto_list'),
    path('producto/create', CreateListView.as_view() , name='producto_create'),
    path('producto/edit/<int:pk>/',  UpdateListView.as_view() , name='producto_edit'),
    path('producto/delete/<int:pk>/',  DeleteListView.as_view() , name='producto_delete'),
    
    path('cliente/listcliente', ClienteListView.as_view() , name='cliente_list'),
    path('cliente/create', CreateCliView.as_view() , name='cliente_create'),
    path('cliente/edit/<int:pk>/',  UpdateCliView.as_view() , name='cliente_edit'),
    path('cliente/delete/<int:pk>/',  DeleteCliView.as_view() , name='cliente_delete')
]