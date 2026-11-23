from django.urls import path
from app_cad_users import views

urlpatterns = [
    # rota, view responsavel, nome de ref
    #usuarios.com
    path('',views.home,name='home'),
    #usuarios.com/usuarios
    path('usuarios/',views.usuarios,name='listagem_usuarios'),
]
