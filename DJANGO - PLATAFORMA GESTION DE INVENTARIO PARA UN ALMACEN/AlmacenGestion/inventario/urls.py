from django.urls import path
from .views import (
    seleccionar_rol_view,
    login_view,
    logout_view,
    ProductoListView,
    ProductoCreateView,
    ProductoUpdateView,
    ProductoDeleteView,
    actualizar_stock_view,
    producto_detalle_view,
    RolListView,
    RolCreateView,
    RolUpdateView,
    RolDeleteView,
    AlertasListView,
    HistorialListView,
    ProveedorListView,
    ProveedorCreateView,
    ProveedorUpdateView,
    ProveedorDeleteView,
)

app_name = 'inventario'

urlpatterns = [
    # Seleccionar rol y login
    path('', seleccionar_rol_view, name='seleccionar_rol'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    
    # Productos
    path('listado/', ProductoListView.as_view(), name='listado'),
    path('crear/', ProductoCreateView.as_view(), name='crear'),
    path('<int:pk>/editar/', ProductoUpdateView.as_view(), name='editar'),
    path('<int:pk>/eliminar/', ProductoDeleteView.as_view(), name='eliminar'),
    path('<int:pk>/actualizar-stock/', actualizar_stock_view, name='actualizar_stock'),
    path('<int:pk>/detalle/', producto_detalle_view, name='detalle'),
    
    # Alertas (HU013)
    path('alertas/', AlertasListView.as_view(), name='alertas'),
    
    # Historial de Movimientos (HU015)
    path('historial/', HistorialListView.as_view(), name='historial'),
    
    # Proveedores (HU016)
    path('proveedores/', ProveedorListView.as_view(), name='proveedor_list'),
    path('proveedores/nuevo/', ProveedorCreateView.as_view(), name='proveedor_crear'),
    path('proveedores/<int:pk>/editar/', ProveedorUpdateView.as_view(), name='proveedor_editar'),
    path('proveedores/<int:pk>/eliminar/', ProveedorDeleteView.as_view(), name='proveedor_eliminar'),
    
    # Roles / Usuarios
    path('roles/', RolListView.as_view(), name='rol_list'),
    path('roles/nuevo/', RolCreateView.as_view(), name='rol_crear'),
    path('roles/<int:pk>/editar/', RolUpdateView.as_view(), name='rol_editar'),
    path('roles/<int:pk>/eliminar/', RolDeleteView.as_view(), name='rol_eliminar'),
]
