from .serializer import UserProfileSerializer
from .models import UserProfile
from .enums import TargetStatus


def update_user_profile(request):
    serializer = UserProfileSerializer(request.data)
    user_profile = UserProfile.objects.filter(user=request.user)
    if serializer.is_valid():
        user_profile.update(
            gender=serializer.data['gender'],
            weight_in_kg=serializer.data['weight_in_kg'],
            height_in_cm=serializer.data['height_in_cm'],
            target_weight_in_kg=serializer.data['target_weight_in_kg'],
        )
        if serializer.data['target_weight_in_kg']>serializer.data['weight_in_kg']:
            user_profile.weight_target_status = TargetStatus.GAIN
        elif serializer.data['target_weight_in_kg']<serializer.data['weight_in_kg']:
            user_profile.weight_target_status = TargetStatus.LOSS
        else:
            user_profile.weight_target_status = TargetStatus.MAINTAIN
        user_profile.save()
        return True
    return False