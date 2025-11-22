from django.test import TestCase
from .models import Producto, Alerta

class ProductoModelTest(TestCase):
    def setUp(self):
        self.producto = Producto.objects.create(codigo='PRD001', nombre='Test', precio=100, stock=10, stock_minimo=5)
    
    def test_producto_creation(self):
        self.assertEqual(self.producto.codigo, 'PRD001')
    
    def test_stock_bajo(self):
        self.producto.stock = 3
        self.producto.save()
        self.assertTrue(self.producto.stock_bajo())
    
    def test_actualizar_stock(self):
        nuevo_stock = self.producto.actualizar_stock(5, 'agregar')
        self.assertEqual(nuevo_stock, 15)

class AlertaModelTest(TestCase):
    def setUp(self):
        self.producto = Producto.objects.create(codigo='PRD002', nombre='Test2', precio=50, stock=1, stock_minimo=5)
        self.alerta = Alerta.objects.create(producto=self.producto, nivel_prioridad='Critica')
    
    def test_alerta_creation(self):
        self.assertEqual(self.alerta.nivel_prioridad, 'Critica')
    
    def test_alerta_resuelta(self):
        self.assertFalse(self.alerta.resuelta)
        self.alerta.resuelta = True
        self.alerta.save()
        self.assertTrue(self.alerta.resuelta)
