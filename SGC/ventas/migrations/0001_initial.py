# Generated by Django 2.2.7 on 2020-11-25 00:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bodega', '0002_auto_20201124_2132'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.TextField(max_length=100)),
                ('telefono', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(choices=[('Entregado y pagado', 'Entregado y pagado'), ('Entregado y no pagado', 'Entregado y no pagado'), ('No entregado y pagado', 'No entregado y pagado'), ('No entregado y no pagado', 'No entregado y no pagado')], max_length=50)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cliente', to='ventas.Cliente', verbose_name='cliente')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Detalle_Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Producto', to='bodega.Producto', verbose_name='producto')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='venta', to='ventas.Venta', verbose_name='venta')),
            ],
        ),
    ]
