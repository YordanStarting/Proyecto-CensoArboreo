"""censoarboleo2022 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path
import django.views.static 
from django.conf.urls import include

import os
from usuarios.views import  *
from formulario.views import crear_formulario_view, editar_formulario, listar_formularios, listar_formularios_censista, ver_formulario

urlpatterns = [
    path('', login_view, name='login'),
    path('logout', custom_logout, name='logout'),
    path('registro_usuario', registro_usuario_view, name='registro_usuario'),
    path('cambiar_contrasena', cambiar_contrasena, name='cambiar_contrasena'),
    path('formulario', crear_formulario_view, name='formulario'),
    path('listar_usuarios_administrador', listar_usuarios_administrador, name='listar_usuarios_administrador'),
    path('listar_censistas_supervisor', listar_censistas_supervisor, name='listar_censistas_supervisor'),
    path('listar_formularios', listar_formularios, name='listar_formularios'),
     path('listar_formularios_censista', listar_formularios_censista, name='listar_formularios_censista'),
    path('editar/<username>/', editar_usuario, name='editar_usuario'),
    path('editar_formulario/<id_arbol>/', editar_formulario, name='editar_formulario'),
    path('ver_formulario/<id_arbol>/', ver_formulario, name='ver_formulario'),

	re_path(r'^censoarboleo2022/media/(.*)$', django.views.static.serve, {'document_root' : os.path.join(os.path.dirname(__file__), 'media')}),

]
