from django.contrib import admin
from .models import Cliente,Detalle_Venta, Venta

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Detalle_Venta)
admin.site.register(Venta)