from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from training.serializer import (
    PresetTrainingSetSerializer,
    CustomTrainingSetSerializer
)
from training.models import (
    PresetTrainingSet, 
    CustomTrainingSet
)
from .services import create_custom_preset_training_set
from .exceptions import TrainingSetError


# Create your views here.
class PresetTrainingSetViewSet(ReadOnlyModelViewSet):
    queryset = PresetTrainingSet.objects.all().order_by('id')
    serializer_class = PresetTrainingSetSerializer
    permission_classes = [AllowAny]
    authentication_classes = []


class CustomPresetTrainingSetViewSet(ModelViewSet):
    """
    the endpoint for creating training assiociate to user profile based on preset.
    for pure customize training set, it will be on other endpoint
    """
    queryset = CustomTrainingSet.objects.all().order_by('-created')
    serializer_class = CustomTrainingSetSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        try:
            custom_training_set = create_custom_preset_training_set(request)
            data = CustomTrainingSetSerializer(custom_training_set).data
            return Response(data, status = status.HTTP_201_CREATED)
        except TrainingSetError as e:
            return Response({'message':str(e)}, status=status.HTTP_400_BAD_REQUEST)



