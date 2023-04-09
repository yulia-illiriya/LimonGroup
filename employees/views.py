from rest_framework import generics
from .models import Employee, Position
from .serializers import EmployeeSerializer, PositionSerializer

class PositionView(generics.ListCreateAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    
class EmployeeListView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    

    


