from django.urls import path
from rest_framework import routers

from .views import (
    PresetTrainingSetViewSet,
    CustomPresetTrainingSetViewSet,
    CustomTrainingSetViewSet
)


app_name = 'training'

router = routers.DefaultRouter()

router.register('preset-training-set', PresetTrainingSetViewSet, basename='preset_training_set')
router.register('custom-preset-training-set', CustomPresetTrainingSetViewSet, basename='custom_preset_training_set')
router.register('custom-training-set', CustomTrainingSetViewSet, basename='custom_training_set')

urlpatterns=[
    
]
urlpatterns += router.urls
