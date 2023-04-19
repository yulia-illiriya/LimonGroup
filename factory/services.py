from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.response import Response
from .models import DailyWork


class CustomDateField(serializers.DateField):
    def to_representation(self, value):        
        return value.strftime('%d.%m.%Y')

