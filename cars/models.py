from django.db import models
from core.models import BaseModel

class CarBrand(BaseModel):
    cascade_delete_relations = ['cars_brand']

    name = models.CharField("Marca", max_length=100)

    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"

    def __str__(self):
        return self.name

class CarModel(BaseModel):
    name = models.CharField("Modelo", max_length=100)
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE, related_name='cars_brand')

    class Meta:
        verbose_name = "Modelo"
        verbose_name_plural = "Modelos"

    def __str__(self):
        return f"{self.brand.name} {self.name}"
    
class Car(BaseModel):
    protected_relations = ['contracts']

    plate = models.CharField("Placa", max_length=20, unique=True)
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='cars_model')
    manufacture_date = models.DateField("Fecha de fabricación")

    class Meta:
        verbose_name = "Auto"
        verbose_name_plural = "Autos"

    def __str__(self):
        return f"{self.model.brand.name} {self.model.name} ({self.plate})"

    
