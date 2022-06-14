"""mywebsite URL Configuration

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
from django.urls import path, include
from django.http import JsonResponse
from django.shortcuts import render

from django.conf.urls.static import static
from django.conf import settings

from productos.models import Producto, Categoria, Mascota


def index(request):

    mascotas_all = Mascota.objects.all()
    tienda = {}

    for mascota in mascotas_all:
        categorias_mascota = Categoria.objects.filter(mascota=mascota)
        dic_categorias = dict()
        for categoria in categorias_mascota:
            productos_categoria = Producto.objects.filter(categoria=categoria)
            dic_productos = dict()
            for producto in productos_categoria:
                producto_data = dict(
                    nombre = producto.nombre,
                    categoria = producto.categoria.nombre,
                    precio = producto.precio,
                    descripcion = producto.descripcion,
                    imagen = producto.imagen.url
                )
                dic_productos[producto.nombre] = producto_data
            dic_categorias[categoria.nombre] = dict(descripcion = categoria.descripcion, productos=dic_productos)
        tienda[mascota.nombre] = dict(descripcion = mascota.descripcion, categorias=dic_categorias)

    context = dict(tienda = tienda)
    print(tienda)

    return render(request, '../templates/index.html', context)

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls), 
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
