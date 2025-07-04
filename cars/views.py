from django.shortcuts import render
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.utils.http import urlencode
from django.db import transaction
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Car, CarBrand, CarModel
from django.contrib.auth.mixins import LoginRequiredMixin
from core.classes.base import CustomDeleteView, CustomListView, CustomCreateView, CustomUpdateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

class CarListView(LoginRequiredMixin, CustomListView):
    model = Car
    template_name = 'core/list.html'
    ordering = ['-created_at']
    available_columns = {
        'ID': 'id',
        'Placa': 'plate',
        'Marca': 'model__brand__name',
        'Modelo': 'model__name',
        'Fecha de fabricación': 'manufacture_date',
    }
    default_columns = ['plate', 'model__brand__name', 'model__name', 'manufacture_date']
    create_url = 'cars:create'
    update_url = 'cars:update'

class CarCreateView(LoginRequiredMixin, CustomCreateView):
    model = Car
    fields = ['plate', 'model', 'manufacture_date']
    success_url = 'cars:list'
    title = 'Crear nuevo auto'

class CarUpdateView(LoginRequiredMixin, CustomUpdateView):
    model = Car
    fields = ['plate', 'model', 'manufacture_date']
    success_url = 'cars:list'
    title = 'Editar auto'
    delete_url = 'cars:delete'

class CarDeleteView(LoginRequiredMixin, CustomDeleteView):
    model = Car
    success_url = 'cars:list'

class CarBrandListView(LoginRequiredMixin, CustomListView):
    model = CarBrand
    template_name = 'core/list.html'
    ordering = ['-created_at']
    available_columns = {
        'ID': 'id',
        'Nombre': 'name',
    }
    default_columns = ['name']
    create_url = 'cars:brand-create'
    update_url = 'cars:brand-update'

class CarBrandCreateView(LoginRequiredMixin, CustomCreateView):
    model = CarBrand
    fields = ['name']
    success_url = 'cars:brand-list'
    title = 'Crear nueva marca'

class CarBrandUpdateView(LoginRequiredMixin, CustomUpdateView):
    model = CarBrand
    fields = ['name']
    success_url = 'cars:brand-list'
    title = 'Editar marca'
    delete_url = 'cars:brand-delete'

class CarBrandDeleteView(LoginRequiredMixin, CustomDeleteView):
    model = CarBrand
    success_url = 'cars:brand-list'

class CarModelListView(LoginRequiredMixin, CustomListView):
    model = CarModel
    template_name = 'core/list.html'
    ordering = ['-created_at']
    available_columns = {
        'ID': 'id',
        'Nombre': 'name',
        'Marca': 'brand__name',
    }
    default_columns = ['name', 'brand__name']
    create_url = 'cars:model-create'
    update_url = 'cars:model-update'

class CarModelCreateView(LoginRequiredMixin, CustomCreateView):
    model = CarModel
    fields = ['name', 'brand']
    success_url = 'cars:model-list'
    title = 'Crear nuevo modelo'

class CarModelUpdateView(LoginRequiredMixin, CustomUpdateView):
    model = CarModel
    fields = ['name', 'brand']
    success_url = 'cars:model-list'
    title = 'Editar modelo'
    delete_url = 'cars:model-delete'

class CarModelDeleteView(LoginRequiredMixin, CustomDeleteView):
    model = CarModel
    success_url = 'cars:model-list'