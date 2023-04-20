from datetime import datetime, timedelta
from rest_framework import serializers

from .models import (
    Client,
    Order,
    NewOrder,
    DailyWork,
    SewingModel,
    FabricCutting,
    RawStuff,
    Storage,
    Price,
    QuantityModel
)



class PriceSerializer(serializers.ModelSerializer):
    end_date = serializers.DateTimeField(default=datetime.now() + timedelta(days=30))

    class Meta:
        model = Price
        fields = ('created_at', 'updated_at', 'start_date', 'end_date', 'is_actual', 'value')
    

class SewingModelSerializer(serializers.ModelSerializer):
    
    """Позволяет сразу создать или подтянуть из базы данных цену """
    
    labor_cost = PriceSerializer()
    client_price = PriceSerializer()

    class Meta:
        model = SewingModel
        fields = "__all__"

    def create(self, validated_data):
        labor_cost_data = validated_data.pop('labor_cost', None)
        client_price_data = validated_data.pop('client_price', None)

        if not labor_cost_data:
            raise serializers.ValidationError("Поле labor_cost обязательно")
        labor_cost, _ = Price.objects.get_or_create(**labor_cost_data)
        validated_data['labor_cost'] = labor_cost

        if not client_price_data:
            raise serializers.ValidationError("Поле client_price обязательно")
        client_price, _ = Price.objects.get_or_create(**client_price_data)
        validated_data['client_price'] = client_price

        sewing_model = SewingModel.objects.create(**validated_data)
        return sewing_model
        
class SewingModelDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SewingModel
        fields = ['color', 'material', 'type', 'labor_cost', 'client_price']


class OrderSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())
    sewing_model = SewingModelSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['client', 'data_poluchenia', 'quantity_zayav', 'quantity_fact', 'data_zakup', 'raskroi_tkani', 'pod_flizelin', 'sewing_model']

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        client_name = instance.client.full_name
        ret['client'] = client_name
        return ret
    
    def create(self, validated_data):
        sewing_models = validated_data.pop('sewing_model', [])
        client = validated_data.pop('client')
        order = Order(client=client, **validated_data)
        order.save()
        for sewing_model_data in sewing_models:
            sewing_model = SewingModel(order=order, **sewing_model_data)
            sewing_model.save()
        
        return order



class NewOrderSerializer(serializers.ModelSerializer):
    client_name = serializers.SerializerMethodField()

    class Meta:
        model = NewOrder
        fields = ['description', 'price', 'color', 'client_name', 'received_date', 'delivery_date']

    def get_client_name(self, obj):
        return obj.client.full_name

    def create(self, validated_data):
        client_name = self.context['request'].data.get('client_name')
        client, _ = Client.objects.get_or_create(full_name=client_name)
        validated_data['client_id'] = client.id
        return super().create(validated_data)


class DailyWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyWork
        fields = '__all__'





class QuantityModelSerializer(serializers.ModelSerializer):
    quantity_models = SewingModelSerializer()
    numbers_for_account = DailyWorkSerializer()
    
    class Meta:
        model = QuantityModel
        fields = ('id', 'quantity_models', 'quantity', 'numbers_for_account')


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
