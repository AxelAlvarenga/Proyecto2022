
from django.urls import path
from core.erp.views.category.views import *

app_name='erp'
urlpatterns = [
    path('producto/list', ProductoListView.as_view() , name='producto_list'),
    path('producto/create', CreateListView.as_view() , name='producto_create'),
    path('producto/edit/<int:pk>/',  UpdateListView.as_view() , name='producto_edit'),
    path('producto/delete/<int:pk>/',  DeleteListView.as_view() , name='producto_delete')
]