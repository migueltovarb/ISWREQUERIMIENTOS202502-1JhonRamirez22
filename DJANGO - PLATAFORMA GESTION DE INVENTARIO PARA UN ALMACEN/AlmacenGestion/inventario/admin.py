from django.contrib import admin
from .models import Producto, Movimiento, Alerta, Rol, Proveedor

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'marca', 'stock', 'stock_minimo', 'estado_stock', 'proveedor')
    list_filter = ('categoria', 'color', 'proveedor')
    search_fields = ('codigo', 'nombre', 'marca')
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion')
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('codigo', 'nombre', 'marca', 'color', 'categoria')
        }),
        ('Stock', {
            'fields': ('stock', 'stock_minimo')
        }),
        ('Precio y Proveedor', {
            'fields': ('precio', 'proveedor')
        }),
        ('Código de Barras', {
            'fields': ('codigo_barras',)
        }),
        ('Descripción', {
            'fields': ('descripcion',)
        }),
        ('Fechas', {
            'fields': ('fecha_creacion', 'fecha_actualizacion'),
            'classes': ('collapse',)
        }),
    )

@admin.register(Movimiento)
class MovimientoAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'producto', 'tipo', 'cantidad', 'usuario', 'stock_anterior', 'stock_posterior')
    list_filter = ('tipo', 'fecha', 'producto')
    search_fields = ('producto__codigo', 'usuario')
    readonly_fields = ('fecha', 'stock_anterior', 'stock_posterior')
    
    fieldsets = (
        ('Información del Movimiento', {
            'fields': ('producto', 'tipo', 'cantidad', 'usuario')
        }),
        ('Stock', {
            'fields': ('stock_anterior', 'stock_posterior')
        }),
        ('Detalles', {
            'fields': ('descripcion', 'fecha'),
            'classes': ('collapse',)
        }),
    )

@admin.register(Alerta)
class AlertaAdmin(admin.ModelAdmin):
    list_display = ('producto', 'tipo', 'estado', 'fecha_creacion', 'fecha_resolucion')
    list_filter = ('estado', 'tipo', 'fecha_creacion')
    search_fields = ('producto__codigo', 'descripcion')
    readonly_fields = ('fecha_creacion', 'fecha_resolucion')
    
    fieldsets = (
        ('Información de Alerta', {
            'fields': ('producto', 'tipo', 'estado')
        }),
        ('Descripción', {
            'fields': ('descripcion',)
        }),
        ('Fechas', {
            'fields': ('fecha_creacion', 'fecha_resolucion')
        }),
    )

@admin.register(Rol)
class RolAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'rol', 'correo', 'cargo', 'activo', 'fecha_registro')
    list_filter = ('rol', 'activo', 'fecha_registro')
    search_fields = ('nombre', 'correo')
    readonly_fields = ('fecha_registro',)
    
    fieldsets = (
        ('Información Personal', {
            'fields': ('nombre', 'correo', 'cargo')
        }),
        ('Rol y Permisos', {
            'fields': ('rol', 'activo')
        }),
        ('Registro', {
            'fields': ('fecha_registro',),
            'classes': ('collapse',)
        }),
    )

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'contacto', 'email', 'telefono', 'ciudad', 'activo')
    list_filter = ('pais', 'ciudad', 'activo', 'fecha_registro')
    search_fields = ('nombre', 'email', 'telefono')
    readonly_fields = ('fecha_registro',)
    
    fieldsets = (
        ('Información del Proveedor', {
            'fields': ('nombre', 'contacto', 'email', 'telefono')
        }),
        ('Dirección', {
            'fields': ('direccion', 'ciudad', 'pais')
        }),
        ('Estado', {
            'fields': ('activo', 'fecha_registro')
        }),
    )
