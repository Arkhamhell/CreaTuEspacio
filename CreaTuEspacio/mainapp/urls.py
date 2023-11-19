from django.urls import path
from . import views

urlpatterns = [
    
    path('' , views.index , name="index"),
    path('inicio/' ,views.index , name="inicio"),
    path('inicio_usuarios/' ,views.inicio_usuarios , name="inicio_usuarios"),
    path('registro/' , views.register_page , name="register"),
    path('login/' , views.login_page, name="login"),
    path('logout/' , views.logout_user , name="logout"),
    path('usuarios/', views.insertar_usuarios_centro, name="ingresar_usuarios"),
    path('lista_usuarios/' , views.listar_usuarios_centro , name="lista_usuarios"),
    path('eliminar_usuarios/<int:id>' , views.eliminar_usuario , name="eliminar_usuarios"),
    path('actualizar_usuarios/<int:id>' , views.actualizar_usuario, name="actualizar_usuarios")

]