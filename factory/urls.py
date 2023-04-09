from django.urls import path
from . import views

urlpatterns = [
    path('create-Sewmodel/', views.sewingModel_create, name='create-Sewmodel'),
    path('list-Sewmodel/', views.sewingModel_list, name='list-Sewmodel'),
    path('update-Sewmodel/', views.sewingModel_update, name='update-Sewmodel'),
    path('destroy-Sewmodel/', views.sewingModel_destroy, name='destroy-Sewmodel'),

]
