from django.db import models
from core.models import BaseModel

class Car(BaseModel):
    plate = models.CharField("Placa", max_length=20, unique=True)
    model = models.CharField("Modelo", max_length=100)
    brand = models.CharField("Marca", max_length=100)
    manufacture_date = models.DateField("Fecha de fabricación")

    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"

    def __str__(self):
        return f"{self.brand} {self.model} ({self.plate})"