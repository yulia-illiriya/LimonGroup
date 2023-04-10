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


    #Storage

    path(
        'storage-list-create/',
        views.StorageListAPIView.as_view(),
        name='price-list-create'),
    path(
        'storage-update/<int:pk>/',
        views.StorageRetrieveUpdateAPIView.as_view(),
        name='price-ret-update'),
    path(
        'storage-destroy/<int:pk>/',
        views.StorageRetrieveDestroyAPIView.as_view(),
        name='price-ret-destroy'),


    #RawStuff

    path(
        'rawstuff-list-create/',
        views.RawStuffListCreateAPIView.as_view(),
        name='price-list-create'),
    path(
        'rawstuff-update/<int:pk>/',
        views.RawStuffRetrieveUpdateAPIView.as_view(),
        name='price-ret-update'),
    path(
        'rawstuff-destroy/<int:pk>/',
        views.RawStuffRetrieveDestroyAPIView.as_view(),
        name='price-ret-destroy'),


    #FabricCutting

    path(
        'fabriccutting-list-create/',
        views.FabricCuttingListCreateAPIView.as_view(),
        name='price-list-create'),
    path(
        'fabriccutting-update/<int:pk>/',
        views.FabricCuttingRetrieveUpdateAPIView.as_view(),
        name='price-ret-update'),
    path(
        'fabriccutting-destroy/<int:pk>/',
        views.FabricCuttingRetrieveDestroyAPIView.as_view(),
        name='price-ret-destroy'),


]
