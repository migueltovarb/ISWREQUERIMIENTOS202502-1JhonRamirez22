from django.contrib import admin
from django.urls import path, include
from inventario.views import seleccionar_rol_view

urlpatterns = [
    path('', seleccionar_rol_view, name='seleccionar_rol'),
    path('admin/', admin.site.urls),
    path('productos/', include('inventario.urls')),
]
