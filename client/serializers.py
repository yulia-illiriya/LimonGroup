from rest_framework import serializers
from .models import CatalogCategory, Catalog
from client.models import Client
from factory.models import SewingModel, Order
from factory.serializers import SewingModelSerializer, OrderSerializer, NewOrderSerializer


class ClientSerializer(serializers.ModelSerializer):
    order = serializers.SerializerMethodField()
    new_pattern = NewOrderSerializer(many=True, read_only=True)  
    
    class Meta:
        model = Client
        fields = ['full_name', 'contacts', 'address', 'is_new', 'created_at', 'order', 'new_pattern']
    
    def get_order(self, obj):
        orders = Order.objects.filter(client=obj)
        serialized_order = OrderSerializer(orders, many=True).data
        result = []
        for order in serialized_order:
            result.append({
                'data_poluchenia': order['data_poluchenia'],
                'quantity_zayav': order['quantity_zayav'],
                'data_zakup': order['data_zakup'],
                'raskroi_tkani': order['raskroi_tkani'],
                'pod_flizelin': order['pod_flizelin'],
                'sewing_model': order['sewing_model']              
            })
        return result

class CatalogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CatalogCategory
        fields = "__all__"


class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = "__all__"
