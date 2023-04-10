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


class PriceUpdateAPIView(generics.UpdateAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer


price_details = PriceUpdateAPIView.as_view()


class SewingModelListCreateAPIView(generics.ListCreateAPIView):
    queryset = SewingModel.objects.all()
    serializer_class = SewingModelSerializer


sewingModel_list_create = SewingModelListCreateAPIView.as_view()


class SewingModelRetrieveUpdateDestroyAPIView(
    generics.RetrieveUpdateDestroyAPIView):
    queryset = SewingModel.objects.all()
    serializer_class = SewingModelSerializer


sewingModel_details = SewingModelRetrieveUpdateDestroyAPIView.as_view()


class DailyWorkListCreateAPIView(generics.ListCreateAPIView):
    queryset = DailyWork.objects.all()
    serializer_class = DailyWorkSerializer


class DailyWorkRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = DailyWork.objects.all()
    serializer_class = DailyWorkSerializer


class DailyWorkRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = DailyWork.objects.all()
    serializer_class = DailyWorkSerializer


class NewOrderListAPIView(generics.ListCreateAPIView):
    queryset = NewOrder.objects.all()
    serializer_class = NewOrderSerializer


class NewOrderRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = NewOrder.objects.all()
    serializer_class = NewOrderSerializer


class NewOrderRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = NewOrder.objects.all()
    serializer_class = NewOrderSerializer

