from django.contrib import admin
from django.urls import path
from core.erp.views import vista1
urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', vista1)
]