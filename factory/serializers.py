from rest_framework import serializers
from client.models import Client


from .models import (
    Order,
    NewOrder,
    DailyWork,
    SewingModel, FabricCutting, RawStuff, Storage
)

from .models import Order, SewingModel, Price


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = "__all__"



class SewingModelSerializer(serializers.ModelSerializer):
    client = serializers.SlugRelatedField(slug_field='full_name', queryset=Client.objects.all())
    
    class Meta:
        model = SewingModel
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class NewOrderSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = NewOrder
        fields = '__all__'


class DailyWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyWork
        fields = '__all__'


class FabricCuttingSerializer(serializers.ModelSerializer):
    class Meta:
        model = FabricCutting
        fields = '__all__'


class RawStuffSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawStuff
        fields = '__all__'


class StorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = '__all__'