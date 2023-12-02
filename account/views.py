from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from .serializer import (
    UserSerializer, 
    UserSignUpSerializer,
    ChangePasswordSerializer,
    UserLoginSerializer
)
from .services import sign_out_user
from .models import User
from user.models import UserProfile
from get_buff.permission import IsPostOnly


# Create your views here.
class UserCreateViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny, IsPostOnly]
    authentication_classes=[]

    def create(self, request):
        serializer = UserSignUpSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create_user(
                email=serializer.data['email'],
                password=serializer.data['password'],
                first_name=serializer.data['first_name'],
                last_name=serializer.data['last_name'],
            )
            if user:
                token = Token.objects.create(user=user)
                user_profile = UserProfile.objects.filter(user=user)
                user_profile.update(
                    gender=serializer.data['gender'],
                    weight_in_kg=serializer.data['weight_in_kg'],
                    height_in_cm=serializer.data['height_in_cm'],
                    target_weight_in_kg=serializer.data['weight_in_kg']
                )
            return Response({'success':True, 'token':token.key}, status=status.HTTP_201_CREATED)
        return Response({'success':False, 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class ObtainAuthTokenView(ObtainAuthToken):
    permission_classes = [AllowAny]
    authentication_classes=[]

    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            try:
                UserProfile.objects.get(user=user)
            except UserProfile.DoesNotFound:
                UserProfile.objects.create(user=user)
            return Response({'success': True, 'token': token.key}, status = status.HTTP_200_OK)
        return Response({'success': False, 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordvView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request):
        serializer = ChangePasswordSerializer(
            data = request.data, user = request.user
        )
        if serializer.is_valid():
            request.user.set_password(serializer.data['new_password'])
            request.user.save()
            return Response({'success':True}, status=status.HTTP_200_OK)
        return Response({'success':False, 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        resp = sign_out_user(request.user)
        if resp:
            return Response(
                {
                    "message":'Successfully Logout',
                    "success": True
                }, 
                status=status.HTTP_200_OK
            ) 
