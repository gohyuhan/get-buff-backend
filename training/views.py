from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.views import APIView

from training.serializer import (
    PresetTrainingSetSerializer,
    CustomTrainingSetSerializer
)
from training.models import (
    PresetTrainingSet, 
    CustomTrainingSet
)
from .services import (
    create_custom_preset_training_set, 
    create_custom_training_set,
    pause_training_set,
    conclude_training_set,
    give_up_training_set
)
from .exceptions import TrainingSetError
from user.exceptions import UserProfileError
from get_buff.permission import IsPostOnly, NoPutDeletePermission


"""
NOTE: we are not allowing update or delete request for any training related request
"""

# Create your views here.
class PresetTrainingSetViewSet(ReadOnlyModelViewSet):
    queryset = PresetTrainingSet.objects.all().order_by('id')
    serializer_class = PresetTrainingSetSerializer
    permission_classes = [AllowAny, NoPutDeletePermission]
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
            custom_training_set = create_custom_preset_training_set(request)
            data = CustomTrainingSetSerializer(custom_training_set).data
            return Response(data, status = status.HTTP_201_CREATED)
        except TrainingSetError as e:
            return Response({'message':str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except UserProfileError as e:
            return Response({'message':str(e)}, status=status.HTTP_400_BAD_REQUEST)


class CustomTrainingSetViewSet(ModelViewSet):
    """
    the endpoint for creating training assiociate to user profile based on user customization.
    This endpoint is only responsible for creation of customize training set, 
    for retrieve use CustomPresetTrainingViewSet endpoint, as the model are the same but the post request
    return data is in different structure
    """
    queryset = CustomTrainingSet.objects.all().order_by('-created')
    serializer_class = CustomTrainingSetSerializer
    permission_classes = [IsAuthenticated, IsPostOnly]

    def create(self, request, *args, **kwargs):
        try:
            custom_training_set = create_custom_training_set(request)
            data = CustomTrainingSetSerializer(custom_training_set).data
            return Response(data, status = status.HTTP_201_CREATED)
        except TrainingSetError as e:
            return Response({'message':str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except UserProfileError as e:
            return Response({'message':str(e)}, status=status.HTTP_400_BAD_REQUEST)
        

class TrainingSetPauseView(APIView):
    """
    endpoint for saving the progress of a training set that is completed yet, the training is put to a hold
    """
    permission_classes = [IsAuthenticated, IsPostOnly]

    def post(self, request, *args, **kwargs):
        try:
            pause_training_set(request)
            return Response(status = status.HTTP_200_OK)
        except:
            return Response(status = status.HTTP_400_BAD_REQUEST)


class TrainingSetConcludeView(APIView):
    """
    endpoint for concluding a training set,
    NOTE: the badges progress conclude should also be include in this endpoint in the future
    """
    permission_classes = [IsAuthenticated, IsPostOnly]

    def post(self, request, *args, **kwargs):
        try:
            conclude_training_set(request)
            return Response(status = status.HTTP_200_OK)
        except:
            return Response(status = status.HTTP_400_BAD_REQUEST)
    

class TrainingSetGiveUpView(APIView):
    """
    endpoint for giving up a training set
    """
    permission_classes = [IsAuthenticated, IsPostOnly]

    def post(self, request, *args, **kwargs):
        try:
            give_up_training_set(request)
            return Response(status = status.HTTP_200_OK)
        except:
            return Response(status = status.HTTP_400_BAD_REQUEST)
