from django.urls import path, include
from rest_framework import routers
from . import views
from factory.views import *

router = routers.DefaultRouter()
# router.register(r'order', OrderViewSet) пока не нужно
router.register(r'storage', StorageViewSet)
# router.register(r'rawstuff', RawStuffViewSet) пока не нужен 
router.register(r'fabriccutting', FabricCuttingViewSet)
router.register(r'sewingmodel', SewingModelViewSet)
router.register(r'dailywork', DailyWorkViewSet)
router.register(r'neworder', NewOrderViewSet)

urlpatterns = [

    # NewOrder
    path('', include(router.urls), name='neworder'),

    # DailyWork
    path('', include(router.urls), name='dailywork'),

    # SewingModel
    path('', include(router.urls), name='sewingmodel'),

    # Price
    # path('price/', include(router.urls), name='price'),

    # Storage
    path('', include(router.urls), name='storage'),

    # RawStuff
    # path('rawstuff/', include(router.urls), name='rawstuff'),

    # FabricCutting
    path('', include(router.urls), name='fabriccutting'),

    # Order
    # path('order/', include(router.urls), name='order'),

    # Production
    path('production-per-day/', views.ProductionWork.as_view(), name="production")

] + router.urls







