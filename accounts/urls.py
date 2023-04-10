from django.urls import path
from rest_framework.routers import SimpleRouter

from accounts.views import UserViewSet, UserMeAPIView

router = SimpleRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('users/me/', UserMeAPIView.as_view(), name='me'),
]
urlpatterns += router.urls