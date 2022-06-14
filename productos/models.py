from django.db import models

class Mascota(models.Model):
    nombre = models.TextField(max_length=64)
    descripcion = models.TextField(max_length=512, default='')

    def __str__(self) -> str:
        return f'{self.nombre}'

class Categoria(models.Model):
    nombre = models.TextField(max_length=64)
    descripcion = models.TextField(max_length=512, default='')
    mascota = models.ForeignKey(Mascota, related_name='mascota', on_delete=models.CASCADE, null=True)
    imagen = models.ImageField(upload_to='static/categorias/', null=True)

    def __str__(self) -> str:
        return f'{self.nombre}'

class Producto(models.Model):

    nombre = models.TextField(max_length=64, blank=False)
    categoria = models.ForeignKey(Categoria, related_name='categoria', on_delete=models.CASCADE, null=True)
    descripcion = models.TextField(max_length=512, blank=False)
    precio = models.PositiveIntegerField(blank=False)
    imagen = models.ImageField(upload_to='static/productos/', null=True)

    def __str__(self) -> str:
        return f'{self.nombre} [{self.mascota.nombre} / {self.categoria.nombre}]'