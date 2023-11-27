from decimal import Decimal

from rest_framework import serializers
from enumfields import EnumField

from .models import UserProfile


# fields 
class TargetStatusField(EnumField):
    def to_representation(self, instance):
        return instance.label


# serializer
class InitialUserProfileSerializer(serializers.ModelSerializer):
    # a serializer use only for user sign up view only
    # it was use in sign up page, there are also other field in request.data
    class Meta:
        model = UserProfile
        fields = [
            "gender",
            "weight_in_kg",
            "height_in_cm"
        ]
        extra_kwargs = {'allow_extra_fields': True}
    
    def validate_gender(self,value):
        return __validate_gender(value)

    def validate_weight_in_kg(self, value):
        return __validate_weight_in_kg(value)

    def validate_height_in_cm(self,value):
        return __validate_height_in_cm(value)


class UserProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')

    class Meta:
        model = UserProfile
        fields = (
            'first_name',
            'last_name',
            "gender",
            "weight_in_kg",
            "height_in_cm",
            "target_weight_in_kg",
            "weight_target_status"
        )
        read_only_fields = ("first_name", "last_name", "weight_target_status",)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['weight_target_status'] = instance.get_weight_target_status_display()
        return representation

    
    def validate_gender(self,value):
        return __validate_gender(value)
    
    def validate_weight_in_kg(self, value):
        return __validate_weight_in_kg(value)

    def validate_height_in_cm(self,value):
        return __validate_height_in_cm(value)
    
    def validate_target_weight_in_kg(self, value):
        return __validate_weight_in_kg(value)




def __validate_weight_in_kg(value):
         # return 170 if user enter anything other than integer/float
        if isinstance(value, int) or isinstance(value, float):
            decimal_value = Decimal(str(value))

            decimal_places = decimal_value.as_tuple().exponent

            if decimal_places >= -2 and value>0:
                return decimal_value
            elif decimal_places < -2 and value>0:
                return decimal_value.quantize(Decimal('0.00'))
            elif value<0:
                return 0.01
            else:
                return 499.99
        else:
            return 60

def __validate_height_in_cm(value):
    # return 170 if user enter anything other than integer
    if isinstance(value, int):
        if value<=0:
            return 1
        else:
            return 349
    return 170


def __validate_gender(value):
    if str(value) == "male":
        return str(value)
    elif str(value) == "female":
        return str(value)
    else:
        return "male"
        