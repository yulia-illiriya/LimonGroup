from django.urls import path
from . import views


urlpatterns = [
    path('create-Sewmodel/', views.sewingModel_create, name='create-Sewmodel'),
    path('list-Sewmodel/', views.sewingModel_list, name='list-Sewmodel'),
    path('update-Sewmodel/', views.sewingModel_update, name='update-Sewmodel'),
    path('destroy-Sewmodel/', views.sewingModel_destroy, name='destroy-Sewmodel'),
    path('list-dailywork/', views.DailyWorkListAPIView.as_view(), name='list-dailywork'),
    path('create-dailywork/', views.DailyWorkCreateAPIView.as_view(), name='create-dailywork'),
    path('details-dailywork/', views.DailyWorkDetailsAPIView.as_view(), name='details-dailywork')

]
