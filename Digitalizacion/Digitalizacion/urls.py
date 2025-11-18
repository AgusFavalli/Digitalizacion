from django.contrib import admin
from django.urls import path, include
from django.conf  import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),

    # URLS de las apps
    path('api/usuarios/', include('apps.usuarios.urls')),
    path('api/areas/', include('apps.areas.urls')),
    #path('api/expedientes/', include('apps.expedientes.urls')),
    #path('api/movimientos/', include('apps.movimientos.urls')),

    # Documentacion de la API
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'), # Genera un archivo JSON con el esquema de la API
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'), # Interfaz visual e interactiva para probar la API
]

# Servir archivos media en desarrollo (solo en produccion)
if  settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
