from rest_framework import serializers
from .models import Employee, Position
from rest_framework.permissions import AllowAny, IsAuthenticated
from .permissions import IsAdminOrReadOnly


class EmployeeSerializer(serializers.ModelSerializer):
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly, ]
    position = serializers.SlugRelatedField(slug_field='name', queryset=Position.objects.all())

    class Meta:
        model = Employee
        fields = '__all__'


class PositionSerializer(serializers.ModelSerializer):
    permission_classes = [IsAdminOrReadOnly, ]
    employees = EmployeeSerializer(many=True, read_only=True)


    class Meta:
        model = Position
        fields = ['name', 'is_active', 'employees', 'slug']
