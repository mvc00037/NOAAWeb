from django.urls import path

from render.views import index,prediction

urlpatterns = [
    path('', index, name='index'),
    path('prediction/<str:idSat>', prediction, name='prediction'),
]