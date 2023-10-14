from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from render.views import index,prediction,cargar_imagen_audio

urlpatterns = [
    path('', index, name='index'),
    path('prediction/<str:idSat>', prediction, name='prediction'),
    path('form/', cargar_imagen_audio, name='form'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)