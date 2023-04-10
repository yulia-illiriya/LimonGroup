from django.contrib import admin
from .models import Position, Employee


class PositionAdmin(admin.ModelAdmin):
    list_display = ['name',
                    'is_active']

    ordering = ['name']


admin.site.register(Position, PositionAdmin)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['full_name',
                    'contacts',
                    'start_date',
                    'position',
                    'salary']

    ordering = ['position']


admin.site.register(Employee, EmployeeAdmin)
