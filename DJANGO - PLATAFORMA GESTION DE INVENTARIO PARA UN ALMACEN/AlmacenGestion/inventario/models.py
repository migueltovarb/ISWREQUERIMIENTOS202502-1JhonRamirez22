from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal
import barcode
from barcode.writer import ImageWriter
from io import BytesIO
import os

class Producto(models.Model):
    COLORES = [
        ('ROJO', 'Rojo'),
        ('AZUL', 'Azul'),
        ('NEGRO', 'Negro'),
        ('BLANCO', 'Blanco'),
        ('GRIS', 'Gris'),
        ('VERDE', 'Verde'),
    ]

    CATEGORIAS = [
        ('ELECTRONICA', 'Electrónica'),
        ('HERRAMIENTAS', 'Herramientas'),
        ('VEHICULOS', 'Vehículos'),
        ('OFICINA', 'Oficina'),
        ('OTROS', 'Otros'),
    ]

    codigo = models.CharField(max_length=20, unique=True, verbose_name='Código de Producto')
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    marca = models.CharField(max_length=100, verbose_name='Marca del Producto')
    color = models.CharField(max_length=20, choices=COLORES, verbose_name='Color')
    categoria = models.CharField(max_length=50, choices=CATEGORIAS, default='OTROS', verbose_name='Categoría')
    stock = models.IntegerField(default=0, validators=[MinValueValidator(0)], verbose_name='Stock Disponible')
    stock_minimo = models.IntegerField(default=5, validators=[MinValueValidator(0)], verbose_name='Stock Mínimo')
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'), verbose_name='Precio Unitario')
    descripcion = models.TextField(blank=True, null=True, verbose_name='Descripción')
    codigo_barras = models.CharField(max_length=13, unique=True, blank=True, null=True, verbose_name='Código de Barras')
    proveedor = models.ForeignKey('Proveedor', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Proveedor')
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['-fecha_creacion']

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"

    @property
    def estado_stock(self):
        if self.stock == 0:
            return 'CRÍTICA'
        elif self.stock < self.stock_minimo:
            return 'ALTA'
        else:
            return 'NORMAL'


class Rol(models.Model):
    ROLES_OPCIONES = [
        ('administrador', 'Administrador'),
        ('gerente', 'Gerente'),
        ('operario', 'Operario'),
    ]

    nombre = models.CharField(max_length=100, verbose_name='Nombre del Usuario')
    correo = models.EmailField(verbose_name='Correo Electrónico')
    cargo = models.CharField(max_length=50, verbose_name='Cargo')
    rol = models.CharField(max_length=20, choices=ROLES_OPCIONES, verbose_name='Rol')
    activo = models.BooleanField(default=True, verbose_name='Activo')
    fecha_registro = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Registro')

    class Meta:
        verbose_name = 'Rol/Usuario'
        verbose_name_plural = 'Roles/Usuarios'

    def __str__(self):
        return f"{self.nombre} - {self.get_rol_display()}"


class Alerta(models.Model):
    ESTADOS_ALERTA = [
        ('activa', 'Activa'),
        ('resuelta', 'Resuelta'),
        ('ignorada', 'Ignorada'),
    ]

    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name='Producto')
    tipo = models.CharField(max_length=20, default='stock_bajo', verbose_name='Tipo de Alerta')
    estado = models.CharField(max_length=20, choices=ESTADOS_ALERTA, default='activa', verbose_name='Estado')
    descripcion = models.TextField(blank=True, default='', verbose_name='Descripción')
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    fecha_resolucion = models.DateTimeField(null=True, blank=True, verbose_name='Fecha de Resolución')

    class Meta:
        verbose_name = 'Alerta'
        verbose_name_plural = 'Alertas'
        ordering = ['-fecha_creacion']

    def __str__(self):
        return f"Alerta {self.producto.codigo} - {self.estado}"


class Movimiento(models.Model):
    TIPOS_MOVIMIENTO = [
        ('entrada', 'Entrada de Stock'),
        ('salida', 'Salida de Stock'),
        ('ajuste', 'Ajuste de Inventario'),
        ('devolución', 'Devolución'),
    ]

    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name='Producto')
    tipo = models.CharField(max_length=20, choices=TIPOS_MOVIMIENTO, verbose_name='Tipo de Movimiento')
    cantidad = models.IntegerField(validators=[MinValueValidator(1)], verbose_name='Cantidad')
    usuario = models.CharField(max_length=100, verbose_name='Usuario que Realizó Movimiento')
    descripcion = models.TextField(blank=True, default='', verbose_name='Descripción/Observaciones')
    fecha = models.DateTimeField(auto_now_add=True, verbose_name='Fecha del Movimiento')
    stock_anterior = models.IntegerField(verbose_name='Stock Anterior')
    stock_posterior = models.IntegerField(verbose_name='Stock Posterior')

    class Meta:
        verbose_name = 'Movimiento'
        verbose_name_plural = 'Movimientos'
        ordering = ['-fecha']

    def __str__(self):
        return f"{self.producto.codigo} - {self.get_tipo_display()} - {self.cantidad} unidades"


class Proveedor(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Nombre del Proveedor')
    contacto = models.CharField(max_length=100, verbose_name='Contacto')
    email = models.EmailField(verbose_name='Correo Electrónico')
    telefono = models.CharField(max_length=20, verbose_name='Teléfono')
    direccion = models.TextField(verbose_name='Dirección')
    ciudad = models.CharField(max_length=100, verbose_name='Ciudad')
    pais = models.CharField(max_length=100, verbose_name='País')
    activo = models.BooleanField(default=True, verbose_name='Activo')
    fecha_registro = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Registro')

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre
