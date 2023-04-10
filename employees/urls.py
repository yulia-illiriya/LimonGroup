from django.urls import path
from employees.views import PositionView, EmployeeListView, EmployeeDetailView

urlpatterns = [
    path("employees/", EmployeeListView.as_view()),
    path("position", PositionView.as_view()),
    path('employees/<int:pk>/', EmployeeDetailView.as_view(), name='Сотрудник')
]
