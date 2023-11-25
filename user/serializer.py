from decimal import Decimal

from rest_framework import serializers
from enumfields import EnumField

from .models import UserProfile
from .enums import TargetStatus



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

    def validate_weight_in_kg(self, value):
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

    def validate_height_in_cm(self,value):
        if value<=0:
            return 1
        else:
            return 349


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

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['weight_target_status'] = instance.get_weight_target_status_display()
        return representation
    
