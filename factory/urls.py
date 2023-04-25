from django.urls import path, include
from rest_framework import routers
from . import views
from factory.views import *

router = routers.DefaultRouter()
router.register(r'order', OrderViewSet)
router.register(r'storage', StorageViewSet)
router.register(r'rawstuff', RawStuffViewSet)
router.register(r'fabriccutting', FabricCuttingViewSet)

urlpatterns = [

    path(
        'list-dailywork/',
        views.DailyWorkListAPIView.as_view(),
        name='list-dailywork'),
    path(
        'create-dailywork/<int:pk>/',
        views.DailyWorkCreateUpdateAPIView.as_view(),
        name='create-update-dailywork'),
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

    # Storage
    path('factory/storage/', include(router.urls), name='storage'),

    # RawStuff
    path('factory/rawstuff/', include(router.urls), name='rawstuff'),

    # FabricCutting
    path('factory/fabriccutting/', include(router.urls), name='fabriccutting'),

    #Order
    path('factory/order/', include(router.urls), name='order'),

    # Production
    path('production-per-day/', views.ProductionWork.as_view(), name="production")

] + router.urls





