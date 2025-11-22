from django import forms
from .models import Producto, Rol, Proveedor

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['codigo', 'nombre', 'marca', 'color', 'categoria', 'stock', 'stock_minimo', 'precio', 'descripcion', 'proveedor']
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Código'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del Producto'}),
            'marca': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Marca'}),
            'color': forms.Select(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'stock_minimo': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'proveedor': forms.Select(attrs={'class': 'form-control'}),
        }

class ActualizarStockForm(forms.Form):
    OPERACIONES = [
        ('agregar', 'Agregar al stock'),
        ('restar', 'Restar del stock'),
    ]
    cantidad = forms.IntegerField(min_value=1, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cantidad'}))
    operacion = forms.ChoiceField(choices=OPERACIONES, widget=forms.Select(attrs={'class': 'form-control'}))

class RolForm(forms.ModelForm):
    class Meta:
        model = Rol
        fields = ['nombre', 'correo', 'cargo', 'rol', 'activo']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo'}),
            'cargo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cargo'}),
            'rol': forms.Select(attrs={'class': 'form-control'}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class HistorialSearchForm(forms.Form):
    TIPOS = [
        ('', 'Todos'),
        ('entrada', 'Entrada'),
        ('salida', 'Salida'),
        ('ajuste', 'Ajuste'),
        ('devolución', 'Devolución'),
    ]
    fecha_desde = forms.DateField(required=False, widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    fecha_hasta = forms.DateField(required=False, widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    tipo = forms.ChoiceField(required=False, choices=TIPOS, widget=forms.Select(attrs={'class': 'form-control'}))
    producto = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Código de Producto'}))

class BuscarProductoForm(forms.Form):
    codigo = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Código'}))
    nombre = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}))
    marca = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Marca'}))

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'contacto', 'email', 'telefono', 'direccion', 'ciudad', 'pais', 'activo']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del Proveedor'}),
            'contacto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contacto'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}),
            'direccion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Dirección completa'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ciudad'}),
            'pais': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'País'}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
