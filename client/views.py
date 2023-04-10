from rest_framework import generics
from client.models import Client
from client.serializers import ClientSerializer

class ClientListCreateAPIViews(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    
class ClientDetailUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    
class ClientReadDeleteAPIView(generics.RetrieveDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    
