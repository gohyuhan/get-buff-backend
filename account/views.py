from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.conf import settings
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import SetPasswordForm

from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from .serializer import (
    UserSerializer, 
    UserSignUpSerializer,
    ChangePasswordSerializer,
    UserLoginSerializer
)
from .services import sign_out_user
from .models import User, SecurityToken
from .enums import AccountEmailStatus,SecurityTokenEventType
from user.models import UserProfile, TrainingSetting
from get_buff.permission import IsPostOnly, IsGetOnly
from badges.services import user_achivement_badge_create
from notifications.services import send_notification_email
from notifications.models import Event


# Create your views here.
class UserCreateView(APIView):
    permission_classes = [AllowAny, IsPostOnly]
    authentication_classes=[]

    def post(self, request):
        serializer = UserSignUpSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = User.objects.create_user(
                    email=serializer.data['email'],
                    password=serializer.data['password'],
                    first_name=serializer.data['first_name'],
                    last_name=serializer.data['last_name'],
                    gender=serializer.data['gender'],
                    weight=serializer.data['weight_in_kg'],
                    height=serializer.data['height_in_cm'],
                    target_weight=serializer.data['weight_in_kg']
                )   
                if user:
                    token = Token.objects.create(user=user)
                    user_profile = UserProfile.objects.filter(user=user)
                    user_achivement_badge_create(user_profile = user_profile.first())
                return Response({'success':True, 'token':token.key}, status=status.HTTP_201_CREATED)
            except ValueError as e:
                return Response({'success':False, 'error':{'non_field_errors':[str(e)]}}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'success':False, 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    

class UserCheckView(APIView):
    """
    To check user token is valid, else we return an error so frontend client can prompt user to login again
    """
    permission_classes = [IsAuthenticated, IsGetOnly]

    def get(self, request):
        if request.user:
            if not UserProfile.objects.filter(user=request.user).exists():
                user_profile = UserProfile.objects.create(user=request.user)
            user_profile = UserProfile.objects.get(user=request.user)
            if not TrainingSetting.objects.filter(user_profile__user=request.user).exists():
                TrainingSetting.objects.create(user_profile=user_profile)
            user_achivement_badge_create(user_profile = user_profile)
            return Response({'success':True}, status=status.HTTP_200_OK)


class ObtainAuthTokenView(ObtainAuthToken):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            try:
                UserProfile.objects.get(user=user)
            except UserProfile.DoesNotFound:
                UserProfile.objects.create(user=user)
            print(token.key)
            return Response({'success': True, 'token': token.key}, status = status.HTTP_200_OK)
        return Response({'success': False, 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request):
        serializer = ChangePasswordSerializer(
            data = request.data, user = request.user
        )
        if serializer.is_valid():
            request.user.set_password(serializer.data['new_password'])
            request.user.save()
            return Response({'success':True}, status=status.HTTP_200_OK)
        return Response({'success':False, 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        resp = sign_out_user(request.user)
        if resp:
            return Response(
                {
                    "message":'Successfully Logout',
                    "success": True
                }, 
                status=status.HTTP_200_OK
            ) 
        

class PasswordResetRequestView(APIView):
    permission_classes = [AllowAny]
    authentication_classes=[]

    def get(self, request):
        user= User.objects.filter(
            email= request.GET.get('email')
        ).first()
        if user:
            if SecurityToken.objects.filter(event = SecurityTokenEventType.PASSWORD_RESET, user=user).exists():
                SecurityToken.objects.filter(event = SecurityTokenEventType.PASSWORD_RESET, user=user).update(
                    is_valid=False
                )
            token = SecurityToken.objects.create(event = SecurityTokenEventType.PASSWORD_RESET, user=user)
            password_reset_event, created = Event.objects.get_or_create(
                name = "password reset",
                desp = "Event that to send email for password reset",
                subject = "Reset Password"
            )
            link = settings.HOST_DOMAIN+reverse("reset_password")+f"?token={token.token}"
            send_notification_email(
                "email/password_reset_email.html", 
                {'name':f'{user.first_name} {user.last_name}', 'account':f'{request.GET.get("email")}' ,'link':link},
                password_reset_event,
                user
            )
            return Response({'success':True, "data":'please check email to continue password reset'}, status=status.HTTP_200_OK)
        return Response({'success':False, "data":f'No User associate with email: {request.GET.get("email")}'}, status=status.HTTP_400_BAD_REQUEST)


# SSR (Server Side Rendering) Views
class VerifyEmailView(TemplateView):
    template_name = 'account/email_verification.html'

    def get(self, request):
        retrieved_token = SecurityToken.objects.filter(
            token = request.GET.get('token')
        ).first()
        context = {
            'success':False,
            'is_verified':False
        }
        if retrieved_token:
            if retrieved_token.is_token_valid() and retrieved_token.event == SecurityTokenEventType.EMAIL_VERIFICATION:
                retrieved_token.deactivate()
                retrieved_token.user.activate()
                context['success'] = True
            elif retrieved_token.user.email_status == AccountEmailStatus.ACTIVE:
                context['is_verified'] = True

        return self.render_to_response(self.get_context_data(**context))
    

class PasswordResetView(FormView):
    template_name = 'account/reset_password.html'
    form_class = SetPasswordForm
    security_token = None

    def dispatch(self, request, *args, **kwargs ):
        token = request.GET.get('token')
        if token:
            security_token = get_object_or_404(SecurityToken, token=token, event = SecurityTokenEventType.PASSWORD_RESET)
            if not security_token.is_token_valid():
                return HttpResponseRedirect(self.request.path+'?status=invalid_token')
            self.security_token = security_token
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(PasswordResetView, self).get_context_data()
        context['label_suffix'] = ""
        context['status'] = self.request.GET.get('status')
        return context
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = None

        return kwargs
    
    def get(self,request, *args, **kwargs):
        if not self.security_token and not self.request.GET.get('status'):
            return HttpResponseRedirect(self.request.path+'?status=invalid_token')
        return super().get(request, *args, **kwargs)
    
    def form_valid(self,form):
        self.security_token.deactivate()
        user = self.security_token.user
        user.set_password(form.cleaned_data['new_password1'])
        user.save()
        return HttpResponseRedirect(self.request.path+'?status=success')

