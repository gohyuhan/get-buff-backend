from django.urls import path
from rest_framework import routers

from .views import (
    UserCreateView, 
    ObtainAuthTokenView, 
    LogoutView,
    ChangePasswordView,
    PasswordResetRequestView,
    UserCheckView
)


app_name = 'account'

router = routers.DefaultRouter()

urlpatterns=[
    path('check', UserCheckView.as_view(), name='check'),
    path('user-sign-up', UserCreateView.as_view(), name='user_sign_up'),
    path('user-login', ObtainAuthTokenView.as_view(), name='user_login'),
    path('user-logout', LogoutView.as_view(), name='user_logout'),
    path('change-password', ChangePasswordView.as_view(), name='change_password'),
    path('password-reset', PasswordResetRequestView.as_view(), name='password-reset')
]
urlpatterns += router.urls
