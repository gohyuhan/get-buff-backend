from .models import (
    Track,
    Badge,
    SkeletonAchivementBadge,
    UserAchivementBadge
)
from training.models import CustomTrainingExercise
from muscle.enums import MuscleGroup
from training.enums import (
    TrainingLevel,
    TrainingOrExerciseType
)
from .enums import (
    SpecialTargetType,
    TargetCountType,
)


# services
"""
NOTE: the achivement badges currently are only planned to be tracking training/exercise by counts,
      for special, it will also be tracking training streak by day counts.

NOTE IMPORTANT: be sure to be clear about how we track and handle achivement badges before working on it>
                ESPECIALLY about tracking
"""

def user_achivement_badge_create(user_profile):
    """
    a services to generate achivement badges for individual user,
    for more detail about badges work see `badges.model`
    """
    existing_user_badges_id = [
        badge.id for badge in
        UserAchivementBadge.objects.select_related('badge').filter(user_profile=user_profile)
    ] 

    # here the unown_badges didn't mean unobtained but didn't create for user to be tracked
    user_unown_badges = [
        badges for badges in SkeletonAchivementBadge.objects.all().order_by('id').exclude(badge__id__in=existing_user_badges_id)
    ]

    UserAchivementBadge.objects.bulk_create(
        [
            UserAchivementBadge(
                user_profile = user_profile,
                desp = badge.desp,
                required_value = badge.required_value,
                badge = badge.badge,
                track = badge.track
            )for badge in user_unown_badges
        ]
    )


def user_training_achivement_badge_progression_update(user_profile, training_set):
    """
    a services to update non special training/exercise tracked achivement badges
    """
    progression_updated_badges = []
    exercise_count = len(CustomTrainingExercise.objects.filter(belong_to_custom_training_set = training_set))
    inprogress_user_badges = UserAchivementBadge.objects.filter(user_profile = user_profile, is_obtained=False)

    # 1) update normal training progression count
    normal_training_count_badge = inprogress_user_badges.filter(
        track__special_target = SpecialTargetType.NONE,
        track__type_target = TrainingOrExerciseType.TRAINING,
        track__level_target = TrainingLevel.NONE,
        track__muscle_target = MuscleGroup.NONE,
        track__count_type = TargetCountType.COUNT,
    )
    for badge in normal_training_count_badge:
        badge.progress_count = badge.progress_count+1
        progression_updated_badges.append(badge)
        badge.save()

    # 2) update exercise progression count
    exercise_count_badge = inprogress_user_badges.filter(
        track__special_target = SpecialTargetType.NONE,
        track__type_target = TrainingOrExerciseType.EXERCISE,
        track__level_target = TrainingLevel.NONE,
        track__muscle_target = MuscleGroup.NONE,
        track__count_type = TargetCountType.COUNT,
    )
    for badge in exercise_count_badge:
        badge.progress_count = badge.progress_count+exercise_count
        progression_updated_badges.append(badge)
        badge.save()

    # 3) update training level progression count
    training_level_count_badge = inprogress_user_badges.filter(
        track__special_target = SpecialTargetType.NONE,
        track__type_target = TrainingOrExerciseType.TRAINING,
        track__level_target = training_set.level,
        track__muscle_target = MuscleGroup.NONE,
        track__count_type = TargetCountType.COUNT,
    )
    for badge in training_level_count_badge:
        badge.progress_count = badge.progress_count+1
        progression_updated_badges.append(badge)
        badge.save()

    # 4) update muscle training progression count
    training_level_count_badge = inprogress_user_badges.filter(
        track__special_target = SpecialTargetType.NONE,
        track__type_target = TrainingOrExerciseType.TRAINING,
        track__level_target = TrainingLevel.NONE,
        track__muscle_target = training_set.muscle_category.type,
        track__count_type = TargetCountType.COUNT,
    )
    for badge in training_level_count_badge:
        badge.progress_count = badge.progress_count+1
        progression_updated_badges.append(badge)
        badge.save()

    # 5) track special target achivement ( should only consist of 1 model )
    progression_updated_badges + track_special_badge_all_other_non_special_badges_obtain(inprogress_user_badges, user_profile)
    

    return user_newly_obtained_achivement_badge(progression_updated_badges, True)
 

def user_training_streak_achivement_badge_progression_update(user_profile):
    """
    a services to update special (streak) training/exercise tracked achivement badges
    """
    pass


def user_newly_obtained_achivement_badge(badges_list, return_list=False):
    """
    return list is set to false by default
    if set to true, will return a list of newly obtained badges
    """
    newly_obtained_list=[]
    for badge in badges_list:
        if badge.is_obtainable():
            newly_obtained_list.append(badge)
            badge.set_obtained()
    if return_list:
        return newly_obtained_list
    
   
def track_special_badge_all_other_non_special_badges_obtain(inprogress_user_badges, user_profile):
    # update special badge progress
    return_list=[]
    special_training_count_badge = inprogress_user_badges.filter(
        track__special_target = SpecialTargetType.ALL,
        track__type_target = TrainingOrExerciseType.NONE,
        track__level_target = TrainingLevel.NONE,
        track__muscle_target = MuscleGroup.NONE,
        track__count_type = TargetCountType.NONE,
    )
    for badge in special_training_count_badge:
        badge.progress_count = len(UserAchivementBadge.objects.filter(user_profile = user_profile, is_obtained=False))
        badge.save()
        return_list.append(badge)
    return return_list