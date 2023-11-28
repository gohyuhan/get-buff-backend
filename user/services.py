from .serializer import (
    UserProfileSerializer,
    TrainingSettingSerializer
)
from .models import TrainingSetting, UserProfile
from .enums import TargetStatus
from .exceptions import UserProfileError


def update_user_profile(request):
    serializer = UserProfileSerializer(data=request.data)
    user_profile = UserProfile.objects.get(user=request.user)
    if serializer.is_valid():
        user_profile.gender=serializer.data['gender']
        user_profile.weight_in_kg=serializer.data['weight_in_kg']
        user_profile.height_in_cm=serializer.data['height_in_cm']
        user_profile.target_weight_in_kg=serializer.data['target_weight_in_kg']
        
        if serializer.data['target_weight_in_kg']>serializer.data['weight_in_kg']:
            user_profile.weight_target_status = TargetStatus.GAIN
        elif serializer.data['target_weight_in_kg']<serializer.data['weight_in_kg']:
            user_profile.weight_target_status = TargetStatus.LOSS
        else:
            user_profile.weight_target_status = TargetStatus.MAINTAIN
        user_profile.save()
        return True
    return False


def update_user_training_setting(request):
    user = request.user
    profile_uuid = request.data.pop('profile')
    if not user.is_authenticated or not UserProfile.objects.filter(user=user, uuid=profile_uuid).exists():
        raise UserProfileError("Error on authentication, please logout and login again")
    serializer = TrainingSettingSerializer(data=request.data)
    if serializer.is_valid():
        TrainingSetting.objects.filter(
            user_profile__user = request.user
        ).update(rest_time=serializer.data['rest_time'])
        return serializer
    return False
