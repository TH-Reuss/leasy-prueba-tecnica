from django.db import models
from django.utils import timezone
from core.models import BaseModel
from contracts.models import Contract

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
        verbose_name = "Invoice"
        verbose_name_plural = "Invoices"
        ordering = ['due_date']

    def __str__(self):
        return f"Invoice {self.installment_number} - Contract {self.contract_id}"
