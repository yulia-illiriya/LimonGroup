from decimal import Decimal
from django.db.models import Sum
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.response import Response
from .models import DailyWork, SewingModel, QuantityModel
from .serializers import QuantityModelSerializer


class CustomDateField(serializers.DateField):
    def to_representation(self, value):        
        return value.strftime('%d.%m.%Y')


from django.db.models import Sum

def get_production(date):
    daily_works = DailyWork.objects.filter(date=date)
    sewing_models = SewingModel.objects.filter(quantity_models__daily_work__in=daily_works).distinct()

    summary = []
    total_quantity = 0
    total_cost = Decimal('0.00')
    for sewing_model in sewing_models:
        quantity = QuantityModel.objects.filter(sewing_model=sewing_model, daily_work__in=daily_works).aggregate(Sum('quantity'))
        total_quantity += quantity['quantity__sum']
        client_price = sewing_model.client_price.value
        cost = client_price * quantity['quantity__sum']
        total_cost += cost

        
        sewing_model_name = f"{sewing_model.type} {sewing_model.color} {sewing_model.material}"
        summary.append({
            'sewing_model': sewing_model_name,
            'quantity': quantity['quantity__sum'],
            'total_cost': cost
        })

    
    summary.append({
        'Total': 'Итого:',
        'quantity': total_quantity,
        'total_cost': total_cost
    })

    return summary
