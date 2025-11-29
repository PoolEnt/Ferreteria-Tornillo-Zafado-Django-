from django.contrib import admin
from .models import Producto
# Register your models here.

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'stock', 'precio_unitario', 'categoria', 'fecha_ingreso']
    list_filter = ['categoria', 'fecha_ingreso']
    search_fields = ['nombre', 'descripcion']