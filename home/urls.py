
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('realizar_cadastro/', views.realizar_cadastro, name='realizar_cadastro', ),
]

