from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Cliente, Producto, Pedido, PedidoProducto
from .forms import ClienteForm, ProductoForm, PedidoForm
from django.views.generic import TemplateView
from .forms import ClienteForm, ProductoForm, PedidoForm, PedidoProductoFormSet
from django.forms import inlineformset_factory
class HomeView(TemplateView):
    template_name = 'core/home.html'

#vistas 


#listas
class ClienteListView(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = 'core/cliente_list.html'


class ProductoListView(LoginRequiredMixin, ListView):
    model = Producto
    template_name = 'core/producto_list.html'


class PedidoListView(LoginRequiredMixin, ListView):
    model = Pedido
    template_name = 'core/pedido_list.html'


#delete

class ClienteDeleteView(LoginRequiredMixin, DeleteView):
    model = Cliente
    template_name = 'confirmacion.html'
    success_url = reverse_lazy('cliente_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Cliente'
        context['return_url'] = 'cliente_list'
        return context


class ProductoDeleteView(LoginRequiredMixin, DeleteView):
    model = Producto
    template_name = 'confirmacion.html'
    success_url = reverse_lazy('producto_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Producto'
        context['return_url'] = 'producto_list'
        return context
    


class PedidoDeleteView(LoginRequiredMixin, DeleteView):
    model = Pedido
    template_name = 'confirmacion.html'
    success_url = reverse_lazy('pedido_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Pedido'
        context['return_url'] = 'pedido_list'
        return context


#update
class ClienteUpdateView(LoginRequiredMixin, UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'core/cliente_form.html'
    success_url = reverse_lazy('cliente_list')


class ProductoUpdateView(LoginRequiredMixin, UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'core/producto_form.html'
    success_url = reverse_lazy('producto_list')




class PedidoUpdateView(LoginRequiredMixin, UpdateView):
    model = Pedido
    form_class = PedidoForm
    template_name = 'core/pedido_form.html'
    success_url = reverse_lazy('pedido_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Usa siempre el mismo prefix que en CreateView ("form")
        if self.request.method == 'POST':
            context['formset'] = PedidoProductoFormSet(
                self.request.POST,
                instance=self.object,
                prefix='form'
            )
        else:
            context['formset'] = PedidoProductoFormSet(
                instance=self.object,
                prefix='form'
            )
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            # guarda el Pedido
            self.object = form.save()
            # asocia y guarda los productos
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)



#forms

class ClienteCreateView(LoginRequiredMixin, CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'core/cliente_form.html'
    success_url = reverse_lazy('cliente_list')


class ProductoCreateView(LoginRequiredMixin, CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'core/producto_form.html'
    success_url = reverse_lazy('producto_list')

class PedidoCreateView(CreateView):
    model = Pedido
    form_class = PedidoForm
    template_name = 'core/pedido_form.html'
    success_url = reverse_lazy('pedido_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # si hay POST, pasamos POST; si no, solo la instancia (None en Create)
        if self.request.method == 'POST':
            context['formset'] = PedidoProductoFormSet(
                self.request.POST,
                instance=self.object,
                prefix='form'
            )
        else:
            context['formset'] = PedidoProductoFormSet(
                instance=self.object,
                prefix='form'
            )
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            # primero guardamos el pedido
            self.object = form.save()
            # luego los productos
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)









