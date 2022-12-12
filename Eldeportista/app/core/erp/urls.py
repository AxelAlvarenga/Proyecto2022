
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
    path('cliente/create', CreateCliView.as_view() , name='cliente_create'),
    path('cliente/edit/<int:pk>/',  UpdateCliView.as_view() , name='cliente_edit'),
    path('cliente/delete/<int:pk>/',  DeleteCliView.as_view() , name='cliente_delete'),

    
    path('categoria/listcate', CategoriaListView.as_view() , name='categoria_list'),
    path('categoria/create', CreateCateView.as_view() , name='categoria_create'),
    path('categoria/edit/<int:pk>/',  UpdateCateView.as_view() , name='categoria_edit'),
    path('categoria/delete/<int:pk>/',  DeleteCateView.as_view() , name='categoria_delete'),

     path('color/listcolor', ColorListView.as_view() , name='color_list'),
    path('color/create', CreateColorView.as_view() , name='color_create'),
    path('color/edit/<int:pk>/',  UpdateColorView.as_view() , name='color_edit'),
    path('color/delete/<int:pk>/',  DeleteColorView.as_view() , name='color_delete')
]