from django.db import models

from django.conf import settings

class Mascota(models.Model):
    nombre = models.TextField(max_length=64)
    descripcion = models.TextField(max_length=512, default='')

    def __str__(self) -> str:
        return f'{self.nombre}'

class Categoria(models.Model):
    nombre = models.TextField(max_length=64)
    descripcion = models.TextField(max_length=512, default='')
    mascota = models.ForeignKey(Mascota, related_name='mascota', on_delete=models.CASCADE, null=True)
    imagen = models.ImageField(upload_to=settings.MEDIA_ROOT / 'categorias', null=True)

    def __str__(self) -> str:
        return f'{self.nombre} ({self.mascota.nombre})'

class Producto(models.Model):

    nombre = models.TextField(max_length=64, blank=False)
    categoria = models.ForeignKey(Categoria, related_name='categoria', on_delete=models.CASCADE, null=True)
    descripcion = models.TextField(max_length=512, blank=False)
    precio = models.PositiveIntegerField(blank=False)
    stock = models.IntegerField(blank=False)
    imagen = models.ImageField(upload_to=settings.MEDIA_ROOT / 'productos', null=True)

    def __str__(self) -> str:
        return f'{self.nombre} - {str(self.categoria)}'

class UserData(models.Model):
    correo = models.CharField(max_length=64)
    password = models.CharField(max_length=30)
    


    def __str__(self) -> str:
        return f'{self.correo} ({self.password})' 