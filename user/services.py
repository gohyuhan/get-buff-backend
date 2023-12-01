from datetime import datetime, timedelta

from .serializer import (
    UserProfileSerializer,
    TrainingSettingSerializer
)
from .models import TrainingSetting, UserProfile, TrainingSetCompletedRecord
from .enums import TargetStatus
from .exceptions import UserProfileError
from user.enums import TargetStatus


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


def calories_calculator(user, kg_gain_lost):
    try:
        user_profile = UserProfile.objects.get(user=user)
        if(
            user_profile.weight_in_kg is not None and
            user_profile.height_in_cm is not None and
            user_profile.gender is not None and
            user_profile.dob is not None
        ):
            age = _calculate_age(user_profile.dob)
            # calculate bmr
            if user_profile.gender == "male":
                bmr = ( float(10) * float(user_profile.weight_in_kg) ) + ( float(6.25) * float(user_profile.height_in_cm) ) - ( float(5) * float(age) ) + float(5)
            else:
                bmr = ( float(10) * float(user_profile.weight_in_kg) ) + ( float(6.25) * float(user_profile.height_in_cm) ) - ( float(5) * float(age) ) - float(161)

            # calculate TDEE
            tdee = float(bmr)* float(_determine_activity_level(user_profile))

            extra_caloreis_needed = float(kg_gain_lost)*float(7700/7)
            if user_profile.weight_target_status == TargetStatus.LOSS:
                return round(tdee-extra_caloreis_needed)
            elif user_profile.weight_target_status == TargetStatus.GAIN:
                return round(tdee + extra_caloreis_needed)
            return round(tdee)
        else:
            raise UserProfileError("Please provide your weight(kg), height(cm), gender and date of birth to calculate your calories needed")
    except UserProfile.DoesNotExist:
        raise UserProfileError("Profile Error, Try logout and login again")
    

def _calculate_age(dob):
    today = datetime.now()

    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

    return age


def _determine_activity_level(user_profile):
    """
    to check how active a user was in term of training/activity.
    we user completed training activities that were completed by the user for the 
    pass 7 days when the user request for calories calculation
    """
    end_date = datetime.now()
    start_date = end_date - timedelta(days=7)
    training_completed = len(TrainingSetCompletedRecord.objects.filter(completed_date_time__range=(start_date, end_date)))
    if training_completed<1:
        return 1.2
    elif training_completed>=1 and training_completed<=3:
        return 1.375
    elif training_completed>=4 and training_completed<=5:
        return 1.55
    elif training_completed>=6 and training_completed<=7:
        return 1.725
    elif training_completed>=8:
        return 1.9
    
    