

from django.urls import  path
# importar las vistas
from .views import *
# fin vistas
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # modificar esto
    # urls de productos
    path('Productos/', lista.as_view(template_name = 'Productos/lista.html'), name = 'lista'),
    path('Productos/detalle/<int:pk>', ProductosDetalle.as_view(template_name = "Productos/detalles.html"), name='detalles'), 
    path('Productos/crear', ProductosCrear.as_view(template_name = "Productos/crear.html"), name='crear'),
    path('Productos/editar/<int:pk>', ProductosActualizar.as_view(template_name = "Productos/editar.html"), name='editar'),    
    path('Productos/eliminar/<int:pk>', ProductosEliminar.as_view(), name='eliminar'),   

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 




    

