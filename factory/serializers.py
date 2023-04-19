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

from factory.services import CustomDateField

class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = "__all__"


class SewingModelSerializer(serializers.ModelSerializer):
    
    """Позволяет сразу создать или подтянуть из базы данных цену """
    
    labor_cost = PriceSerializer()
    client_price = PriceSerializer()

    class Meta:
        model = SewingModel
        fields = "__all__"

<<<<<<< HEAD

=======
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
        
>>>>>>> 7c8006da84bb32770c5b1603d4363539684e6774
class SewingModelDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SewingModel
        fields = ['color', 'material', 'type', 'labor_cost', 'client_price']


class OrderSerializer(serializers.ModelSerializer):
<<<<<<< HEAD
    sewing_model = SewingModelDetailSerializer(many=True, read_only=True)
=======
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())
    sewing_model = SewingModelSerializer(many=True, read_only=True)
>>>>>>> 7c8006da84bb32770c5b1603d4363539684e6774

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
