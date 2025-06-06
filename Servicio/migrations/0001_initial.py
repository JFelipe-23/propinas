# Generated by Django 5.2.1 on 2025-05-28 21:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Cliente', '0001_initial'),
        ('Trabajador', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('activa', models.BooleanField()),
                ('calificacion', models.IntegerField()),
                ('nota', models.TextField(blank=True, null=True)),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cliente.cliente')),
                ('id_trabajador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Trabajador.trabajador')),
            ],
        ),
        migrations.CreateModel(
            name='Propina',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Cantidad', models.DecimalField(decimal_places=2, max_digits=10)),
                ('servicio', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Servicio.servicio')),
            ],
        ),
    ]
