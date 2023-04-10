from django.urls import path
from . import views


urlpatterns = [

    path(
        'listcreate-dailywork/',
        views.DailyWorkListCreateAPIView.as_view(),
        name='list-dailywork'),
    path(
        'update-dailywork/<int:pk>',
        views.DailyWorkRetrieveUpdateAPIView.as_view(),
        name='create-dailywork'),
    path(
        'destroy-dailywork/<int:pk>/',
        views.DailyWorkRetrieveDestroyAPIView.as_view(),
        name='destroy-dailywork'),
    path(
        'listcreate-neworder/',
        views.NewOrderListAPIView.as_view(),
        name='list-neworder'),
    path(
        'update-neworder/<int:pk>',
        views.NewOrderRetrieveUpdateAPIView.as_view(),
        name='update-neworder'),
    path(
        'destroy-neworder/<int:pk>/',
        views.NewOrderRetrieveDestroyAPIView.as_view(),
        name='destroy-neworder'),

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
