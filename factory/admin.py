from django.contrib import admin
from .models import DailyWork


class DailyAdmin(admin.ModelAdmin):
    list_display = ['employee',
                    'quantity',
                    'date',
                    'prepayment']

    ordering = ['date']


admin.site.register(DailyWork, DailyAdmin)
