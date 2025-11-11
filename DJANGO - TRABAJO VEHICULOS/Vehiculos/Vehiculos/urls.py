from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('vehiculosapp.urls')),  # Ruta raíz apunta a tu app
]
