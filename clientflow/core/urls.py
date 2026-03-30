from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('clientes/', views.clientes_list, name='clientes_list'),
    path('clientes/nuevo/', views.cliente_create, name='cliente_create'),
    path('clientes/<int:id>/editar/', views.cliente_update, name='cliente_update'),
    path('clientes/<int:id>/eliminar/', views.cliente_delete, name='cliente_delete'),
]