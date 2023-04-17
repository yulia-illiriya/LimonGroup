from rest_framework import generics, viewsets
from client.models import Client
from client.serializers import ClientSerializer

class ClientAPIViews(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    

    
