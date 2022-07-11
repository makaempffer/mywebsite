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
from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.conf.urls.static import static
from django.conf import settings

from django.contrib.auth import authenticate, login, logout

from productos.models import Producto, Categoria, Mascota

import ulid

from rest_framework import routers
from ofertas.views import OfertaViewSet


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
                    unique_id=ulid.new().str,
                    nombre = producto.nombre,
                    categoria = producto.categoria.nombre,
                    precio = producto.precio,
                    descripcion = producto.descripcion,
                    stock = producto.stock,
                    imagen = producto.imagen.url
                )
                dic_productos[producto.nombre] = producto_data
            cat_uid = f'{mascota.nombre.replace(" ", "_")}__{categoria.nombre.replace(" ", "_")}'
            dic_categorias[categoria.nombre] = dict(descripcion = categoria.descripcion, imagen = categoria.imagen.url, productos=dic_productos, unique_id=cat_uid)
        tienda[mascota.nombre] = dict(descripcion = mascota.descripcion, categorias=dic_categorias)

    context = dict(tienda = tienda)
    #print(tienda)

    return render(request, '../templates/index.html', context)

def login_view(request):

    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        print('LOGGEADO')
        return HttpResponse('Ingreso correcto', status=200)
    else:
        print('HUBO UN ERROR')
        return HttpResponse('Ingreso fallido', status=400)

def logout_view(request):
    logout(request)
    
    return HttpResponse('Ingreso correcto', status=200)

router = routers.DefaultRouter()
router.register(r'ofertas', OfertaViewSet)

urlpatterns = [
    path('', index),
    path('ingresar/', login_view),
    path('salir/', logout_view),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
