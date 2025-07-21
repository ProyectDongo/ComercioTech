from django import forms
from .models import Cliente, Producto, Pedido
from django.forms import inlineformset_factory
from .models import Cliente, Producto, Pedido, PedidoProducto

class ClienteForm(forms.ModelForm):
      class Meta:
          model = Cliente
          fields = ['nombre', 'email', 'telefono']

class ProductoForm(forms.ModelForm):
      class Meta:
          model = Producto
          fields = ['nombre', 'descripcion', 'precio', 'stock']
          
class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'estado']  # Eliminado 'total'
        widgets = {
            'estado': forms.Select(),
        }

# Formset para manejar productos y cantidades
PedidoProductoFormSet = inlineformset_factory(
    Pedido, PedidoProducto, 
    fields=['producto', 'cantidad'],
    extra=1,
    can_delete=True,
    widgets={
        'producto': forms.Select(),
        'cantidad': forms.NumberInput(attrs={'min': 1}),
    }
)