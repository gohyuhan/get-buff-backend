from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
import importlib


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(
        self, 
        email, 
        password, 
        first_name, 
        last_name, 
        **extra_fields
    ):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(
            email=email, 
            first_name=first_name, 
            last_name=last_name,
            **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        # create assiociate user profile
        # default gender is male, other will be left as blank 
        user_models = importlib.import_module("user.models")
        user_profile = getattr(
            user_models, "UserProfile"
        )
        training_setting = getattr(
            user_models, "TrainingSetting"
        )
        if user_profile and training_setting:
            user_prof = user_profile.objects.create(
                user=user,
                gender = "male",
            )
            training_setting.objects.create(
                user_profile=user_prof
            )

        return user

    def create_superuser(
        self,
        email,
        password,
        first_name,
        last_name,
        **extra_fields
    ):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password,first_name,last_name, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email
