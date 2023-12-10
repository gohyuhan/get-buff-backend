from rest_framework.authtoken.models import Token


def get_user(request):
    user = request.user
    if user.is_anonymous:
        return False
    return user


def sign_out_user(user):
    if user:
        try:
            Token.objects.get(user=user)
            return True
        except Token.DoesNotExist:
            return False
    return False
