from django.urls import path
from rest_framework import routers

from user.views import (
    UserProfileViewSet,
    UserTrainingSettingView,
    TrainingSetHistoryView,
    CaloriesView
)

app_name = 'user'

router = routers.DefaultRouter()
router.register('user-profile', UserProfileViewSet, basename='user_profile')

urlpatterns=[
    path('training-setting', UserTrainingSettingView.as_view(), name="training_setting"),
    path('training-record', TrainingSetHistoryView.as_view(), name='training_history'),
    path('calories', CaloriesView.as_view(), name='calories')
]

urlpatterns += router.urls
