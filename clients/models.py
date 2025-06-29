from django.db import models
from django.utils import timezone
from core.models import BaseModel

class Client(BaseModel):
    name = models.CharField("Nombre", max_length=150)
    last_name = models.CharField("Apellido", max_length=150)
    dni = models.CharField("DNI", max_length=50, unique=True)

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"

    def __str__(self):
        return f"{self.name} ({self.document})"