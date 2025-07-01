from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from core.classes.base import CustomListView
from .models import Contract, Invoice

class ContractListView(LoginRequiredMixin, CustomListView):
    model = Contract
    template_name = 'core/list.html'
    ordering = ['-created_at']
    available_columns = {
        
        'Nombre cliente': 'client__first_name',
        'Apellido cliente': 'client__last_name',
        'Auto': 'car__plate',
        'Monto semanal': 'weekly_fee',
        'Cantidad de semanas': 'total_weeks',
        'Fecha de inicio': 'start_date',
        'Estado': 'is_active',
    }
    default_columns = ['client__first_name', 'client__last_name', 'car__plate', 'weekly_fee', 'total_weeks', 'start_date']

class InvoiceListView(LoginRequiredMixin, CustomListView):
    model = Invoice
    template_name = 'core/list.html'
    ordering = ['-created_at']
    available_columns = {
        'Contrato': 'contract__id',
        'Monto': 'amount',
        'Número de cuota': 'installment_number',
        'Fecha de vencimiento': 'due_date',
        'Fecha de pago': 'payment_date',
    }