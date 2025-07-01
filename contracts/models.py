from django.db import models
from django.utils import timezone
from django.db.models import Q
from core.models import BaseModel
from clients.models import Client
from cars.models import Car

class Contract(BaseModel):
    client = models.ForeignKey(
        Client,
        on_delete=models.PROTECT,
        related_name='contracts'
    )
    car = models.ForeignKey(
        Car,
        on_delete=models.PROTECT,
        related_name='contracts'
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
                condition=Q(is_active=True, deleted_at__isnull=True),
                name='unique_active_contract_per_client'
            ),
            models.UniqueConstraint(
                fields=['car'],
                condition=Q(is_active=True, deleted_at__isnull=True),
                name='unique_active_contract_per_car'
            ),
        ]

    def __str__(self):
        return f"Contrato #{self.id} - {self.client.first_name} {self.client.last_name} / {self.car.plate}"