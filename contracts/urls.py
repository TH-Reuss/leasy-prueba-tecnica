from django.urls import path
from .views import (
    ContractListView,
    ContractCreateView,
    InvoiceListView,
)

app_name = 'contracts'

urlpatterns = [
    path('',  ContractListView.as_view(),  name='list'),
    path('create/',  ContractCreateView.as_view(),  name='create'),
    path('invoices/',  InvoiceListView.as_view(),  name='invoice-list'),
]