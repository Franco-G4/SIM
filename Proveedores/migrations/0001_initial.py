# Generated by Django 3.1.5 on 2022-03-01 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedores',
            fields=[
                ('idproveedor', models.IntegerField(primary_key=True, serialize=False)),
                ('razon_social', models.CharField(blank=True, max_length=100, null=True)),
                ('nombre_apellido', models.CharField(max_length=70)),
                ('direccion', models.CharField(blank=True, max_length=50, null=True)),
                ('direccion2', models.CharField(blank=True, max_length=70, null=True)),
                ('telefono', models.CharField(blank=True, max_length=20, null=True)),
                ('celular', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_alta', models.DateField(blank=True, null=True)),
                ('tipodoc', models.CharField(blank=True, max_length=50, null=True)),
                ('dni', models.CharField(blank=True, max_length=50, null=True)),
                ('localidad', models.CharField(blank=True, max_length=50, null=True)),
                ('saldomax', models.FloatField(blank=True, null=True)),
                ('nombre_fantasia', models.CharField(blank=True, max_length=80, null=True)),
                ('tiporesponsable', models.CharField(blank=True, max_length=50, null=True)),
                ('provincia', models.CharField(blank=True, max_length=50, null=True)),
                ('estado', models.SmallIntegerField(blank=True, null=True)),
            ],
        ),
    ]
