from django.db import models

# Create your models here.
class Categorias(models.Model):
    idcategoria = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=70, blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.descripcion
