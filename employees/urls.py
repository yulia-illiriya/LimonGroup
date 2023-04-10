from django.urls import path
from employees.views import PositionView, EmployeeListView, EmployeeDetailUpdateView, PositionUpdateAPIView, PositionDeleteAPIView, EmployeeReadDeleteAPIView

urlpatterns = [
    path("employees/", EmployeeListView.as_view()),
    path("position/", PositionView.as_view()),
    path('employees/<int:pk>/', EmployeeDetailUpdateView.as_view(), name='Сотрудник'),
    path('employees/delete/<int:pk>/', EmployeeReadDeleteAPIView.as_view(), name='Удалить сотрудника'),
    path('position/<slug:slug>/', PositionUpdateAPIView.as_view(), name='Должность'),
    path('position/delete/<int:pk>', PositionDeleteAPIView.as_view(), name="Удалить должность"), 
]
