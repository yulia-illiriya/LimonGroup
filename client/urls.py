from django.urls import path
from .views import ClientListCreateAPIViews, ClientDetailUpdateAPIView, ClientReadDeleteAPIView

urlpatterns = [
    path("client-list/", ClientListCreateAPIViews.as_view(), name='Клиенты'),
    path("client-list/<int:pk>/", ClientDetailUpdateAPIView.as_view(), name='Клиент'),
    # path('employees/<int:pk>/', EmployeeDetailUpdateView.as_view(), name='Сотрудник'),
    path('client-list/delete/<int:pk>/', ClientReadDeleteAPIView.as_view(), name='Удалить клиента'),
    # path('position/<slug:slug>/', PositionUpdateAPIView.as_view(), name='Должность'),
    # path('position/delete/<int:pk>', PositionDeleteAPIView.as_view(), name="Удалить должность"), 
]