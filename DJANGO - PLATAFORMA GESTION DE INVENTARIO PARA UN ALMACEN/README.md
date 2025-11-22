# Sistema de Gestión de Inventario - Django

Aplicación completa para gestionar inventario de almacén con alertas automáticas, códigos de barras y historial de movimientos.

## Características

✅ Alertas automáticas cuando stock está bajo
✅ Generación automática de código de barras EAN13
✅ CRUD completo de productos
✅ Historial de movimientos (Entrada/Salida/Modificación)
✅ Búsqueda avanzada de productos
✅ Gestión de usuarios y roles
✅ Style Tile integrado
✅ Responsive design
✅ Admin panel personalizado
✅ Validaciones completas

## Instalación

### 1. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 2. Configurar settings.py
Agregar 'inventario' a INSTALLED_APPS:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'inventario',  # ← Agregar esta línea
]

# Agregar configuración de media
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

### 3. Realizar migraciones
```bash
python manage.py migrate
```

### 4. Crear superusuario
```bash
python manage.py createsuperuser
```

### 5. Ejecutar servidor
```bash
python manage.py runserver
```

## Acceso

- **Aplicación:** http://localhost:8000/inventario/
- **Admin:** http://localhost:8000/admin/

## URLs principales

- `/inventario/` - Inicio
- `/inventario/productos/` - Listado de productos
- `/inventario/alertas/` - Ver alertas
- `/inventario/historial/` - Historial de movimientos
- `/inventario/buscar/` - Búsqueda de productos
- `/inventario/roles/` - Gestión de usuarios

## Modelos

### Producto
- Código (único)
- Nombre
- Precio
- Stock
- Stock Mínimo
- Código de barras (automático)
- Proveedor
- Categoría, Color, Descripción

### Alerta
- Producto (FK)
- Nivel (Crítica/Alta/Media)
- Fecha de generación
- Estado (Resuelta/Pendiente)

### HistorialMovimiento
- Producto (FK)
- Tipo (Entrada/Salida/Modificación)
- Cantidad
- Fechas de movimiento

### Rol
- Nombre
- Cargo
- Correo
- Rol del sistema

## Características implementadas

### HU1: Recibir Alertas Automáticas
- Alertas cuando stock < stock_mínimo
- Tres niveles: Crítica (Rojo), Alta (Naranja), Media (Amarillo)
- Interfaz de alertas con filtros

### HU2: Modificar Información de Productos
- Formulario CRUD con validaciones
- Historial de cambios automático

### HU3: Asociar Código de Barras
- Generación automática EAN13
- Generador manual
- Visualización e impresión

### HU4: Consultar Historial
- Búsqueda por producto, tipo, fecha
- Tabla completa de movimientos

### HU5: Buscar Productos
- Búsqueda por código y nombre
- Resultados en cards

### HU6: Gestión de Usuarios
- CRUD completo
- Roles: Admin, Gerente, Operario

## Tecnologías

- Django 4.2
- PostgreSQL/SQLite
- Python-barcode
- Pillow
- xlsxwriter
- HTML5/CSS3/JavaScript

## Autor

Sistema desarrollado para Ingeniería de Software.

## Licencia

Proyecto de código abierto para fines educativos.
