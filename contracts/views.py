from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from core.classes.base import CustomListView, CustomCreateView
from .models import Contract, Invoice

class ContractListView(LoginRequiredMixin, CustomListView):
    model = Contract
    template_name = 'core/list.html'
    ordering = ['-created_at']
    available_columns = {
        'ID': 'id',
        'Nombre cliente': 'client__first_name',
        'Apellido cliente': 'client__last_name',
        'Auto': 'car__plate',
        'Monto semanal': 'weekly_fee',
        'Cantidad de semanas': 'total_weeks',
        'Fecha de inicio': 'start_date',
        'Estado': 'is_active',
    }
    default_columns = ['client__first_name', 'client__last_name', 'car__plate', 'weekly_fee', 'total_weeks', 'start_date']
    create_url = 'contracts:create'

class ContractCreateView(LoginRequiredMixin, CustomCreateView):
    model = Contract
    fields = ['client', 'car', 'weekly_fee', 'total_weeks', 'start_date', 'is_active']
    success_url = 'contracts:list'
    title = 'Crear nuevo contrato'

class InvoiceListView(LoginRequiredMixin, CustomListView):
    model = Invoice
    template_name = 'core/list.html'
    ordering = ['-created_at']
    available_columns = {
        'ID': 'id',
        'Contrato': 'contract__id',
        'Monto': 'amount',
        'Número de cuota': 'installment_number',
        'Fecha de vencimiento': 'due_date',
        'Fecha de pago': 'payment_date',
    }
    default_columns = ['contract__id', 'amount', 'installment_number', 'due_date', 'payment_date']
    create_url = 'contracts:invoice-create'