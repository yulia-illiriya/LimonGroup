from django.urls import path
from employees.views import PositionView, EmployeeListView

urlpatterns = [
    path("employees/", EmployeeListView.as_view()),
    path("position", PositionView.as_view()),
]
