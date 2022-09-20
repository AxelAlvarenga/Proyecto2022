from unicodedata import category
from django.shortcuts import render
from core.erp.models import Category
def category_list(request):
    data = {
        "title" : "Listado de Productos",
        "categories" : Category.objects.all()
    }
    return render(request,'categoria/list.html', data )