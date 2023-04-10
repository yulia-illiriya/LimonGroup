from django.urls import path
from . import views


urlpatterns = [

    path(
        'listcreate-dailywork/',
        views.DailyWorkListCreateAPIView.as_view(),
        name='list-dailywork'),
    path(
        'update-dailywork/',
        views.DailyWorkRetrieveUpdateAPIView.as_view(),
        name='create-dailywork'),
    path(
        'destroy-dailywork/<int:pk>/',
        views.DailyWorkRetrieveDestroyAPIView.as_view(),
        name='details-dailywork'),
    path(
        'listcreate-neworder/',
        views.NewOrderListAPIView.as_view(),
        name='list-neworder'),
    path(
        'update-neworder/',
        views.NewOrderRetrieveUpdateAPIView.as_view(),
        name='create-neworder'),
    path(
        'destroy-neworder/<int:pk>/',
        views.NewOrderRetrieveDestroyAPIView.as_view(),
        name='details-neworder'),

    # SewingModel
    path(
        'Sewmodel-create/',
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
