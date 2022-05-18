"""Proyecto01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from Proyecto01.views import (
    inicio,
    hola_mundo,
    segunda_vista,
    dia_hoy,
    mis_datos,
    calcular_anio_nacimiento,
    calcular_edad,
    probando_template
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio),
    path('hello_world/', hola_mundo),
    path('second_view/', segunda_vista),
    path('today/', dia_hoy),
    path('my_name/<nombre>/<edad>', mis_datos),
    path('birth_year/<anio>', calcular_anio_nacimiento),
    path('age/<str:fecha_nacimiento>', calcular_edad),
    path('testing_template/', probando_template),
]
