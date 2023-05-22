from datetime import datetime, timedelta, date
from decimal import Decimal
from django.db.models import Sum, F
from rest_framework import serializers
from .services import update_daily_salary

from employees.serializers import EmployeeSerializer

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
    QuantityModel,
)
from employees.models import Employee


class PriceSerializer(serializers.ModelSerializer):
    end_date = serializers.DateTimeField(default=datetime.now() + timedelta(days=30))

    class Meta:
        model = Price
        fields = ('created_at', 'updated_at', 'start_date', 'end_date', 'is_actual', 'value')


class SewingModelSerializer(serializers.ModelSerializer):
    """Позволяет сразу создать или подтянуть из базы данных цену """

    cost = PriceSerializer()
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
    sewing_model = SewingModelDetailSerializer(many=True, read_only=True)
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())

    class Meta:
        model = Order
        fields = [
            'client', 
            'data_poluchenia', 
            'quantity_zayav', 
            'quantity_fact', 
            'data_zakup', 
            'raskroi_tkani', 
            'pod_flizelin', 
            'sewing_model'
            ]

        fields = ['client', 'data_poluchenia', 'quantity_zayav', 'quantity_fact', 'data_zakup', 'raskroi_tkani',
                  'pod_flizelin', 'sewing_model']

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
    
    sewing_model = serializers.PrimaryKeyRelatedField(queryset=SewingModel.objects.all())
        
    class Meta:
        model = QuantityModel
        fields = ('sewing_model', 'quantity')
         
    def create(self, validated_data):
        print(validated_data)        
        sewing_model_id = validated_data.pop('sewing_model')
        sewing_model = SewingModel.objects.get(pk=sewing_model_id)
        validated_data['sewing_model'] = sewing_model
        return super().create(validated_data)


class DailyWorkSerializer(serializers.ModelSerializer):
    employee = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all())
    # daily_salary = serializers.DecimalField(max_digits=7, decimal_places=2)
    sewing_models = QuantityModelSerializer(source='numbers_for_account', many=True)
    
    class Meta:
        model = DailyWork
        fields = ('id', 'employee', 'date', 'prepayment', 'daily_salary', 'sewing_models')
         
    def create(self, validated_data):
        sewing_models_data = validated_data.pop('numbers_for_account')
        today = date.today()
        employee = validated_data['employee']
        daily_work, _ = DailyWork.objects.get_or_create(employee=employee, date=today, defaults=validated_data)
        
        quantity_models = []       
        for i in sewing_models_data:
            print(sewing_models_data)
            sewing_model_str =str(i['sewing_model']).split(' ')            
            quantity = i['quantity']
            
            sewing_model = SewingModel.objects.get(type=sewing_model_str[0], color=sewing_model_str[1], material=sewing_model_str[2])
            print(sewing_model)
            quantity_models.append(QuantityModel(daily_work=daily_work, sewing_model=sewing_model, quantity=quantity))
            
        QuantityModel.objects.bulk_create(quantity_models)
        
        update_daily_salary(daily_work)
              
        return daily_work
    
    def update(self, instance, validated_data):
        # Обработка обновления вложенных полей sewing_models
        sewing_models_data = validated_data.pop('numbers_for_account', None)
        if sewing_models_data is not None:
            instance.numbers_for_account.all().delete()  # Удаление всех связанных объектов QuantityModel
            quantity_models = []
            for i in sewing_models_data:
                sewing_model_str =str(i['sewing_model']).split(' ')            
                quantity = i['quantity']
                sewing_model = SewingModel.objects.get(type=sewing_model_str[0], color=sewing_model_str[1], material=sewing_model_str[2])
                quantity_models.append(QuantityModel(daily_work=instance, sewing_model=sewing_model, quantity=quantity))
            QuantityModel.objects.bulk_create(quantity_models)

        # Обновление остальных полей модели DailyWork
        instance.employee = validated_data.get('employee', instance.employee)
        instance.date = validated_data.get('date', instance.date)
        instance.prepayment = validated_data.get('prepayment', instance.prepayment)
        instance.daily_salary = validated_data.get('daily_salary', instance.daily_salary)
        instance.save()

        update_daily_salary(instance)  # Вызов функции update_daily_salary после обновления объекта DailyWork
        return instance


class FabricCuttingSerializer(serializers.ModelSerializer):
    sewing_model = SewingModel.objects.all()
    storage_model = Storage.objects.all()
    # add method get create
    class Meta:
        model = FabricCutting
        fields = '__all__'


class RawStuffSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawStuff
        fields = '__all__'


class StorageSerializer(serializers.ModelSerializer):
    product = RawStuff.objects.all()
    # add func create update
    class Meta:
        model = Storage
        fields = ["product"]
