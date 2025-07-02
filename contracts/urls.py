from django.urls import path
from .views import (
    ContractListView,
    ContractCreateView,
    ContractUpdateView,
    ContractDeleteView,
    InvoiceListView,
)

app_name = 'contracts'

urlpatterns = [
    path('',  ContractListView.as_view(),  name='list'),
    path('create/',  ContractCreateView.as_view(),  name='create'),
    path('update/<uuid:pk>/',  ContractUpdateView.as_view(),  name='update'),
    path('delete/<uuid:pk>/',  ContractDeleteView.as_view(),  name='delete'),
    path('invoices/',  InvoiceListView.as_view(),  name='invoice-list'),
]