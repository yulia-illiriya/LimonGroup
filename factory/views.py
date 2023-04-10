from rest_framework import generics
from .serializers import (OrderSerializer,
                          SewingModelSerializer,
                          DailyWorkSerializer,
                          NewOrderSerializer, PriceSerializer)
from .models import (Order, SewingModel, DailyWork,
                     NewOrder, Price)


class PriceListCreateAPIView(generics.ListCreateAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer


price_list_create = PriceListCreateAPIView.as_view()


class PriceRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer


price_ret_update = PriceRetrieveUpdateAPIView.as_view()


class PriceRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer


price_ret_destroy = PriceRetrieveDestroyAPIView.as_view()


class SewingModelListCreateAPIView(generics.ListCreateAPIView):
    queryset = SewingModel.objects.all()
    serializer_class = SewingModelSerializer


sewingModel_list_create = SewingModelListCreateAPIView.as_view()


class SewingModelRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = SewingModel.objects.all()
    serializer_class = SewingModelSerializer


sewingModel_ret_update = SewingModelRetrieveUpdateAPIView.as_view()


class SewingModelRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = SewingModel.objects.all()
    serializer_class = SewingModelSerializer


sewingModel_ret_destroy = SewingModelRetrieveDestroyAPIView.as_view()


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
