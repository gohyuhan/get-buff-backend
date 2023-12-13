import importlib
from datetime import timedelta

from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models, transaction
from django.utils.crypto import get_random_string
from django.utils import timezone

from enumfields import EnumField

from .enums import AccountEmailStatus,SecurityTokenEventType


# Create your models here.

class UserManager(BaseUserManager):
    def create_user(
        self, 
        email, 
        password, 
        first_name, 
        last_name, 
        gender, 
        weight,
        height, 
        target_weight,
        **extra_fields
    ):
        if not email:
            raise ValueError('The Email field must be set')
        try:
            with transaction.atomic():
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
                user_prof = user_profile.objects.create(
                    user=user,
                    gender=gender,
                    weight_in_kg=weight,
                    height_in_cm=height,
                    target_weight_in_kg=target_weight
                )
                training_setting.objects.create(
                    user_profile=user_prof
                )
                send_verification_email(user)
                return user
        except Exception:
            raise ValueError('please check all value to see if they are valid (Especially weight and height)')

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
        gender = 'male'
        weight = 60
        height = 170
        target_weight = 60
        return self.create_user(
            email, 
            password,
            first_name,
            last_name, 
            gender, 
            weight,
            height, 
            target_weight,
            **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    email_verified_date = models.DateTimeField(null=True, blank=True)
    email_status = EnumField(AccountEmailStatus, max_length=3, default = AccountEmailStatus.DISABLED)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email
    
    def activate(self):
        self.email_verified_date =timezone.now()
        self.email_status = AccountEmailStatus.ACTIVE
        self.save()
    
    def verification_pending(self):
        self.email_status = AccountEmailStatus.PENDING
        self.save()


def get_random_token():
    return SecurityToken.generate_token()


class SecurityToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=20, db_index=True, default = get_random_token)
    event = EnumField(SecurityTokenEventType,max_length=3,default =SecurityTokenEventType.NONE)
    created_date = models.DateTimeField(auto_now_add=True)
    is_valid = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.token} - {self.is_valid}"
    
    def deactivate(self):
        self.is_valid = False
        self.save()

    def is_token_valid(self):
        result = False
        start_date = timezone.now() - timedelta(days=1)
        end_date = timezone.now() 
        if self.is_valid and start_date<=self.created_date<=end_date:
            result = True
        return result
    
    @staticmethod
    def generate_token():
        token  = get_random_string(length = 20)
        while SecurityToken.objects.filter(token = token).exists():
            token = get_random_string(length=20)
        return token
    

def send_verification_email(user):
    # test send mail
    from notifications.services import send_notification_email
    from notifications.models import Event
    email_verification_event, created = Event.objects.get_or_create(
        name = "email verification",
        desp = "Event that verify user email account",
        subject = "Email Verification"
    )
    token = SecurityToken.objects.create(event = SecurityTokenEventType.EMAIL_VERIFICATION, user=user)
    link = settings.HOST_DOMAIN+reverse("verify_email")+f"?token={token.token}"
    user.verification_pending()
    send_notification_email(
        "email/verify_email.html", 
        {'name':f'{user.first_name} {user.last_name}', 'link':link},
        email_verification_event,
        user
    )
