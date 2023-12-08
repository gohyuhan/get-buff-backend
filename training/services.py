from django.db import transaction

from constance import config

from training.models import (
    PresetTrainingExercise,
    CustomTrainingSet,
    CustomTrainingExercise,
    Exercise
)
from muscle.models import MuscleCategory
from muscle.enums import MuscleGroup
from training.enums import (
    TrainingLevel, 
    TrainingStatus, 
    TrainingType,
)
from user.models import (
    UserProfile,
    TrainingSetCompletedRecord
)
from .exceptions import (
    TrainingSetError,
    TrainingExerciseError
)
from user.exceptions import UserProfileError


def create_custom_preset_training_set(request):
    user = request.user
    profile_uuid = request.data.pop('profile')
    if not user.is_authenticated or not UserProfile.objects.filter(user=user, uuid=profile_uuid).exists():
        raise UserProfileError("Error on authentication, please logout and login again ")
    preset_exercise = request.data.pop('exercise')
    lvl = request.data.get('level')
    if len(preset_exercise)< config.TRAINING_EXERCISE_MIN_COUNT:
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
        user_profile=UserProfile.objects.get(uuid=profile_uuid),
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
                order = i+1,
                status = TrainingStatus.ONGOING,
            )
        except PresetTrainingExercise.DoesNotExist:
            pass

    return custom_training_set


def create_custom_training_set(request):
    """
    use to create custom training set based on user customization
    """
    user = request.user
    profile_uuid = request.data.pop('profile')
    if not user.is_authenticated or not UserProfile.objects.filter(user=user, uuid=profile_uuid).exists():
        raise UserProfileError("Error on authentication, please logout and login again ")
    custom_exercise = request.data.pop('exercise')
    if len(custom_exercise)< config.TRAINING_EXERCISE_MIN_COUNT:
        raise TrainingSetError("Exercise count should more than or equal 5")
    muscle_none, created = MuscleCategory.objects.get_or_create(
        name = 'None',
        type = MuscleGroup.CUSTOM,
        image_url = ''
    )
    with transaction.atomic():
        custom_training_set = CustomTrainingSet.objects.create(
            user_profile=UserProfile.objects.get(uuid=profile_uuid),
            name=request.data.get('name'),
            level=TrainingLevel.CUSTOM,
            muscle_category = muscle_none,
            status=TrainingStatus.ONGOING,
            training_type=TrainingType.CUSTOM
        )
        for i, exercise_set in enumerate(custom_exercise):
            try:
                exe = Exercise.objects.get(id=exercise_set['id'])
                if exercise_set['count']<exe.min_count:
                    raise TrainingExerciseError("Please make sure all exercise in you custom training meets the minimun reps/seconds")
                CustomTrainingExercise.objects.create(
                    calculate_in = exe.calculate_in,
                    required_value = exercise_set['count'],
                    level = TrainingLevel.CUSTOM,
                    belong_to_custom_training_set = custom_training_set,
                    exercise = exe,
                    order = i+1,
                    status = TrainingStatus.ONGOING,
                )
            except Exercise.DoesNotExist:
                pass

    return custom_training_set


def pause_training_set(request):
    user = request.user
    profile_uuid = request.data.pop('profile')
    if not user.is_authenticated or not UserProfile.objects.filter(user=user, uuid=profile_uuid).exists():
        raise UserProfileError("Error on authentication, please logout and login again ")
    custom_training_set_id = request.data.get('custom_training_set')
    custom_training_set = CustomTrainingSet.objects.get(
        id= custom_training_set_id,
        user_profile__user = user
    )
    custom_exercise = request.data.pop('exercise')
    for exercise_set in custom_exercise:
        try:
            exe = CustomTrainingExercise.objects.get(
                id = exercise_set['id'],
                belong_to_custom_training_set = custom_training_set
            )
            exe.status = return_training_status(exercise_set['status'])
            exe.save()
        except CustomTrainingExercise.DoesNotExist:
            pass


def conclude_training_set(request):
    user = request.user
    profile_uuid = request.data.pop('profile')
    user_profile = UserProfile.objects.filter(user=user, uuid=profile_uuid)
    if not user.is_authenticated or not user_profile.exists():
        raise UserProfileError("Error on authentication, please logout and login again ")
    custom_training_set_id = request.data.get('custom_training_set')
    custom_training_set = CustomTrainingSet.objects.get(
        id= custom_training_set_id,
        user_profile__user = user
    )
    CustomTrainingExercise.objects.filter(
        status = TrainingStatus.ONGOING,
        belong_to_custom_training_set=custom_training_set
    ).update(
        status = TrainingStatus.COMPLETED
    )
    custom_training_set.status = TrainingStatus.COMPLETED
    custom_training_set.save()
    TrainingSetCompletedRecord.objects.create(
        user_profile = UserProfile.objects.get(uuid=profile_uuid),
        training_set = custom_training_set
    )
    return user_profile.first(), custom_training_set


def give_up_training_set(request):
    user = request.user
    profile_uuid = request.data.pop('profile')
    if not user.is_authenticated or not UserProfile.objects.filter(user=user, uuid=profile_uuid).exists():
        raise UserProfileError("Error on authentication, please logout and login again ")
    custom_training_set_id = request.data.get('custom_training_set')
    custom_training_set = CustomTrainingSet.objects.get(
        id= custom_training_set_id,
        user_profile__user = user
    )
    CustomTrainingExercise.objects.filter(
        status = TrainingStatus.ONGOING,
        belong_to_custom_training_set=custom_training_set
    ).update(
        status = TrainingStatus.GIVEUP
    )
    custom_training_set.status = TrainingStatus.GIVEUP
    custom_training_set.save()


def ongoing_training_or_exercise(user):
    ongoing_training_set = CustomTrainingSet.objects.filter(user_profile__user = user, status = TrainingStatus.ONGOING)
    for training in ongoing_training_set:
        # check if the exercise tied with it has ongoing status else update the status with give up or completed
        if not CustomTrainingExercise.objects.filter(belong_to_custom_training_set = training, status = TrainingStatus.ONGOING).exists():
            if CustomTrainingExercise.objects.filter(belong_to_custom_training_set = training, status = TrainingStatus.GIVEUP).exists():
                training.status = TrainingStatus.GIVEUP
            else:
                training.status = TrainingStatus.COMPLETED
            training.save()
    if CustomTrainingSet.objects.filter(user_profile__user = user, status = TrainingStatus.ONGOING).exists():
        return True
    return False


def return_training_status(status):
    if status == TrainingStatus.COMPLETED.label:
        return TrainingStatus.COMPLETED
    elif status == TrainingStatus.GIVEUP.label:
        return TrainingStatus.GIVEUP
    else:
        return TrainingStatus.ONGOING