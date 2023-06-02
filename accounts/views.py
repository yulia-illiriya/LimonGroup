from django.utils.decorators import method_decorator

from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from djoser.views import UserViewSet as DjoserUserViewSet

from drf_yasg.utils import swagger_auto_schema

from accounts.models import User
from .serializers import UserAPISerializer, UserCreateAPISerializer


from djoser import views as djoser_views
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})


class UserCreateView(DjoserUserViewSet):
    """
    Custom view for user registration using Djoser.
    """
    serializer_class = UserCreateAPISerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        user = serializer.instance

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserMeAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserAPISerializer

    @swagger_auto_schema(tags=['users'])
    def retrieve(self, request):
        if not request.user.is_authenticated:
            return Response(data='Not authenticated', status=status.HTTP_401_UNAUTHORIZED)

        user = self.get_serializer(request.user).data
        return Response(data=user)

class TestMeAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(tags=['users'], manual_parameters=[
        openapi.Parameter('Authorization', openapi.IN_HEADER, type=openapi.TYPE_STRING, description='Token'),
    ])
    def get(self, request):
        if not request.user.is_authenticated:
            return Response(data='Not authenticated', status=status.HTTP_401_UNAUTHORIZED)

        user = request.user
        serializer = UserAPISerializer(user)
        return Response(serializer.data)