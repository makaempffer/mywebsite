from django.db import models

class Oferta(models.Model):
    nombre = models.TextField(max_length=64)
    descripcion = models.TextField(max_length=512, default='')
    vigente = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.nombre}'