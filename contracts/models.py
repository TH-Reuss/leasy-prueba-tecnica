from django.db import models
from django.utils import timezone
from django.db.models import Q
from core.models import BaseModel
from clients.models import Client
from cars.models import Car

class Contract(BaseModel):
    cascade_delete_relations = ['invoices']

    client = models.ForeignKey(
        Client,
        on_delete=models.PROTECT,
        related_name='contracts',
        verbose_name='Cliente',
    )
    car = models.ForeignKey(
        Car,
        on_delete=models.PROTECT,
        related_name='contracts',
        verbose_name='Auto',
    )
    weekly_fee = models.DecimalField(
        "Monto semanal",
        max_digits=6,
        decimal_places=2
    )
    total_weeks = models.PositiveIntegerField("Cantidad de semanas")
    start_date = models.DateField("Fecha de inicio")
    is_active = models.BooleanField("Activo", default=True)

    class Meta:
        verbose_name = "Contrato"
        verbose_name_plural = "Contratos"
        constraints = [
            models.UniqueConstraint(
                fields=['client'],
                condition=models.Q(is_active=True, deleted_at__isnull=True),
                name='unique_active_contract_per_client'
            ),
            models.UniqueConstraint(
                fields=['car'],
                condition=models.Q(is_active=True, deleted_at__isnull=True),
                name='unique_active_contract_per_car'
            ),
        ]

    def __str__(self):
        return f"Contrato #{self.id} - {self.client.first_name} {self.client.last_name} / {self.car.plate}"
    
class Invoice(BaseModel):
    contract = models.ForeignKey(
        Contract,
        on_delete=models.CASCADE,
        related_name='invoices'
    )
    amount = models.DecimalField(
        "Monto",
        max_digits=10,
        decimal_places=2
    )
    installment_number = models.PositiveIntegerField("Número de cuota")
    due_date = models.DateField("Fecha de vencimiento")
    payment_date = models.DateField(
        "Fecha de pago",
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "Factura"
        verbose_name_plural = "Facturas"
        ordering = ['due_date']

    def __str__(self):
        return f"Factura {self.installment_number} - Contrato {self.contract_id}"