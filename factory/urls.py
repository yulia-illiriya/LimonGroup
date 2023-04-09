from django.urls import path
from . import views


urlpatterns = [

    path('create-Sewmodel/', views.sewingModel_create, name='create-Sewmodel'),
    path('list-Sewmodel/', views.sewingModel_list, name='list-Sewmodel'),
    path('update-Sewmodel/', views.sewingModel_update, name='update-Sewmodel'),
    path('destroy-Sewmodel/', views.sewingModel_destroy, name='destroy-Sewmodel'),
    path('list-dailywork/', views.DailyWorkListAPIView.as_view(), name='list-dailywork'),
    path('create-dailywork/', views.DailyWorkCreateAPIView.as_view(), name='create-dailywork'),
    path('details-dailywork/', views.DailyWorkDetailsAPIView.as_view(), name='details-dailywork'),
    path('list-neworder/', views.NewOrderListAPIView.as_view(), name='list-neworder'),
    path('create-neworder/', views.NewOrderCreateAPIView.as_view(), name='create-neworder'),
    path('details-neworder/', views.NewOrderDetailsAPIView.as_view(), name='details-neworder')

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
