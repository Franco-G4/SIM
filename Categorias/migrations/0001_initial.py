# Generated by Django 3.1.5 on 2022-04-15 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('idcategoria', models.IntegerField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(blank=True, max_length=70, null=True)),
                ('estado', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
