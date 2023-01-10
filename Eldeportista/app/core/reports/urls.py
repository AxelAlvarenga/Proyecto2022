from django.urls import path
from core.reports.views import *
urlpatterns = [
 path('sale/', ReportSaleView.as_view() , name='sale_report'),
 path('buy/', ReportBuyView.as_view() , name='buy_report')

 ]