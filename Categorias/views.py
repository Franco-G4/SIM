
# from django.shortcuts import render
from django.views.generic import ListView, DetailView
# from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


# from django.http import HttpResponse
from .forms import Cat_form

from Categorias.models import Categorias


# Create your views here.
# crud categorias

class ListCat(ListView):
    model = Categorias
    template_name = 'Categorias/listcat.html'

class ListDetalle(DetailView):
    model = Categorias

class CatAdd(SuccessMessageMixin ,CreateView):
    model = Categorias
    form = Categorias
    form_class = Cat_form
    # Mostramos este Mensaje luego de Crear la categoria
    success_message = 'Categoria Creada Correctamente !'
    template_name = "Categorias/crearcat.html"

    # Redireccionamos a la página principal luego de crear un registro o Productos
    def get_success_url(self):
        return reverse('listcat')  # Redireccionamos a la vista principal 'leer'

class CategoriasActualizar(SuccessMessageMixin, UpdateView):
    model = Categorias
    form = Categorias
    fields = "__all__"
    # Mostramos este Mensaje luego de Editar un Productos
    success_message = 'Categorias Actualizado Correctamente !'

    # Redireccionamos a la página principal luego de actualizar un registro o Productos
    def get_success_url(self):
        return reverse('listcat')  # Redireccionamos a la vista principal 'leer'

class CategoriasEliminar(SuccessMessageMixin, DeleteView):
    model = Categorias
    form = Categorias
    fields = "__all__"

    # Redireccionamos a la página principal luego de eliminar un registro o Productos
    def get_success_url(self):
        # Mostramos este Mensaje luego de Editar un Productos
        success_message = 'Categoria Eliminada Correctamente !'
        messages.success(self.request, (success_message))
        return reverse('liscat')  # Redireccionamos a la vista principal 'leer'

class form_cat(FormView):
    form_class = Cat_form
    template_name = 'Categorias/crearcat.html'
    success_url = reverse_lazy('crearcat')
    