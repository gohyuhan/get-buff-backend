from django.core.exceptions import ObjectDoesNotExist

from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed

from user.models import UserProfile


class CustomTokenAuthentication(TokenAuthentication):
    def authenticate(self, request):
        credentials = super().authenticate(request)
        if credentials is None:
            raise AuthenticationFailed("Authentication Token Not Provided")
        user, token = credentials
        if user and not UserProfile.objects.filter(user=user).exists:
            # create user profile if not exist during login
            UserProfile.objects.create(
                user=user,
                gender = "male",
            )
        return user, token