# uploads/views.py
import csv, io
from django.views import View
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.db import transaction
from django.contrib.auth.mixins import LoginRequiredMixin

from clients.models import Client  # o el modelo que uses

class BulkUploadView(LoginRequiredMixin, View):
    success_url   = reverse_lazy('dashboard:home')

    def post(self, request, *args, **kwargs):
        # 1. Extraer el archivo
        file = request.FILES.get('file')
        if not file:
            messages.error(request, "Debes seleccionar un archivo.")
            return render(request, self.template_name, {})

        name = file.name.lower()
        if not (name.endswith('.csv') or name.endswith('.xlsx')):
            messages.error(request, "Solo se admiten archivos .csv o .xlsx.")
            return render(request, self.template_name, {})

        # 2. Leer y validar encabezados
        try:
            decoded = io.TextIOWrapper(file, encoding='utf-8')
            data = csv.DictReader(decoded)
        except Exception:
            messages.error(request, "No se pudo leer el archivo CSV.")
            return render(request, self.template_name, {})

        required_cols = {'name', 'document', 'registration_date'}
        missing = required_cols - set(data.fieldnames or [])
        if missing:
            messages.error(
               request,
               f"Faltan columnas requeridas: {', '.join(missing)}"
            )
            return render(request, self.template_name, {})

        # 3. Validar filas
        rows, row_errors = [], []
        for idx, row in enumerate(data, start=2):
            if not row['name'].strip():
                row_errors.append(f"Fila {idx}: 'name' vacío")
            if not row['document'].strip():
                row_errors.append(f"Fila {idx}: 'document' vacío")
            else:
                rows.append(row)

        if row_errors:
            for e in row_errors:
                messages.error(request, e)
            return render(request, self.template_name, {})

        # 4. Bulk insert en transacción
        objs = [
            Client(
                name=row['name'].strip(),
                document=row['document'].strip(),
                registration_date=row['registration_date']
            )
            for row in rows
        ]
        try:
            with transaction.atomic():
                Client.objects.bulk_create(objs, batch_size=500)
            messages.success(
                request,
                f"Se importaron {len(objs)} registros correctamente."
            )
        except Exception as e:
            messages.error(
                request,
                f"Error al guardar en la base de datos: {e}"
            )

        return redirect(self.success_url)
