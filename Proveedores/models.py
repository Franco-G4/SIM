from django.db import models

# Create your models here.
class Proveedores(models.Model):
    idproveedor = models.IntegerField(primary_key=True)
    razon_social = models.CharField(max_length=100, blank=True, null=True)
    nombre_apellido = models.CharField(max_length=70)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    direccion2 = models.CharField(max_length=70, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    celular = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    fecha_alta = models.DateField(blank=True, null=True)
    tipodoc = models.CharField(max_length=50, blank=True, null=True)
    dni = models.CharField(max_length=50, blank=True, null=True)
    localidad = models.CharField(max_length=50, blank=True, null=True)
    saldomax = models.FloatField(blank=True, null=True)
    nombre_fantasia = models.CharField(max_length=80, blank=True, null=True)
    tiporesponsable = models.CharField(max_length=50, blank=True, null=True)
    provincia = models.CharField(max_length=50, blank=True, null=True)
    estado = models.SmallIntegerField(blank=True, null=True)

    def __str__(self):
        return self.razon_social