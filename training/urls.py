from django.urls import path
from rest_framework import routers

from .views import (
    PresetTrainingSetViewSet
)


app_name = 'training'

router = routers.DefaultRouter()

router.register('preset-training-set', PresetTrainingSetViewSet, basename='preset_training_set')

urlpatterns=[
    
]
urlpatterns += router.urls
