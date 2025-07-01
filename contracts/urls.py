from django.urls import path
from .views import ContractListView, InvoiceListView

app_name = 'contracts'

urlpatterns = [
    path('',  ContractListView.as_view(),  name='list'),
    path('invoices/',  InvoiceListView.as_view(),  name='invoice-list'),
]