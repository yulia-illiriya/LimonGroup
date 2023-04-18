from rest_framework import generics, viewsets
from .models import Employee, Position
from .serializers import EmployeeSerializer, PositionSerializer

class PositionView(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    
    
class EmployeeView(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
          

# class EmployeeDetailUpdateView(generics.RetrieveUpdateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
    
    
# class EmployeeReadDeleteAPIView(generics.RetrieveDestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
    
    
# class PositionDetailView(generics.RetrieveAPIView):
#     queryset = Position.objects.all()
#     serializer_class = PositionSerializer
    
    
# class PositionUpdateAPIView(generics.RetrieveUpdateAPIView):
#     queryset = Position.objects.all()
#     serializer_class = PositionSerializer
#     lookup_field = 'slug'
    
# class PositionDeleteAPIView(generics.RetrieveDestroyAPIView):
#     queryset = Position.objects.all()
#     serializer_class = PositionSerializer
    



