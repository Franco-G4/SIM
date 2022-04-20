from django.urls import  path
# importar las vistas
from Categorias.views import *
# fin vistas
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # urls de categorias 
    path('Categorias/', ListCat.as_view(template_name = 'Categorias/listcat.html'), name = 'listcat'),
    path('Categorias/detalle/<int:pk>', ListDetalle.as_view(template_name = "Categorias/detallescat.html"), name='detcategorias'), 
    path('Categorias/crear', CatAdd.as_view(template_name = "Categorias/crearcat.html"), name='crearcat'),
    path('Categorias/editar/<int:pk>', CategoriasActualizar.as_view(template_name = "Categorias/editarcat.html"), name='editar'),    
    path('Categorias/eliminar/<int:pk>', CategoriasEliminar.as_view(), name='eliminarcat'),    
    # path('Categorias/formcat', form_cat.as_view(), name='formcat'),    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
