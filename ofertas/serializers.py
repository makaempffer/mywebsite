import imp
from rest_framework import serializers
from .models import Oferta

class OfertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oferta
        fields = ['nombre', 'descripcion', 'vigente']