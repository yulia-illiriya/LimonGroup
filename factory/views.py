from rest_framework import generics, viewsets
from django.db.models.query import QuerySet
from decimal import Decimal
from django.db.models import F, Sum

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .services import get_production
from accounts.permissions import IsTechnologist, IsAdminPermission
from employees.permissions import IsAdminOrReadOnly
from .serializers import (OrderSerializer,
                          SewingModelSerializer,
                          DailyWorkSerializer,
                          NewOrderSerializer,
                          PriceSerializer,
                          FabricCuttingSerializer,
                          RawStuffSerializer,
                          StorageSerializer, )
from .models import (Order, SewingModel, DailyWork,
                     NewOrder, Price, FabricCutting, RawStuff, Storage)


# class PriceViewSet(viewsets.ModelViewSet):
#     queryset = Price.objects.all()
#     serializer_class = PriceSerializer


class SewingModelViewSet(viewsets.ModelViewSet):
    queryset = SewingModel.objects.all()
    serializer_class = SewingModelSerializer


class DailyWorkViewSet(viewsets.ModelViewSet):
    queryset = DailyWork.objects.all()
    serializer_class = DailyWorkSerializer
    http_method_names = ['get', 'post']
    permission_classes = [IsAdminPermission, IsTechnologist]

class NewOrderViewSet(viewsets.ModelViewSet):
    queryset = NewOrder.objects.all()
    serializer_class = NewOrderSerializer
    permission_classes = [IsAdminPermission, IsTechnologist]


class FabricCuttingViewSet(viewsets.ModelViewSet):
    queryset = FabricCutting.objects.all()
    serializer_class = FabricCuttingSerializer
    permission_classes = [IsAdminOrReadOnly, ]



class RawStuffViewSet(viewsets.ModelViewSet):
    queryset = RawStuff.objects.all()
    serializer_class = RawStuffSerializer


class StorageViewSet(viewsets.ModelViewSet):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer
    http_method_names = ['get', 'post']




class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        print(request.data)
        return super().create(request, *args, **kwargs)


class ProductionWork(APIView):
    def get(self, request):
        date = request.data.get('date')
        if not date:
            return Response({'error': 'Вы не указали дату'}, status=400)

        summary = get_production(date)

        return Response(summary)
