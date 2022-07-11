from msilib.schema import ListView
from rest_framework import viewsets, mixins

from .serializers import OfertaSerializer
from .models import Oferta

class OfertaViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Oferta.objects.all()
    serializer_class = OfertaSerializer
