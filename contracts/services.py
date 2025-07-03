from contracts.models import Contract, Invoice
from datetime import timedelta
from django.db import transaction
from django.core.exceptions import ValidationError

class ContractService:

    def create_contract(self, client, car, weekly_fee, total_weeks, start_date):
        if Contract.objects.filter(client=client, is_active=True).exists():
            raise ValidationError("El cliente ya tiene un contrato activo")
        
        if Contract.objects.filter(car=car, is_active=True).exists():
            raise ValidationError("El vehiculo ya tiene un contrato activo")
        
        if total_weeks <= 0:
            raise ValidationError("El numero de semanas debe ser mayor a 0")
        
        if weekly_fee <= 0:
            raise ValidationError("El monto de la cuota semanal debe ser mayor a 0")

        try:
            contract = Contract.objects.create(client=client, car=car, weekly_fee=weekly_fee, total_weeks=total_weeks, start_date=start_date)
        except Exception as e:
            raise ValidationError("Error al crear el contrato")
        
        self._create_invoice(contract)
        return contract

    def delete_contract(self, contract):
        contract.is_active = False
        contract.save()
        self._delete_contract_invoices(contract)
        contract.delete()
        return contract
    
    def _create_invoice(self, contract):
        try:
            for i in range(1, contract.total_weeks + 1):
                Invoice.objects.create(contract=contract, installment_number=i, due_date=contract.start_date + timedelta(days=i * 7), amount=contract.weekly_fee)
        except Exception as e:
            raise ValidationError("Error al crear las facturas")
    
    def _delete_contract_invoices(self, contract):
        try:
            invoices = Invoice.objects.filter(contract=contract)
            invoices.delete()
        except Exception as e:
            raise ValidationError("Error al eliminar las facturas del contrato")