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
    class Meta:
        model = Price
        fields = "__all__"


class SewingModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SewingModel
        fields = "__all__"


class SewingModelDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SewingModel
        fields = ['color', 'material', 'type', 'labor_cost', 'client_price']


class OrderSerializer(serializers.ModelSerializer):
    sewing_model = SewingModelDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['data_poluchenia', 'quantity_zayav', 'quantity_fact', 'data_zakup', 'raskroi_tkani', 'pod_flizelin',
                  'sewing_model']


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


class QuantityModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuantityModel
        fields = ('id',
                  'sewing_model',
                  'quantity')


class DailyWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyWork
        fields = ('employee',
                  'date',
                  'prepayment',
                  'daily_salary',
                  'total_cost',
                  'quantity'
                  )

    def create(self, validated_data):
        quantity_data = validated_data.pop('quantity')
        daily_work = DailyWork.objects.create(validated_data)
        for data in quantity_data:
            QuantityModel.objects.create(daily_work=daily_work, *data)
        return daily_work


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
