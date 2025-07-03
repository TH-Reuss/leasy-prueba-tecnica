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
from contracts.models import Contract, Invoice
from contracts.services import ContractService
from django.core.exceptions import ValidationError
import pandas as pd

class BulkUploadView(LoginRequiredMixin, View):
    success_url = reverse_lazy('analytics:index')
    origin_url  = reverse_lazy('analytics:index')

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

    def _validate_extension(self, file, request):
        name = file.name.lower()
        if not (name.endswith('.csv') or name.endswith('.xlsx')):
            messages.error(request, "Solo se admiten archivos .csv o .xlsx.")
            return redirect(self.origin_url)
        
    def _validate_headers(self, headers, request):
        missing = self.required_cols - set(headers)
        if missing:
            messages.error(
                request,
                f"Faltan columnas requeridas: {', '.join(missing)}"
            )
            return redirect(self.origin_url)
        
    def _parse_excel(self, file):
        df = pd.read_excel(file)
        df = df.fillna('')
        headers = df.columns.tolist()
        rows = df.to_dict(orient='records')
        return headers, rows
    
    def _parse_csv(self, file):
        decoded = io.TextIOWrapper(file, encoding='utf-8')
        reader = csv.DictReader(decoded)
        headers = reader.fieldnames or []
        rows = list(reader)
        return headers, rows
    
    def _validate_empty_rows(self, raw_rows, request):
        valid_rows = []
        row_errors = []

        for idx, row in enumerate(raw_rows, start=2):
            empty_fields = [col for col in self.required_cols if not str(row.get(col, '')).strip()]
            if empty_fields:
                for col in empty_fields:
                    row_errors.append(f"Fila {idx}: '{col}' está vacío")
            else:
                valid_rows.append(row)

        return valid_rows, row_errors


    def post(self, request, *args, **kwargs):
        file = request.FILES.get('file')
        if not file:
            messages.error(request, "Debes cargar un archivo.")
            return redirect(self.origin_url)

        self._validate_extension(file, request)

        try:
            if file.name.endswith('.csv'):
                headers, raw_rows = self._parse_csv(file)
            else:
                headers, raw_rows = self._parse_excel(file)
        except Exception as e:
            messages.error(request, f"No se pudo leer el archivo: {str(e)}")
            return redirect(self.origin_url)


        self._validate_headers(headers, request)

        rows, row_errors = self._validate_empty_rows(raw_rows, request)

        if row_errors:
            for e in row_errors:
                messages.error(request, e)
            return redirect(self.origin_url)
        
        service = ContractService()

        try:
            with transaction.atomic():
                for idx, row in enumerate(rows, start=2):
                    client, _ = Client.objects.get_or_create(
                        dni=str(row['Número de documento']).strip(),
                        defaults={
                            'first_name': str(row['Nombres']).strip(),
                            'last_name': str(row['Apellidos']).strip(),
                        }
                    )

                    car_brand, _ = CarBrand.objects.get_or_create(name=str(row['Marca del auto']).strip())
                    car_model, _ = CarModel.objects.get_or_create(
                        name=str(row['Modelo del auto']).strip(),
                        brand=car_brand
                    )
                    start_date = parse_date(str(row['Inicio de contrato']).strip())

                    car, _ = Car.objects.get_or_create(
                        plate=str(row['Placa del auto']).strip(),
                        defaults={
                            'model': car_model,
                            'manufacture_date': start_date or None,
                        }
                    )

                    weekly_fee = Decimal(str(row['Cuota semanal']).strip())
                    total_weeks = int(str(row.get('Cantidad de semanas', '1')).strip())

                    service.create_contract(
                        client=client,
                        car=car,
                        weekly_fee=weekly_fee,
                        total_weeks=total_weeks,
                        start_date=start_date
                    )

            messages.success(request, f"Se importaron {len(rows)} contratos correctamente.")

        except ValidationError as e:
            messages.error(request, f"Error en fila {idx}: {str(e)}")
        except Exception as e:
            messages.error(request, f"Error inesperado: {str(e)}")

        return redirect(self.success_url)

