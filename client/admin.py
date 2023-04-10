from django.contrib import admin
from .models import (Client,
                     Catalog,
                     CatalogCategory)


class ClientAdmin(admin.ModelAdmin):
    list_display = ['full_name',
                    'contacts',
                    'address',
                    'is_new',
                    'created_at']

    ordering = ['created_at']


admin.site.register(Client, ClientAdmin)


class CatalogAdmin(admin.ModelAdmin):
    list_display = ['articul',
                    'colors',
                    'image',
                    'quantity',
                    'category']

    ordering = ['category']


admin.site.register(Catalog, CatalogAdmin)


class CatalogCategoryAdmin(admin.ModelAdmin):
    list_display = ['name',
                    'slug']

    ordering = ['name']


admin.site.register(CatalogCategory, CatalogCategoryAdmin)
