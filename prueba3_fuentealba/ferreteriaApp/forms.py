from django import forms
from .models import Producto
from datetime import datetime

class ProductoForm(forms.ModelForm):
    fecha_ingreso = forms.CharField(
        max_length=10,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'dd/mm/yyyy'
        }),
        label='Fecha de Ingreso'
    )
    
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'stock', 'precio_unitario', 'fecha_ingreso', 'categoria']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'precio_unitario': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {
            'nombre': 'Nombre del Producto',
            'descripcion': 'Descripción',
            'stock': 'Stock',
            'precio_unitario': 'Precio Unitario ($)',
            'categoria': 'Categoría',
        }
    
    def clean_fecha_ingreso(self):
        fecha_str = self.cleaned_data.get('fecha_ingreso')
        
        if not fecha_str:
            raise forms.ValidationError('La fecha es obligatoria.')
        
        try:
            fecha = datetime.strptime(fecha_str, '%d/%m/%Y').date()
            return fecha
        except ValueError:
            raise forms.ValidationError('Formato de fecha inválido. Use dd/mm/yyyy (Ejemplo: 31/12/2024)')
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance