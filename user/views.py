from datetime import datetime

from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import (
    UserProfile,
    TrainingSetting,
    TrainingSetCompletedRecord
)
from training.models import (
    CustomTrainingSet,
    CustomTrainingExercise
)
from .serializer import (
    UserProfileSerializer,
    TrainingSettingSerializer,
    TrainingSetHistorySerializer
)
from training.enums import TrainingStatus
from .services import (
    update_user_profile,
    update_user_training_setting,
    calories_calculator
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
            return Response({"success":True, "data":serializer.data}, status = status.HTTP_200_OK)
        return Response({"success":False, "error":"Invalid data format or type (Please ensure not negative value and the value is within range)"}, status = status.HTTP_400_BAD_REQUEST)


class UserTrainingSettingView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            training_setting = TrainingSetting.objects.get(user_profile__user=request.user)
            serializer = TrainingSettingSerializer(training_setting)
            return Response({"success":True, "data":serializer.data}, status=status.HTTP_200_OK)
        except TrainingSetting.DoesNotExist:
            user_profile = UserProfile.objects.filter(user=request.user)
            if(user_profile):
                training_setting = TrainingSetting.objects.create(user_profile=user_profile)
                serializer = TrainingSettingSerializer(training_setting)
                return Response({"success":True, "data":serializer.data}, status=status.HTTP_200_OK)
            return Response({"success":False, "error":"something's no right, please logout and login again"}, status=status.HTTP_400_BAD_REQUEST)


    def post(self,request):
        try:
            serializer= update_user_training_setting(request)
            if serializer:
                return Response({"success":True, "data":serializer.data}, status=status.HTTP_200_OK)
            return Response({"success":False, "error":"Invalid data format or type"},status=status.HTTP_400_BAD_REQUEST)
        except UserProfileError as e:
            return Response({"success":False, "error":str(e)},status=status.HTTP_400_BAD_REQUEST)
        

class TrainingSetHistoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Access query parameters
        date_param = request.query_params.get("date", None)

        # Check if the date parameter is provided
        if date_param:
            try:
                # Convert the date parameter to a datetime object
                date_obj = datetime.strptime(date_param, "%Y-%m-%d").date()
                
                # Filter model objects based on the date parameter
                queryset = CustomTrainingSet.objects.filter(
                    created__year=date_obj.year,
                    created__month=date_obj.month
                ).order_by("created")
                serializer = TrainingSetHistorySerializer(queryset, many=True)
                return Response({"success":True, "data":serializer.data}, status= status.HTTP_200_OK)
            except ValueError:
                # Handle invalid date format
                return Response({"success":False, "error": "Invalid date format. Please use YYYY-MM-DD."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            # Handle the case where no date parameter is provided
            return Response({"success":False, "error": "Date parameter is required."}, status=status.HTTP_400_BAD_REQUEST)
        

class CaloriesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            kg_gain_lost = request.GET.get("kg_gain_lost",0.5)
            calories = calories_calculator(request.user, kg_gain_lost)
            return Response({"success":True, "calories":calories}, status=status.HTTP_200_OK)
        except UserProfileError as e:
            return Response({"success":False, "error":str(e)}, status=status.HTTP_400_BAD_REQUEST)
        

class UserTrainingExerciseCompletedCount(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        completed_training_set_id = [
            completed.training_set.id for completed in
            TrainingSetCompletedRecord.objects.select_related(
                'training_set'
                ).filter(
                    user_profile__user = request.user
                )
        ]
        completed_training_set_count=len(completed_training_set_id )
        related_exercise = CustomTrainingExercise.objects.filter(belong_to_custom_training_set__id__in=completed_training_set_id, status=TrainingStatus.COMPLETED)
        exercise_count = len(related_exercise)
        return Response({"success":True, "data":{"training":completed_training_set_count, "exercise":exercise_count}}, status= status.HTTP_200_OK)