from django.urls import path
from . import views


urlpatterns = [

    path(
        'list-dailywork/',
        views.DailyWorkListAPIView.as_view(),
        name='list-dailywork'),
    path(
        'create-dailywork/',
        views.DailyWorkCreateAPIView.as_view(),
        name='create-dailywork'),
    path(
        'details-dailywork/',
        views.DailyWorkDetailsAPIView.as_view(),
        name='details-dailywork'),
    path(
        'list-neworder/',
        views.NewOrderListAPIView.as_view(),
        name='list-neworder'),
    path(
        'create-neworder/',
        views.NewOrderCreateAPIView.as_view(),
        name='create-neworder'),
    path(
        'details-neworder/',
        views.NewOrderDetailsAPIView.as_view(),
        name='details-neworder'),

    # SewingModel
    path(
        'Sewmodel-list-create/',
        views.sewingModel_list_create,
        name='Sewmodel-list-create'),
    path(
        'Sewmodel-details/<int:pk>/',
        views.sewingModel_details,
        name='Sewmodel-details'),

    # Price
    path(
        'price-list-create/',
        views.price_list_create,
        name='price-list-create'),
    path('price-details/<int:pk>/', views.price_details, name='price-details'),



]
