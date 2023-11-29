from decimal import Decimal

from rest_framework import serializers

from .models import (
    UserProfile,
    TrainingSetting
)
from training.models import (
    CustomTrainingSet
)


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
    if value<1 or value>350:
        return 170
    return value


def _gender_validate(value):
    if str(value) == "male":
        return str(value)
    elif str(value) == "female":
        return str(value)
    else:
        return "male"
        


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
        return _gender_validate(value)

    def validate_weight_in_kg(self, value):
        return _weight_in_kg_validate(value)

    def validate_height_in_cm(self,value):
        return _height_in_cm_validate(value)


class UserProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source="user.first_name", read_only=True)
    last_name = serializers.CharField(source="user.last_name",read_only=True)

    class Meta:
        model = UserProfile
        fields = (
            "first_name",
            "last_name",
            "uuid",
            "gender",
            "weight_in_kg",
            "height_in_cm",
            "target_weight_in_kg",
            "weight_target_status"
        )
        read_only_fields = ("first_name", "last_name", "uuid","weight_target_status",)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        try:
            representation['weight_target_status'] = instance.get_weight_target_status_display()
        except:
            pass
        return representation

    def validate_gender(self,value):
        return _gender_validate(value)
    
    def validate_weight_in_kg(self, value):
        return _weight_in_kg_validate(value)

    def validate_height_in_cm(self,value):
        return _height_in_cm_validate(value)
    
    def validate_target_weight_in_kg(self, value):
        return _weight_in_kg_validate(value)


class TrainingSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingSetting
        fields=("rest_time",)

    def validate_rest_time(self, value):
        if value<5 or value>120:
            return 25
        return value
    

class TrainingSetHistorySerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = CustomTrainingSet
        fields = ('name', 'image_url', 'status', )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['status'] = instance.get_status_display()
        return representation

    def get_image_url(self, instance):
        muscle_category = getattr(instance, 'muscle_category', None)

        if muscle_category:
            return muscle_category.image_url
        else:
            "return a image to indicate it was a custom training set"
            return None
    