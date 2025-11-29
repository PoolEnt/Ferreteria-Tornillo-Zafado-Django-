"""
URL configuration for prueba3_fuentealba project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from ferreteriaApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('', views.login_view, name='login'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('producto/', views.listar_productos, name='listar_producto'),
    path('buscar/', views.buscar_producto, name='buscar_producto'),
    path('agregar/', views.agregar_producto, name='agregar_producto'),
    path('modificar/<int:id>/', views.modificar_producto, name='modificar_producto'),
    path('eliminar/<int:id>/', views.eliminar_producto, name='eliminar_producto'),
]
