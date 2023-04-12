from rest_framework import serializers
from .models import CatalogCategory, Catalog
from client.models import Client
from factory.models import SewingModel
from factory.serializers import SewingModelSerializer, OrderSerializer, NewOrderSerializer


class ClientSerializer(serializers.ModelSerializer):
    sewing_model = SewingModelSerializer(many=True, read_only=True)
    order = OrderSerializer(many=True, read_only=True)
    new_order = NewOrderSerializer(read_only=True)
    
    
    class Meta:
        model = Client
        fields = ['full_name', 'contacts', 'address', 'is_new', 'created_at', 'sewing_model', 'order', 'new_order']
    
    

class CatalogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CatalogCategory
        fields = "__all__"


class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = "__all__"
