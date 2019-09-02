from django.urls import path
from .views import listar, buscar, remover, cadastrar, editar

urlpatterns = [
    path('', listar, name='listar'),
    path('buscar/<int:id>', buscar, name='buscar'),
    path('remover/<int:id>', remover, name='remover'),
    path('cadastrar/', cadastrar, name='cadastrar'),
    path('editar/<int:id>', editar, name='editar')
]