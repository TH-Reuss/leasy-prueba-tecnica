from django.db import models
from core.models import BaseModel

class CarBrand(BaseModel):
    name = models.CharField("Marca", max_length=100)

    class Meta:
        verbose_name = "Car Brand"
        verbose_name_plural = "Car Brands"

    def __str__(self):
        return self.name

class CarModel(BaseModel):
    name = models.CharField("Modelo", max_length=100)
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Car Model"
        verbose_name_plural = "Car Models"

    def __str__(self):
        return f"{self.brand.name} {self.name}"
    
class Car(BaseModel):
    plate = models.CharField("Placa", max_length=20, unique=True)
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    manufacture_date = models.DateField("Fecha de fabricación")

    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"

    def __str__(self):
        return f"{self.brand} {self.model} ({self.plate})"
    
