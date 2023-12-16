from django.urls import path
from rest_framework import routers

from .views import (
    UserAchivementBadgeView
)


app_name = 'badges'

router = routers.DefaultRouter()

urlpatterns=[
    path('user-badge', UserAchivementBadgeView.as_view(), name='user_badge'),
]
urlpatterns += router.urls