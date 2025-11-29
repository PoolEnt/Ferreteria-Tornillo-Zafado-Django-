from django.db import models

# Create your models here.

class Producto(models.Model):
    CATEGORIAS = [
        ('herramientas', 'Herramientas'),
        ('pintura', 'Pintura'),
        ('pisos', 'Pisos'),
        ('jardineria', 'Jardineria'),
    ]
    
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    stock = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_ingreso = models.DateField()
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    
    def __str__(self):
        return self.nombre
    
    #class Meta:
       # db_tale = 'productos'