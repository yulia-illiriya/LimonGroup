from django.utils.decorators import method_decorator

from rest_framework.response import Response
from rest_framework.views import ModelViewSet
from rest_framework.generics import RetrieveAPIView
from rest_framework import status

from drf_yasg.utils import swagger_auto_schema

from accounts.models import User
from accounts.serializers import UserSerializer


@method_decorator(name='list', decorator=swagger_auto_schema(tags=['users']))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(tags=['users']))
@method_decorator(name='create', decorator=swagger_auto_schema(tags=['users']))
@method_decorator(name='update', decorator=swagger_auto_schema(tags=['users']))
@method_decorator(name='destroy', decorator=swagger_auto_schema(tags=['users']))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(tags=['users']))
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserMeAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @swagger_auto_schema(tags=['users'])
    def retrieve(self, request):
        if not request.user.is_authenticated:
            return Response(data='Not authenticated', status=status.HTTP_401_UNAUTHORIZED)

        user = self.get_serializer(request.user).data
        return Response(data=user)
