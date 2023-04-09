from rest_framework import serializers
from .models import Employee, Position
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

import json

class PositionSerializer(serializers.ModelSerializer):
    permission_classes = [AllowAny,]
         
    class Meta:
        model = Position
        fields = ['name', 'is_active']
        
    
class EmployeeSerializer(serializers.ModelSerializer):
    permission_classes = [AllowAny,]
    position = PositionSerializer
    
    class Meta:
        model = Employee
        fields = "__all__"
        
