from django.urls import path, include
from rest_framework import routers
from employees.views import PositionView, EmployeeView

router = routers.DefaultRouter()
router.register(r'employee', EmployeeView)
router.register(r'position', PositionView)

urlpatterns = [
    path("v1/", include(router.urls)),

    
]
