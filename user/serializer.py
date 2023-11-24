from decimal import Decimal

from rest_framework import serializers

from .models import UserProfile


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
