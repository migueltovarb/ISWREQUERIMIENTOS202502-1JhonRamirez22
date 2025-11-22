from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q, F
from django.utils import timezone
from .models import Producto, Rol, Alerta, Movimiento, Proveedor
from .forms import ProductoForm, ActualizarStockForm, RolForm, HistorialSearchForm, BuscarProductoForm

def seleccionar_rol_view(request):
    return render(request, 'inventario/seleccionar_rol.html')

def login_view(request):
    rol = request.GET.get('rol', 'operario')
    rol_nombre = request.GET.get('rol_nombre', 'Usuario')
    
    # Operario NO requiere login
    if rol == 'operario':
        return redirect(f"/productos/listado/?rol=operario")
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect(f"/productos/listado/?rol={rol}")
        else:
            return render(request, 'inventario/login.html', {
                'error': 'Usuario o contraseña incorrectos',
                'rol': rol,
                'rol_nombre': rol_nombre
            })
    
    return render(request, 'inventario/login.html', {
        'rol': rol,
        'rol_nombre': rol_nombre
    })

def logout_view(request):
    logout(request)
    return redirect('inventario:seleccionar_rol')

class ProductoListView(ListView):
    model = Producto
    template_name = 'inventario/listado_productos.html'
    context_object_name = 'productos'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(Q(codigo__icontains=search) | Q(marca__icontains=search) | Q(nombre__icontains=search))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        rol = self.request.GET.get('rol', 'operario')
        context['rol'] = rol
        
        # Solo admin/gerente ven alertas
        if rol in ['administrador', 'gerente']:
            context['productos_bajo_stock'] = Producto.objects.filter(stock__lt=F('stock_minimo'))
            context['alertas_activas'] = Alerta.objects.filter(estado='activa').count()
        
        return context

class ProductoCreateView(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'inventario/producto_form.html'
    success_url = reverse_lazy('inventario:listado')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        # Crear movimiento de entrada
        Movimiento.objects.create(
            producto=self.object,
            tipo='entrada',
            cantidad=self.object.stock,
            usuario=self.request.user.username or 'Sistema',
            stock_anterior=0,
            stock_posterior=self.object.stock,
            descripcion='Creación de producto'
        )
        messages.success(self.request, 'Producto creado exitosamente')
        return response
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rol'] = self.request.GET.get('rol', 'administrador')
        return context

class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'inventario/producto_form.html'
    success_url = reverse_lazy('inventario:listado')
    
    def form_valid(self, form):
        messages.success(self.request, 'Producto actualizado exitosamente')
        return super().form_valid(form)

class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'inventario/producto_confirmar_eliminar.html'
    success_url = reverse_lazy('inventario:listado')
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Producto eliminado exitosamente')
        return super().delete(request, *args, **kwargs)

def actualizar_stock_view(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    
    if request.method == 'POST':
        form = ActualizarStockForm(request.POST)
        if form.is_valid():
            cantidad = form.cleaned_data['cantidad']
            operacion = form.cleaned_data['operacion']
            stock_anterior = producto.stock
            
            if operacion == 'agregar':
                producto.stock += cantidad
                tipo_mov = 'entrada'
            else:
                producto.stock = max(0, producto.stock - cantidad)
                tipo_mov = 'salida'
            
            producto.save()
            
            # Registrar movimiento
            Movimiento.objects.create(
                producto=producto,
                tipo=tipo_mov,
                cantidad=cantidad,
                usuario=request.user.username or 'Sistema',
                stock_anterior=stock_anterior,
                stock_posterior=producto.stock,
                descripcion=f'{tipo_mov.title()} de {cantidad} unidades'
            )
            
            # Crear alerta si es necesario
            if producto.stock < producto.stock_minimo and producto.stock > 0:
                Alerta.objects.create(
                    producto=producto,
                    tipo='stock_bajo',
                    estado='activa',
                    descripcion=f'Stock bajo: {producto.stock} unidades'
                )
            
            messages.success(request, f'Stock actualizado a {producto.stock} unidades')
            return redirect('inventario:listado')
    else:
        form = ActualizarStockForm()
    
    return render(request, 'inventario/actualizar_stock.html', {'form': form, 'producto': producto})

def producto_detalle_view(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'inventario/producto_detalle.html', {'producto': producto})

# ============== HU013: ALERTAS ==============
class AlertasListView(ListView):
    model = Alerta
    template_name = 'inventario/alertas.html'
    context_object_name = 'alertas'
    paginate_by = 20
    
    def get_queryset(self):
        return Alerta.objects.filter(estado='activa').order_by('-fecha_creacion')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_alertas'] = Alerta.objects.filter(estado='activa').count()
        context['rol'] = self.request.GET.get('rol', 'administrador')
        return context

# ============== HU015: HISTORIAL ==============
class HistorialListView(ListView):
    model = Movimiento
    template_name = 'inventario/historial.html'
    context_object_name = 'movimientos'
    paginate_by = 50
    
    def get_queryset(self):
        queryset = Movimiento.objects.all()
        
        tipo = self.request.GET.get('tipo')
        if tipo:
            queryset = queryset.filter(tipo=tipo)
        
        producto = self.request.GET.get('producto')
        if producto:
            queryset = queryset.filter(producto__codigo__icontains=producto)
        
        return queryset.order_by('-fecha')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rol'] = self.request.GET.get('rol', 'administrador')
        return context

# ============== HU016: PROVEEDORES ==============
class ProveedorListView(ListView):
    model = Proveedor
    template_name = 'inventario/proveedor_list.html'
    context_object_name = 'proveedores'

class ProveedorCreateView(CreateView):
    model = Proveedor
    template_name = 'inventario/proveedor_form.html'
    fields = ['nombre', 'contacto', 'email', 'telefono', 'direccion', 'ciudad', 'pais']
    success_url = reverse_lazy('inventario:proveedor_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Proveedor creado exitosamente')
        return super().form_valid(form)

class ProveedorUpdateView(UpdateView):
    model = Proveedor
    template_name = 'inventario/proveedor_form.html'
    fields = ['nombre', 'contacto', 'email', 'telefono', 'direccion', 'ciudad', 'pais', 'activo']
    success_url = reverse_lazy('inventario:proveedor_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Proveedor actualizado exitosamente')
        return super().form_valid(form)

class ProveedorDeleteView(DeleteView):
    model = Proveedor
    template_name = 'inventario/proveedor_confirm_delete.html'
    success_url = reverse_lazy('inventario:proveedor_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Proveedor eliminado exitosamente')
        return super().delete(request, *args, **kwargs)

# ============== Vistas para Roles ==============
class RolListView(ListView):
    model = Rol
    template_name = 'inventario/rol_list.html'
    context_object_name = 'roles'

class RolCreateView(CreateView):
    model = Rol
    form_class = RolForm
    template_name = 'inventario/rol_form.html'
    success_url = reverse_lazy('inventario:rol_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Usuario creado exitosamente')
        return super().form_valid(form)

class RolUpdateView(UpdateView):
    model = Rol
    form_class = RolForm
    template_name = 'inventario/rol_form.html'
    success_url = reverse_lazy('inventario:rol_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Usuario actualizado exitosamente')
        return super().form_valid(form)

class RolDeleteView(DeleteView):
    model = Rol
    template_name = 'inventario/rol_confirm_delete.html'
    success_url = reverse_lazy('inventario:rol_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Usuario eliminado exitosamente')
        return super().delete(request, *args, **kwargs)
