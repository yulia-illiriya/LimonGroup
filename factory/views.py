
from django.shortcuts import render

from .serializers import OrderSerializer, SewingModelSerializer, PriceSerializer
from .models import Order, SewingModel, Price


from rest_framework import generics
from .serializers import (OrderSerializer,
                          SewingModelSerializer,
                          DailyWorkSerializer,
                          NewOrderSerializer)
from .models import (Order,
                     SewingModel,
                     DailyWork,
                     NewOrder)


class PriceListAPIView(generics.ListAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer


price_list = PriceListAPIView.as_view()


class PriceCreateAPIView(generics.CreateAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer


price_create = PriceCreateAPIView.as_view()


class PriceUpdateAPIView(generics.UpdateAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer


price_update = PriceUpdateAPIView.as_view()


class PriceDestroyAPIView(generics.DestroyAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer


price_destroy = PriceDestroyAPIView.as_view()


class SewingModelListAPIView(generics.ListAPIView):
    queryset = SewingModel.objects.all()
    serializer_class = SewingModelSerializer


sewingModel_list = SewingModelListAPIView.as_view()


class SewingModelCreateAPIView(generics.CreateAPIView):
    queryset = SewingModel.objects.all()
    serializer_class = SewingModelSerializer


sewingModel_create = SewingModelCreateAPIView.as_view()


class SewingModelUpdateAPIView(generics.UpdateAPIView):
    queryset = SewingModel.objects.all()
    serializer_class = SewingModelSerializer


sewingModel_update = SewingModelUpdateAPIView.as_view()


class SewingModelDestroyAPIView(generics.DestroyAPIView):
    queryset = SewingModel.objects.all()
    serializer_class = SewingModelSerializer


sewingModel_destroy = SewingModelDestroyAPIView.as_view()


class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = None


class DailyWorkListAPIView(generics.ListAPIView):
    queryset = DailyWork.objects.all()
    serializer_class = DailyWorkSerializer


class DailyWorkCreateAPIView(generics.CreateAPIView):
    queryset = DailyWork.objects.all()
    serializer_class = DailyWorkSerializer


class DailyWorkDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DailyWork.objects.all()
    serializer_class = DailyWorkSerializer


class NewOrderListAPIView(generics.ListAPIView):
    queryset = NewOrder.objects.all()
    serializer_class = NewOrderSerializer


class NewOrderCreateAPIView(generics.CreateAPIView):
    queryset = NewOrder.objects.all()
    serializer_class = NewOrderSerializer


class NewOrderDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NewOrder.objects.all()
    serializer_class = NewOrderSerializer
