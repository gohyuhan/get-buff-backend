from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from .serializer import UserSerializer, UserAuthSerializer
from .services import sign_out_user
from .models import User
from user.models import UserProfile
from user.serializer import InitialUserProfileSerializer
from get_buff.permission import IsPostOnly


# Create your views here.
class UserCreateViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny, IsPostOnly]
    authentication_classes=[]

    def create(self, request):
        serializer = UserAuthSerializer(data=request.data)
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
                serializer = InitialUserProfileSerializer(data=request.data)
                if serializer.is_valid():
                    user_profile.update(
                        gender=serializer.data['gender'],
                        weight_in_kg=serializer.data['weight_in_kg'],
                        height_in_cm=serializer.data['height_in_cm'],
                        target_weight_in_kg=serializer.data['weight_in_kg']
                    )
            return Response(token.key, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ObtainAuthTokenView(ObtainAuthToken):
    permission_classes = [AllowAny]
    authentication_classes=[]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        try:
            UserProfile.objects.get(user=user)
        except UserProfile.DoesNotFound:
            UserProfile.objects.create(user=user)
        return Response({'token': token.key})


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
