
from django.urls import path
from core.erp.views.category.views import *

app_name='erp'
urlpatterns = [
    path('producto/list', ProductoListView.as_view() , name='template_list')
]