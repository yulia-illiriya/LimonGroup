from rest_framework import serializers

from .models import (
    Client,
    Order,
    NewOrder,
    DailyWork,
    SewingModel, FabricCutting, RawStuff, Storage, Price, QuantityModel
)


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
    # sewing_model = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = NewOrder
        fields = '__all__'


class QuantityModelSerializer(serializers.ModelSerializer):
    # sewing_model = serializers.StringRelatedField()

    class Meta:
        model = QuantityModel
        fields = '__all__'


class DailyWorkSerializer(serializers.ModelSerializer):
    daily_salary = serializers.ReadOnlyField()

    class Meta:
        model = DailyWork
        fields = ('employee',
                  'quantity',
                  'date',
                  'prepayment',
                  'daily_salary')


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
