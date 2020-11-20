from django.contrib import admin
from .models import Batch,Insumo,Producto,Tipo_cerveza
# Register your models here.

admin.site.register(Batch)
admin.site.register(Insumo)
admin.site.register(Producto)
admin.site.register(Tipo_cerveza)


admin.site.site_header = "Sistema Gestion Cervecero"
admin.site.site_title = "Portal Admin SGC"
admin.site.index_title = "Bienvenidos al portal de administración"