
# from django.shortcuts import render
from django.views.generic import ListView, DetailView
# from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from Categorias.models import Categorias
from Productos.models import Productos

# from django.http import HttpResponse

from Productos.forms import Prod_forms
from Categorias.forms import Cat_form


# Create your views here.
class lista(ListView):
    model = Productos
    template_name = 'Productos/lista.html'


class ProductosDetalle(DetailView):
    model = Productos


class ProductosCrear(SuccessMessageMixin, CreateView):
    model = Productos
    form = Productos
    form_class = Prod_forms
    # Mostramos este Mensaje luego de Crear un Productos
    success_message = 'Producto Creado Correctamente !'
    template_name = "Productos/crear.html"

    # Redireccionamos a la página principal luego de crear un registro o Productos
    def get_success_url(self):
        return reverse('lista')  # Redireccionamos a la vista principal 'leer'


class ProductosActualizar(SuccessMessageMixin, UpdateView):
    model = Productos
    form = Productos
    fields = "__all__"
    # Mostramos este Mensaje luego de Editar un Productos
    success_message = 'Productos Actualizado Correctamente !'

    # Redireccionamos a la página principal luego de actualizar un registro o Productos
    def get_success_url(self):
        return reverse('lista')  # Redireccionamos a la vista principal 'leer'


class ProductosEliminar(SuccessMessageMixin, DeleteView):
    model = Productos
    form = Productos
    fields = "__all__"

    # Redireccionamos a la página principal luego de eliminar un registro o Productos
    def get_success_url(self):
        # Mostramos este Mensaje luego de Editar un Productos
        success_message = 'Productos Eliminado Correctamente !'
        messages.success(self.request, (success_message))
        return reverse('lista')  # Redireccionamos a la vista principal 'leer'

# class ModalAddCat(SuccessMessageMixin ,CreateView):
#     model = Categorias
#     form = Categorias
#     form_class = Cat_form
#     # Mostramos este Mensaje luego de Crear la categoria
#     success_message = 'Categoria Creada Correctamente !'
#     template_name = "Categorias/crearcat.html"

#     # Redireccionamos a la página principal luego de crear un registro o Productos
#     def get_success_url(self):
#         return reverse('listcat')  # Redireccionamos a la vista principal 'leer'
