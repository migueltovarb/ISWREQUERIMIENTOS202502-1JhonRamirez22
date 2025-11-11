from django import forms
from .models import Vehiculo

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['numero_placa', 'marca', 'modelo', 'color']
        labels = {
            'numero_placa': 'Número de placa',
            'marca': 'Marca del vehículo',
            'modelo': 'Modelo del vehículo',
            'color': 'Color del vehículo',
        }
        widgets = {
            'numero_placa': forms.TextInput(attrs={'class': 'form-control'}),
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'color': forms.Select(attrs={'class': 'form-select'}, choices=[
                ('', '---------'),
                ('ROJO', 'ROJO'),
                ('AZUL', 'AZUL'),
                ('VERDE', 'VERDE'),
               
            ]),
        }
