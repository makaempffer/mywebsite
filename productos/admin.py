from django.contrib import admin

from .models import Producto, Categoria, Mascota

for m in (Producto, Categoria, Mascota):
    admin.site.register(m)
