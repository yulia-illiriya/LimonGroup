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
        'Sewmodel-update/<int:pk>/',
        views.sewingModel_ret_update,
        name='Sewmodel-ret-update'),

    path(
        'Sewmodel-destroy/<int:pk>/',
        views.sewingModel_ret_destroy,
        name='Sewmodel-ret-destroy'),


    # Price
    path(
        'price-list-create/',
        views.price_list_create,
        name='price-list-create'),
    path(
        'price-update/<int:pk>/',
        views.price_ret_update,
        name='price-ret-update'),
    path(
        'price-destroy/<int:pk>/',
        views.price_ret_destroy,
        name='price-ret-destroy'),



]
