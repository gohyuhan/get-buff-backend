from django.urls import path
from rest_framework import routers

from .views import (
    UserCreateView, 
    ObtainAuthTokenView, 
    LogoutView,
    ChangePasswordvView
)


app_name = 'account'

router = routers.DefaultRouter()

urlpatterns=[
    path('user-sign-up', UserCreateView.as_view(), name='user_sign_up'),
    path('user-login', ObtainAuthTokenView.as_view(), name='user_login'),
    path('user-logout', LogoutView.as_view(), name='user_logout'),
    path('change-password', ChangePasswordvView.as_view(), name='change_password')
]
urlpatterns += router.urls
