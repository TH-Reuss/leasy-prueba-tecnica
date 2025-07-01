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
from core.classes.base import CustomListView


class CarListView(LoginRequiredMixin, CustomListView):
    model = Car
    template_name = 'core/list.html'
    ordering = ['-created_at']
    available_columns = {
        'Placa': 'plate',
        'Marca': 'brand__name',
        'Modelo': 'model__name',
        'Fecha de fabricación': 'manufacture_date',
    }
    default_columns = ['plate', 'brand__name', 'model__name', 'manufacture_date']

class CarBrandListView(LoginRequiredMixin, CustomListView):
    model = CarBrand
    template_name = 'core/list.html'
    ordering = ['-created_at']
    available_columns = {
        'Nombre': 'name',
    }
    default_columns = ['name']
    
class CarModelListView(LoginRequiredMixin, CustomListView):
    model = CarModel
    template_name = 'core/list.html'
    ordering = ['-created_at']
    available_columns = {
        'Nombre': 'name',
        'Marca': 'brand__name',
    }
    default_columns = ['name', 'brand__name']