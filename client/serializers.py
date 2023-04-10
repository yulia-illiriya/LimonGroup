from rest_framework import serializers
from .models import CatalogCategory, Catalog
from client.models import Client
from factory.models import SewingModel
from factory.serializers import SewingModelSerializer


class ClientSerializer(serializers.ModelSerializer):
    actual_model = SewingModelSerializer(many=True, read_only=True)
    
    class Meta:
        model = Client
        fields = ['full_name', 'contacts', 'address', 'is_new', 'created_at', 'actual_model']


class CatalogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CatalogCategory
        fields = "__all__"


class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = "__all__"
