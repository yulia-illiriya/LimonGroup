from rest_framework import serializers
from .models import Employee, Position
from rest_framework.permissions import AllowAny


class PositionSerializer(serializers.ModelSerializer):
    permission_classes = [AllowAny,]
    # employee = serializers.StringRelatedField(many=True)
         
    class Meta:
        model = Position
        fields = ['name', 'is_active']
        
    
class EmployeeSerializer(serializers.ModelSerializer):
    permission_classes = [AllowAny,]
    position = serializers.SlugRelatedField(slug_field='name', queryset=Position.objects.all())
                
    class Meta:
        model = Employee
        fields = '__all__'
        
    
    
