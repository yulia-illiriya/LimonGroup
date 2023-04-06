from django.shortcuts import render

from .serializers import OrderSerializer
from .models import Order

from rest_framework import generics





class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = None
    