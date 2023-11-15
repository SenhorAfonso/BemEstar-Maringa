
from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat, name='chat'),
    path('ativo', views.chatativo, name='chatativo'),
    path('encontrar-medicos', views.encontrarmedicos, name='chatativo'),
]

