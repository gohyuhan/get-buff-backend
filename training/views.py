from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.views import APIView

from constance import config

from training.serializer import (
    PresetTrainingSetSerializer,
    CustomTrainingSetSerializer,
    ExerciseSerializer
)
from training.models import (
    PresetTrainingSet, 
    CustomTrainingSet,
    Exercise
)
from .services import (
    create_custom_preset_training_set, 
    create_custom_training_set,
    pause_training_set,
    conclude_training_set,
    give_up_training_set,
    ongoing_training_or_exercise
)
from .exceptions import (
    TrainingSetError,
    TrainingExerciseError 
)
from user.exceptions import UserProfileError
from get_buff.permission import (
    IsPostOnly, 
    NoPutDeletePermission,
    IsGetOnly
)
from get_buff.pagination import CustomPagination
from .enums import TrainingStatus
from badges.services import user_training_achivement_badge_progression_update
from badges.serializer import UserAchivementBadgeSerializer


"""
NOTE: we are not allowing update or delete request for any training related request
"""

# Create your views here.
class  ExerciseViewSet(ReadOnlyModelViewSet):
    queryset = Exercise.objects.all().order_by('name')
    permission_classes=[AllowAny, IsGetOnly]
    authentication_classes=[]
    pagination_class = CustomPagination
    serializer_class = ExerciseSerializer


class PresetTrainingSetViewSet(ReadOnlyModelViewSet):
    queryset = PresetTrainingSet.objects.all().order_by('id')
    serializer_class = PresetTrainingSetSerializer
    permission_classes = [AllowAny, IsGetOnly]
    authentication_classes = []


class CustomPresetTrainingSetViewSet(ModelViewSet):
    """
    the endpoint for creating training assiociate to user profile based on preset.
    for pure customize training set, it will be on other endpoint
    """
    queryset = CustomTrainingSet.objects.all().order_by('-created')
    serializer_class = CustomTrainingSetSerializer
    permission_classes = [IsAuthenticated, NoPutDeletePermission]

    def get_queryset(self):
        return super().get_queryset().filter(
            user_profile__user = self.request.user
        )

    def create(self, request, *args, **kwargs):
        try:
            if ongoing_training_or_exercise(request.user):
                return Response({'success':False, 'error':'Ongoing Training Detected, Please Finish or Give Up The Exercise Before Creating A New One'}, status = status.HTTP_400_BAD_REQUEST)
            else:
                custom_training_set = create_custom_preset_training_set(request)
                data = CustomTrainingSetSerializer(custom_training_set).data
                return Response({'success':True, 'data':data}, status = status.HTTP_201_CREATED)
        except TrainingSetError as e:
            return Response({'success':False, 'error':str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except UserProfileError as e:
            return Response({'success':False, 'error':str(e)}, status=status.HTTP_400_BAD_REQUEST)


class CustomTrainingSetViewSet(ModelViewSet):
    """
    NOTE:the endpoint for creating training assiociate to user profile based on user customization.
    This endpoint is only responsible for creation of customize training set, 
    for retrieve use CustomPresetTrainingViewSet endpoint, as the model are the same but the post request
    return data is in different structure

    NOTE: IMPORTANT 2023/12/05 - GOH YU HAN
    This endpoint will not be used in current version of application. 
    It will be available for future release when we integrate relevant function for custom training set
    in frontend
    """
    queryset = CustomTrainingSet.objects.all().order_by('-created')
    serializer_class = CustomTrainingSetSerializer
    permission_classes = [IsAuthenticated, IsPostOnly]

    def create(self, request, *args, **kwargs):
        try:
            if ongoing_training_or_exercise(request.user):
                return Response({'success':False, 'error':'Ongoing Training Detected, Please Finish or Give Up The Exercise Before Creating A New One'}, status = status.HTTP_400_BAD_REQUEST)
            else:
                custom_training_set = create_custom_training_set(request)
                data = CustomTrainingSetSerializer(custom_training_set).data
                return Response(data, status = status.HTTP_201_CREATED)
        except TrainingSetError as e:
            return Response({'success':False, 'error':str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except TrainingExerciseError as e:
            return Response({'success':False, 'error':str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except UserProfileError as e:
            return Response({'success':False, 'error':str(e)}, status=status.HTTP_400_BAD_REQUEST)
        

class TrainingSetPauseView(APIView):
    """
    endpoint for saving the progress of a training set that is completed yet, the training is put to a hold
    """
    permission_classes = [IsAuthenticated, IsPostOnly]

    def post(self, request, *args, **kwargs):
        try:
            pause_training_set(request)
            return Response({'success':True}, status = status.HTTP_200_OK)
        except:
            return Response({'success':False}, status = status.HTTP_400_BAD_REQUEST)


class TrainingSetConcludeView(APIView):
    """
    endpoint for concluding a training set,
    NOTE: the badges progress conclude should also be include in this endpoint in the future
    """
    permission_classes = [IsAuthenticated, IsPostOnly]

    def post(self, request, *args, **kwargs):
        try:
            user_profile,training_set = conclude_training_set(request)
            obtained_badge = user_training_achivement_badge_progression_update(user_profile, training_set) 
            if obtained_badge:
                serializer = UserAchivementBadgeSerializer(obtained_badge, many = True)
                return Response({'success':True, 'badges':serializer.data}, status = status.HTTP_200_OK)
            return Response({'success':True, 'badges':[]}, status = status.HTTP_200_OK)
        except:
             return Response({'success':False}, status = status.HTTP_400_BAD_REQUEST)
    

class TrainingSetGiveUpView(APIView):
    """
    endpoint for giving up a training set
    """
    permission_classes = [IsAuthenticated, IsPostOnly]

    def post(self, request, *args, **kwargs):
        try:
            give_up_training_set(request)
            return Response({'success':True}, status = status.HTTP_200_OK)
        except:
             return Response({'success':False}, status = status.HTTP_400_BAD_REQUEST)


class OngoingTrainingSetView(APIView):
    """
    endpoint for retrieving ongoing training set
    Have Ongoing - return Success : True
    Not Have Ongoing - return Failure : False
    NOTE: both return status code 200
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        if ongoing_training_or_exercise(request.user):
            ongoing_custom_training_set = CustomTrainingSet.objects.filter(
                user_profile__user = request.user, 
                status = TrainingStatus.ONGOING
            ).first()
            data = CustomTrainingSetSerializer(ongoing_custom_training_set).data
            return Response({'success':True, 'data':data}, status = status.HTTP_200_OK)
        else:
            return Response({'success':False}, status = status.HTTP_200_OK)
        

class TrainingRestTimeView(APIView):
    """
    Retrieve rest time for anonymous users.
    Login user will use the rest time associate with their profile
    """
    permission_classes = [AllowAny]
    authentication_classes = []

    def get(self, request, *args, **kwargs):
        return Response({'success':True, 'data':config.TRAINING_DEFAULT_REST_TIME}, status = status.HTTP_200_OK)