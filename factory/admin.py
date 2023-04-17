from django.contrib import admin
from django.db.models import F

from .models import DailyWork, NewOrder, Price, QuantityModel, SewingModel


class QuantityModelAdmin(admin.ModelAdmin):
    list_display = ['sewing_model', 'quantity']


admin.site.register(QuantityModel, QuantityModelAdmin)


class PriceAdmin(admin.ModelAdmin):
    list_display = ['created_at',
                    'updated_at',
                    'start_date',
                    'end_date',
                    'is_actual',
                    'value']

    ordering = ['-created_at']


admin.site.register(Price, PriceAdmin)


class QuatityInline(admin.TabularInline):
    model = QuantityModel
    fields = [
        "sewing_model",
        "quantity"
    ]


class DailyWorkAdmin(admin.ModelAdmin):
    list_display = [
        'employee',
        'date',
        'prepayment',
        'total_cost',
    ]
    inlines = [
        QuatityInline
    ]
    readonly_fields = ["total_cost", "daily_salary"]

    ordering = ['date']


admin.site.register(DailyWork, DailyWorkAdmin)


class NewOrderAdmin(admin.ModelAdmin):
    list_display = ['sewing_model',
                    'price',
                    'color',
                    'image',
                    'client',
                    'received_date',
                    'delivery_date']

    ordering = ['received_date']


admin.site.register(NewOrder, NewOrderAdmin)


class SewingModelAdmin(admin.ModelAdmin):
    list_display = ['client',
                    'color',
                    'material',
                    'type',
                    'labor_cost',
                    'client_price']


admin.site.register(SewingModel, SewingModelAdmin)
