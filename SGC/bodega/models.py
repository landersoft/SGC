from django.db import models

# Modelo Tipo de Cerveza
class Tipo_cerveza(models.Model):
    tipo_nombre = models.CharField(max_length=50)
    caracteristicas = models.CharField(max_length=100)
    class Meta:
        verbose_name = "Tipo de Cerveza"
        verbose_name_plural = "Tipos de Cerveza"

    def __str__(self):
        return (self.tipo_nombre)

#Modelo Batch

class Batch(models.Model):
    fecha_cocimiento = models.DateField(blank=False, null=False)
    fecha_maduracion = models.DateField(blank=True)
    fecha_embotellado = models.DateField(blank=True)
    cantidad_litros = models.IntegerField(blank=True)
    tipo = models.ForeignKey('Tipo_cerveza', related_name="tipo_nombre", on_delete=models.PROTECT, verbose_name="Tipo de Cerveza")

    class Meta:
        verbose_name = "Batch"
        verbose_name_plural = "Batch's"
    def __str__(self):
        return str(self.id)

#Modelo Insumo
class Insumo(models.Model):
    nombre_insumo = models.CharField(max_length=50, blank=False, null=False)
    stock_insumo = models.IntegerField(default=0)
    class Meta: 
        verbose_name = "Insumo"
        verbose_name_plural = "Insumos"
    def __str__(self):
        return self.nombre_insumo

#Modelo Producto

class Producto(models.Model):
       
    BOTELLITA = 'Botella 330cc'
    BOTELLA = 'Botella 1000cc'
    GROULER = 'Grouler'
    BARRIL = 'Barril 30lts'

    FORMATO = [
        (BOTELLITA,'Botella 330cc'),
        (BOTELLA,'Botella 1000cc'),
        (GROULER,'Grouler'),
        (BARRIL ,'Barril 30lts'),
    ]
    nombre_producto = models.CharField(max_length=50)
    formato_producto = models.CharField(max_length=50, choices=FORMATO)
    stock_producto = models.IntegerField()
    class Meta: 
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
    def __str__(self):
        return self.nombre_producto