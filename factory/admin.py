from django.contrib import admin
from .models import DailyWork, NewOrder, Price\



admin.site.register(Price)



class DailyAdmin(admin.ModelAdmin):
    list_display = ['employee',
                    'quantity',
                    'date',
                    'prepayment']

    ordering = ['date']


admin.site.register(DailyWork, DailyAdmin)


class NewOrderAdmin(admin.ModelAdmin):
    list_display = ['product',
                    'price',
                    'color',
                    'image',
                    'client',
                    'received_date',
                    'delivery_date']

    ordering = ['received_date']


admin.site.register(NewOrder, NewOrderAdmin)
