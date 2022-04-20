

from django.urls import  path
# importar las vistas
from HomePage.views import home

# fin vistas
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home.as_view(template_name = 'HomePage/body.html'), name = 'home'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 