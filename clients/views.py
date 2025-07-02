from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from core.classes.base import CustomListView, CustomCreateView, CustomUpdateView, CustomDeleteView
from .models import Client

class ClientListView(LoginRequiredMixin, CustomListView):
    model = Client
    template_name = 'core/list.html'
    ordering = ['-created_at']
    available_columns = {
        'ID': 'id',
        'DNI': 'dni',   
        'Nombre': 'first_name',
        'Apellido': 'last_name',
    }
    default_columns = ['dni', 'first_name', 'last_name']
    create_url = 'clients:create'
    update_url = 'clients:update'

class ClientCreateView(LoginRequiredMixin, CustomCreateView):
    model = Client
    fields = ['first_name', 'last_name', 'dni']
    success_url = 'clients:list'
    title = 'Crear nuevo cliente'

class ClientUpdateView(LoginRequiredMixin, CustomUpdateView):
    model = Client
    fields = ['first_name', 'last_name', 'dni']
    success_url = 'clients:list'
    title = 'Editar cliente'
    delete_url = 'clients:delete'

class ClientDeleteView(LoginRequiredMixin, CustomDeleteView):
    model = Client
    success_url = 'clients:list'
    title = 'Eliminar cliente'
    delete_url = 'clients:delete'