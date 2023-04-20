from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsAdminPermission
from client.models import Client
from client.serializers import ClientSerializer


class ClientAPIViews(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated,]

 

class ClientListCreateAPIViews(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAdminPermission,]


class ClientDetailUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAdminPermission,]


class ClientReadDeleteAPIView(generics.RetrieveDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAdminPermission,]
