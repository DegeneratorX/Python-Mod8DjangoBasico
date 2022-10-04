from django.urls import path
from . import views  # Importa a própria pasta 'blog'.

urlpatterns = [
    path('', views.index)  # Não executo o método com (), só referencio
]