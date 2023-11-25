from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from training.models import PresetTrainingSet
from training.serializer import PresetTrainingSetSerializer
# Create your views here.


class PresetTrainingSetViewSet(ReadOnlyModelViewSet):
    queryset = PresetTrainingSet.objects.all().order_by('id')
    serializer_class = PresetTrainingSetSerializer
    permission_classes = [AllowAny]
    authentication_classes = []