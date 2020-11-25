from django.db import models
from bodega.models import Tipo_cerveza, Batch,Insumo,Producto
from django.conf import settings 

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.TextField(max_length=100)
    telefono = models.CharField(max_length=12)
    def __str__(self):
        return self.nombre


class Venta(models.Model):

    ENT_PAG = "Entregado y pagado"
    ENT_NOPAG = "Entregado y no pagado"
    NOENT_PAG = "No entregado y pagado"
    NOENT_NOPAG = "No entregado y no pagado"

    ESTADO = [
       (ENT_PAG, "Entregado y pagado"),
       (ENT_NOPAG, "Entregado y no pagado"),
       (NOENT_PAG, "No entregado y pagado"),
       (NOENT_NOPAG, "No entregado y no pagado"), 
    ]
    cliente = models.ForeignKey('Cliente', related_name="cliente", on_delete=models.PROTECT, verbose_name="cliente")
    usuario =  models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank=True, null=True)
    estado = models.CharField(max_length=50, choices=ESTADO)

class Detalle_Venta(models.Model):
    venta = models.ForeignKey('Venta', related_name="venta", on_delete=models.PROTECT, verbose_name="venta")
    producto = models.ForeignKey('bodega.Producto', related_name="Producto", on_delete=models.PROTECT, verbose_name="producto")
    cantidad = models.IntegerField()
    def __str__(self):
        return str(self.venta)