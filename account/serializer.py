from decimal import Decimal

from django.contrib.auth.password_validation import (
    validate_password as validate_password_auth
)

from rest_framework import serializers

from .models import User
from .validators import OldPasswordvalidator, PasswordStrengthValidator, UserPasswordvalidator


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name"]


class UserSignUpSerializer(serializers.Serializer):
    # it was use in sign up page, there are also other field in request.data
    email = serializers.EmailField(required=True)
    password = serializers.CharField(style={"input_type": "password"},required=True)
    first_name = serializers.CharField(max_length=50,required=True)
    last_name = serializers.CharField(max_length=50,required=True)
    gender = serializers.CharField(required=True)
    weight_in_kg = serializers.DecimalField(max_digits=5, decimal_places=2,required=True)
    height_in_cm = serializers.IntegerField(required=True)

    def validate_email(self, email):
        if User.objects.filter(email__iexact=email).exists():
            raise serializers.ValidationError("user already exists")
        return email

    def validate_password(self, password):
        validate_password_auth(
            password,
            password_validators = [PasswordStrengthValidator]
        )
        return password
    
    def validate_gender(self,gender):
        return _gender_validate(gender)

    def validate_weight_in_kg(self, weight_in_kg):
        return _weight_in_kg_validate(weight_in_kg)

    def validate_height_in_cm(self,height_in_cm):
        return _height_in_cm_validate(height_in_cm)


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={"input_type": "password"})

    def validate(self, data):
        try:
            self.user = User.objects.get(email__iexact=data['email'])
            validate_password_auth(
                data['password'],
                user=self.user,
                password_validators=[UserPasswordvalidator]
            )
            data['user']=self.user
            return data
        except User.DoesNotExist:
            raise serializers.ValidationError('Invalid user or password')
        except User.MultipleObjectsReturned:
            raise serializers.ValidationError('Multiple users were selected')


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField()
    new_password = serializers.CharField()

    def __init__(self,*args, **kwargs):
        self.user = kwargs.pop('user',None)
        super(ChangePasswordSerializer, self).__init__(*args, **kwargs)
    
    def validate_old_password(self, old_password):
        validate_password_auth(
            old_password,
            user = self.user,
            password_validators = [OldPasswordvalidator]
        )
        return old_password

    def validate_new_password(self, new_password):
        validate_password_auth(
            new_password,
            password_validators = [PasswordStrengthValidator]
        )
        return new_password
    

def _weight_in_kg_validate(value):
    decimal_value = Decimal(str(value))

    decimal_places = decimal_value.as_tuple().exponent

    if decimal_places >= -2 and value>0 and value<=500:
        return decimal_value
    elif decimal_places < -2 and value>0 and value <=500:
        return decimal_value.quantize(Decimal('0.00'))
    elif value<1 or value>500:
        return 60


def _height_in_cm_validate(value):
    # return 170 if user enter anything <0 or >350
    if value<50 or value>350:
        return 170
    return value


def _gender_validate(value):
    if str(value) == "male":
        return str(value)
    elif str(value) == "female":
        return str(value)
    else:
        return "male"