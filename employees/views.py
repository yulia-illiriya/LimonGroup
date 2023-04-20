from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from .permissions import IsAdminOrReadOnly
from .models import Employee, Position
from .serializers import EmployeeSerializer, PositionSerializer


class PositionView(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    permission_classes = [IsAdminOrReadOnly,]
    
    
class EmployeeView(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly,]
          

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
    



