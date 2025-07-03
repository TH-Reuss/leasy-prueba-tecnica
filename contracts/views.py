from django.contrib import messages
from django.forms import ValidationError
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from contracts.services import ContractService
from core.classes.base import CustomListView, CustomCreateView, CustomUpdateView, CustomDeleteView
from .models import Contract, Invoice

class ContractListView(LoginRequiredMixin, CustomListView):
    model = Contract
    template_name = 'core/list.html'
    ordering = ['-created_at']
    available_columns = {
        'ID': 'id',
        'Nombre cliente': 'client__first_name',
        'Apellido cliente': 'client__last_name',
        'Marca del auto': 'car__model__brand__name',
        'Modelo del auto': 'car__model__name',
        'Auto': 'car__plate',
        'Monto semanal': 'weekly_fee',
        'Cantidad de semanas': 'total_weeks',
        'Fecha de inicio': 'start_date',
        'Estado': 'is_active',
    }
    default_columns = ['client__first_name', 'client__last_name', 'car__plate', 'weekly_fee', 'total_weeks', 'start_date']
    create_url = 'contracts:create'
    update_url = 'contracts:update'

class ContractCreateView(LoginRequiredMixin, CustomCreateView):
    model = Contract
    success_url = 'contracts:list'
    title = 'Crear nuevo contrato'
    fields = ['client', 'car', 'weekly_fee', 'total_weeks', 'start_date']

    def form_valid(self, form):
        service = ContractService()

        try:
            contract = service.create_contract(
                client=form.cleaned_data['client'],
                car=form.cleaned_data['car'],
                weekly_fee=form.cleaned_data['weekly_fee'],
                total_weeks=form.cleaned_data['total_weeks'],
                start_date=form.cleaned_data['start_date'],
            )
            messages.success(self.request, "Contrato creado con éxito.")
            return redirect(self.get_success_url())

        except ValidationError as e:
            messages.error(self.request, str(e))
            return self.form_invalid(form)

        except Exception as e:
            messages.error(self.request, "Error inesperado al crear el contrato.")
            return self.form_invalid(form)


class ContractUpdateView(LoginRequiredMixin, CustomUpdateView):
    model = Contract
    success_url = 'contracts:list'
    title = 'Editar contrato'
    fields = ['weekly_fee', 'total_weeks', 'start_date', 'is_active']
    delete_url = 'contracts:delete'

class ContractDeleteView(LoginRequiredMixin, CustomDeleteView):
    model = Contract
    success_url = 'contracts:list'
    title = 'Eliminar contrato'
    delete_url = 'contracts:delete'

    def post(self, request, *args, **kwargs):
        contract = self.get_object()
        try:
            service = ContractService()
            service.delete_contract(contract)
            messages.success(request, "Contrato eliminado con éxito.")
        except ValidationError as e:
            messages.error(request, str(e))
        except Exception as e:
            messages.error(request, "Error inesperado al eliminar el contrato.")
        return redirect(self.get_success_url())


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