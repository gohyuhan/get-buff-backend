from django.urls import path
from rest_framework import routers

from user.views import UserProfileViewSet

app_name = 'user'

router = routers.DefaultRouter()
router.register('user-profile', UserProfileViewSet, basename='user_profile')
urlpatterns=[

]
urlpatterns += router.urls
