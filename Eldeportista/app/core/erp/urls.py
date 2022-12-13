
from django.urls import path
from core.erp.views.category.views import *
from core.erp.views.clientes.views import *
from core.erp.views.categoria.views import *
from core.erp.views.color.views import *

app_name='erp'
urlpatterns = [
    path('producto/list', ProductoListView.as_view() , name='producto_list'),
    path('producto/create', CreateListView.as_view() , name='producto_create'),
    path('producto/edit/<int:pk>/',  UpdateListView.as_view() , name='producto_edit'),
    path('producto/delete/<int:pk>/',  DeleteListView.as_view() , name='producto_delete'),
    
    path('cliente/listcliente', ClienteListView.as_view() , name='cliente_list'),

    
    path('categoria/listcate', CategoriaListView.as_view() , name='categoria_list'),

    path('color/listcolor', ColorListView.as_view() , name='color_list'),
    path('color/create', CreateColorView.as_view() , name='color_create'),
    path('color/edit/<int:pk>/',  UpdateColorView.as_view() , name='color_edit'),
    path('color/delete/<int:pk>/',  DeleteColorView.as_view() , name='color_delete')
]