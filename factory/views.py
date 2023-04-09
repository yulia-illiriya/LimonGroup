from django.shortcuts import render

from .serializers import OrderSerializer, SewingModelSerializer
from .models import Order, SewingModel

from rest_framework import generics


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
