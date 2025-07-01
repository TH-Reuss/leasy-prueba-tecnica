from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from core.classes.base import CustomListView, CustomCreateView
from .models import Client

class ClientListView(LoginRequiredMixin, CustomListView):
    model = Client
    template_name = 'core/list.html'
    ordering = ['-created_at']
    available_columns = {
        'DNI': 'dni',   
        'Nombre': 'first_name',
        'Apellido': 'last_name',
    }
    default_columns = ['dni', 'first_name', 'last_name']
    create_url = 'clients:create'

class ClientCreateView(LoginRequiredMixin, CustomCreateView):
    model = Client
    fields = ['first_name', 'last_name', 'dni']
    success_url = 'clients:list'
    title = 'Crear nuevo cliente'

