from rest_framework import generics
from .models import Employee, Position
from .serializers import EmployeeSerializer, PositionSerializer

class PositionView(generics.ListCreateAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    
    
class EmployeeListView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
          

class EmployeeDetailUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
    
class PositionDetailView(generics.RetrieveAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    
    
class PositionUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    lookup_field = 'slug'
    
class PositionDeleteAPIView(generics.RetrieveDestroyAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    



