from rest_framework import serializers

from .models import (Order,
                     NewOrder,
                     DailyWork)

from .models import Order, SewingModel


class SewingModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SewingModel
        fieds = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class NewOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewOrder
        fields = '__all__'
