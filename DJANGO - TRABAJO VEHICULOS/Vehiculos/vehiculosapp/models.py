from django.db import models

class Vehiculo(models.Model):
    numero_placa = models.CharField(max_length=20)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.marca} {self.modelo} - {self.numero_placa}"
