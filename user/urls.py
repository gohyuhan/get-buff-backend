from django.urls import path
from rest_framework import routers

from user.views import (
    UserProfileViewSet,
    UserTrainingSettingView
)

app_name = 'user'

router = routers.DefaultRouter()
router.register('user-profile', UserProfileViewSet, basename='user_profile')

urlpatterns=[
    path('training-setting', UserTrainingSettingView.as_view(), name="training_setting")
]

urlpatterns += router.urls
