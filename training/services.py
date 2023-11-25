from django.conf import settings

from training.models import (
    PresetTrainingExercise,
    CustomTrainingSet,
    CustomTrainingExercise
)
from muscle.models import MuscleCategory
from training.enums import (
    TrainingLevel, 
    TrainingStatus, 
    TrainingType
)
from user.models import UserProfile
from .exceptions import TrainingSetError


def create_custom_preset_training_set(request):
    profile_id = request.data.pop('profile')
    preset_exercise = request.data.pop('exercise')
    lvl = request.data.get('level')
    if len(preset_exercise)< settings.TRAINING_EXERCISE_MIN_COUNT:
        raise TrainingSetError("Exercise count should more than or equal 5")
    try:
        muscle_category = MuscleCategory.objects.get(id = request.data.get('muscle_category')['id'])
    except MuscleCategory.DoesNotExist:
        muscle_category = None

    if lvl=="beginner":
        level = TrainingLevel.BEGINNER
    elif lvl=="intermediate":
        level =TrainingLevel.INTERMEDIATE
    else:
        level=TrainingLevel.ADVANCED

    custom_training_set = CustomTrainingSet.objects.create(
        user_profile=UserProfile.objects.get(id=profile_id),
        name=request.data.get('name'),
        level=level,
        muscle_category=muscle_category,
        status=TrainingStatus.ONGOING,
        training_type=TrainingType.PRESET
    )

    preset_exercise_id = [exe['id'] for exe in preset_exercise]
    for i, id in enumerate(preset_exercise_id):
        try:
            exe = PresetTrainingExercise.objects.get(id=id)
            CustomTrainingExercise.objects.create(
                calculate_in = exe.calculate_in,
                required_value = exe.required_value,
                level = exe.level,
                belong_to_custom_training_set = custom_training_set,
                exercise = exe.exercise,
                order = i,
                status = TrainingStatus.ONGOING,
            )
        except PresetTrainingExercise.DoesNotExist:
            pass

    return custom_training_set
