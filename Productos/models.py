
from django.forms import *
from django.db import models
from django.db.models.deletion import CASCADE
from Proveedores.models import * 
from Categorias.models import *
# para importar modelos de otra app usar el nombre de la app seguido del nombre del modelo.models
# ej. : idproveedor = models.ForeignKey('nombre_app.nombre_modelo', on_delete = models.CASCADE)
# --------modelos - - - -
# ----- de productos
#  categorias 
# ----- y marca. ------
class Productos(models.Model):
    codigo = models.CharField(primary_key=True, max_length=4)
    idcategoria = models.ForeignKey('Categorias.Categorias', on_delete = models.CASCADE)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    costo_unitario = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    utilidad = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    precioventa = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    descuento = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    importeiva = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    fechaultima = models.DateField(blank=True, null=True )
    unidad = models.CharField(max_length=50, blank=True, null=True)
    stock = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    stock_minimo = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    control_stock = models.BooleanField(blank=True, null=True)
    stock_detallado = models.BooleanField(blank=True, null=True)
    imagen = models.BinaryField(blank=True, null=True)
    idproveedor = models.ForeignKey('Proveedores.Proveedores', on_delete = models.CASCADE)
    idmarca = models.ForeignKey('Marca', on_delete=models.CASCADE)
    estado = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return self.descripcion
    
class Marca(models.Model):
    idmarca = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.nombre

    
