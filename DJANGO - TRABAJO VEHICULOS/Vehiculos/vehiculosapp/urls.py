from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_vehiculos, name='listar_vehiculos'),
    path('create/', views.crear_vehiculo, name='crear_vehiculo'),
    path('edit/<int:id>/', views.editar_vehiculo, name='editar_vehiculo'),
    path('delete/<int:id>/', views.eliminar_vehiculo, name='eliminar_vehiculo'),
]
