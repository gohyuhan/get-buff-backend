from django.urls import path
from rest_framework import routers

from .views import (
    PresetTrainingSetViewSet,
    CustomPresetTrainingSetViewSet,
    CustomTrainingSetViewSet,
    TrainingSetPauseView,
    TrainingSetConcludeView,
    TrainingSetGiveUpView,
    ExerciseViewSet,
    OngoingTrainingSetView
)


app_name = 'training'

router = routers.DefaultRouter()

router.register('exercise', ExerciseViewSet, basename='exercise')
router.register('preset-training-set', PresetTrainingSetViewSet, basename='preset_training_set')
router.register('custom-preset-training-set', CustomPresetTrainingSetViewSet, basename='custom_preset_training_set')
router.register('custom-training-set', CustomTrainingSetViewSet, basename='custom_training_set')

urlpatterns=[
    path('training-pause', TrainingSetPauseView.as_view(), name='training_pause'),
    path('training-conclude', TrainingSetConcludeView.as_view(), name='training_conclude'),
    path('training-give-up', TrainingSetGiveUpView.as_view(), name='training_give_up'),
    path('training-on-going', OngoingTrainingSetView.as_view(), name='training_on_going'),
]
urlpatterns += router.urls
