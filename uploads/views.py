# uploads/views.py
from datetime import timedelta
import csv, io
from decimal import Decimal
from django.views import View
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.db import transaction
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.dateparse import parse_date
from clients.models import Client
from cars.models import Car, CarBrand, CarModel
from contracts.models import Contract
from invoices.models import Invoice


class BulkUploadView(LoginRequiredMixin, View):
    success_url = reverse_lazy('analytics:index')
    origin_url  = reverse_lazy('analytics:index')

    # Columnas que esperamos EXACTAMENTE en el CSV
    required_cols = {
        'Nombres',
        'Apellidos',
        'Número de documento',
        'Inicio de contrato',
        'Cuota semanal',
        'Marca del auto',
        'Modelo del auto',
        'Placa del auto',
    }

    def validate_extension(self, file, request):
        name = file.name.lower()
        if not (name.endswith('.csv') or name.endswith('.xlsx')):
            messages.error(request, "Solo se admiten archivos .csv o .xlsx.")
            return redirect(self.origin_url)
        
    def validate_headers(self, data, request):
        missing = self.required_cols - set(data.fieldnames or [])
        if missing:
            messages.error(
                request,
                f"Faltan columnas requeridas: {', '.join(missing)}"
            )
            return redirect(self.origin_url)

    def post(self, request, *args, **kwargs):
        file = request.FILES.get('file')
        if not file:
            messages.error(request, "Debes cargar un archivo.")
            return redirect(self.origin_url)

        self.validate_extension(file, request)

        try:
            decoded = io.TextIOWrapper(file, encoding='utf-8')
            data = csv.DictReader(decoded)
        except Exception:
            messages.error(request, "No se pudo leer el archivo CSV.")
            return redirect(self.origin_url)

        self.validate_headers(data, request)

        rows, row_errors = [], []
        for idx, row in enumerate(data, start=2):
            # Campos obligatorios no vacíos
            for col in self.required_cols:
                if not row[col].strip():
                    row_errors.append(f"Fila {idx}: '{col}' está vacío")
            if not row_errors:
                rows.append(row)

        if row_errors:
            for e in row_errors:
                messages.error(request, e)
            return redirect(self.origin_url)

        # Preparar contratos para bulk_create
        contract_objs = []
        for row in rows:
            # 1) Client
            client, _ = Client.objects.get_or_create(
                dni=row['Número de documento'].strip(),
                defaults={
                    'first_name': row['Nombres'].strip(),
                    'last_name':  row['Apellidos'].strip(),
                }
            )

            car_brand, _ = CarBrand.objects.get_or_create(
                name=row['Marca del auto']
            )
            car_model, _ = CarModel.objects.get_or_create(
                name=row['Modelo del auto'],
                brand=car_brand
            )

            start_date = parse_date(row['Inicio de contrato'].strip())
            car, _ = Car.objects.get_or_create(
                plate=row['Placa del auto'].strip(),
                defaults={
                    'brand': car_brand,
                    'model': car_model,
                    'manufacture_date': start_date or None,
                }
            )
            weekly_fee = Decimal(row['Cuota semanal'].strip())
            # Si tuvieras una columna 'Cantidad de semanas', la parseas aquí:
            total_weeks = int(row.get('Cantidad de semanas', '1').strip())
            contract_objs.append(
                Contract(
                    client=client,
                    car=car,
                    weekly_fee=weekly_fee,
                    total_weeks=total_weeks,
                    start_date=start_date,
                    is_active=True,
                )
            )

        invoice_objs = []
        for contract in contract_objs:
            for i in range(1, contract.total_weeks + 1):
                invoice_objs.append(
                    Invoice(
                        contract=contract,
                        amount=contract.weekly_fee,
                    installment_number=i,
                        due_date=contract.start_date + timedelta(days=i * 7),
                    )
                )

        try:
            with transaction.atomic():
                Contract.objects.bulk_create(contract_objs, batch_size=500)
            messages.success(
                request,
                f"Se importaron {len(contract_objs)} contratos correctamente."
            )
        except Exception as e:
            messages.error(
                request,
                f"Error al guardar en la base de datos: {e}"
            )

        return redirect(self.success_url)
