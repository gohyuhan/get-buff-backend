from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import (
    UserProfile,
    TrainingSetCompletedRecord,
    TrainingSetting
)
from .serializer import (
    UserProfileSerializer,
    TrainingSettingSerializer
)
from .services import (
    update_user_profile,
    update_user_training_setting
)
from .exceptions import UserProfileError


# Create your views here.
class UserProfileViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().filter(
            user = self.request.user
        )
    
    def create(self,request):
        updated = update_user_profile(request)
        if updated:
            user_profile = UserProfile.objects.get(user=request.user)
            serializer = UserProfileSerializer(user_profile, many=False)
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response({"message":"Invalid data format or type"}, status = status.HTTP_400_BAD_REQUEST)
    

class UserTrainingSettingView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            training_setting = TrainingSetting.objects.get(user_profile__user=request.user)
            serializer = TrainingSettingSerializer(training_setting)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except TrainingSetting.DoesNotExist:
            user_profile = UserProfile.objects.filter(user=request.user)
            if(user_profile):
                training_setting = TrainingSetting.objects.create(user_profile=user_profile)
                serializer = TrainingSettingSerializer(training_setting)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({"message":"something's no right, please logout and login again"}, status=status.HTTP_400_BAD_REQUEST)


    def post(self,request):
        try:
            serializer= update_user_training_setting(request)
            if serializer:
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({"message":"Invalid data format or type"},status=status.HTTP_400_BAD_REQUEST)
        except UserProfileError as e:
            return Response({"message":str(e)},status=status.HTTP_400_BAD_REQUEST)