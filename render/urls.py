from django.urls import path

from render.views import index,prediction,cargar_imagen_audio

urlpatterns = [
    path('', index, name='index'),
    path('prediction/<str:idSat>', prediction, name='prediction'),
    path('form/', cargar_imagen_audio, name='form'),
]