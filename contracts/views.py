from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from core.classes.base import CustomListView
from .models import Contract

class ContractListView(LoginRequiredMixin, CustomListView):
    model = Contract
    template_name = 'core/list.html'
    ordering = ['-created_at']
    available_columns = {
        'ID': 'id',
        'Nombre del cliente': 'client__first_name',
        'Apellido del cliente': 'client__last_name',
        'Auto': 'car__plate',
        'Monto semanal': 'weekly_fee',
        'Cantidad de semanas': 'total_weeks',
        'Fecha de inicio': 'start_date',
        'Estado': 'is_active',
    }
    default_columns = ['id', 'client__first_name', 'car__plate', 'weekly_fee', 'total_weeks', 'start_date', 'is_active']

