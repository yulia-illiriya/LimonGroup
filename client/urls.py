from django.urls import path, include
from rest_framework import routers
from .views import ClientAPIViews

router = routers.DefaultRouter()
router.register(r'client', ClientAPIViews)


urlpatterns = [
    path("v2/", include(router.urls)),
]