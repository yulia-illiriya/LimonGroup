from rest_framework import serializers
from .models import (Order,
                     NewOrder,
                     DailyWork)


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class NewOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewOrder
        fields = '__all__'
