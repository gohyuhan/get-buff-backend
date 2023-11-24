from factory.django import DjangoModelFactory

from account.models import User


class UserModelFactory(DjangoModelFactory):
    class Meta:
        model = User
