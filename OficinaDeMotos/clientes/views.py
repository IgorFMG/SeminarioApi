from rest_framework import viewsets
from clientes.models import clientes
from clientes.serializer import clientesSerializer

class clientesViewSet(viewsets.ModelViewSet):
    queryset = clientes.objects.all()
    serializer_class = clientesSerializer