from django.urls import path
from . import views  # Importa o arquivo views.py da própria pasta (.) que o urls.py se encontra.

# Crio uma list urlpatterns = [] igual a do arquivo na pasta mãe.
urlpatterns = [
    path('', views.index)  # Não executo o método com (), só referencio
    # Está em '' pois referencia ao próprio url /blog/.
]