from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('clientes/', ClienteListView.as_view(), name='cliente_list'),
    path('clientes/nuevo/', ClienteCreateView.as_view(), name='cliente_create'),
    path('clientes/<int:pk>/editar/', ClienteUpdateView.as_view(), name='cliente_update'),
    path('clientes/<int:pk>/eliminar/', ClienteDeleteView.as_view(), name='cliente_delete'),
    path('productos/', ProductoListView.as_view(), name='producto_list'),
    path('productos/nuevo/', ProductoCreateView.as_view(), name='producto_create'),
    path('productos/<int:pk>/editar/', ProductoUpdateView.as_view(), name='producto_update'),
    path('productos/<int:pk>/eliminar/', ProductoDeleteView.as_view(), name='producto_delete'),
    path('pedidos/', PedidoListView.as_view(), name='pedido_list'),
    path('pedidos/nuevo/', PedidoCreateView.as_view(), name='pedido_create'),
    path('pedidos/<int:pk>/editar/', PedidoUpdateView.as_view(), name='pedido_update'),
    path('pedidos/<int:pk>/eliminar/', PedidoDeleteView.as_view(), name='pedido_delete'),
]