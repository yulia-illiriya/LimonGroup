from django.urls import path, include
from rest_framework import routers
from . import views
from factory.views import *

router = routers.DefaultRouter()
router.register(r'order', OrderViewSet)
router.register(r'storage', StorageViewSet)
router.register(r'rawstuff', RawStuffViewSet)
router.register(r'fabriccutting', FabricCuttingViewSet)
router.register(r'price', PriceViewSet)
router.register(r'sewingmodel', SewingModelViewSet)
router.register(r'dailywork', DailyWorkViewSet)
router.register(r'neworder', NewOrderViewSet)

urlpatterns = [

    # NewOrder
    path('factory/neworder/', include(router.urls), name='NewOrder'),

    # DailyWork
    path('factory/dailyworkModel/', include(router.urls), name='DailyWork'),

    # SewingModel
    path('factory/sewingmodel/', include(router.urls), name='SewingModel'),

    # Price
    path('factory/price/', include(router.urls), name='price'),

    # Storage
    path('factory/storage/', include(router.urls), name='storage'),

    # RawStuff
    path('factory/rawstuff/', include(router.urls), name='rawstuff'),

    # FabricCutting
    path('factory/fabriccutting/', include(router.urls), name='fabriccutting'),

    # Order
    path('factory/order/', include(router.urls), name='order'),

    # Production
    path('production-per-day/', views.ProductionWork.as_view(), name="production")

] + router.urls





