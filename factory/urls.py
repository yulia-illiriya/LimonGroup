from django.urls import path
from . import views

urlpatterns = [
    # SewingModel
    path('Sewmodel-create/', views.sewingModel_create, name='Sewmodel-create'),
    path('Sewmodel-list/', views.sewingModel_list, name='Sewmodel-list'),
    path('Sewmodel-update/', views.sewingModel_update, name='Sewmodel-update'),
    path('Sewmodel-destroy/', views.sewingModel_destroy, name='Sewmodel-destroy'),

    # Price
    path('price-create/', views.price_create, name='price-create'),
    path('price-list/', views.price_list, name='price-list'),
    path('price-update/', views.price_update, name='price-update'),
    path('price-destroy/', views.price_destroy, name='price-destroy'),



]
