from rest_framework import serializers

from client.models import Client

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


from .models import CatalogCategory, Catalog


class CatalogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CatalogCategory
        fields = "__all__"


class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = "__all__"
