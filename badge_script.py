import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "get_buff.settings")
import django
django.setup()

from badges.enums import SpecialTargetType, TargetCountType

from badges.models import Badge, SkeletonAchivementBadge, Track
from muscle.enums import MuscleGroup
from training.enums import TrainingLevel, TrainingOrExerciseType


badges={
    'badge_1':Badge.objects.create(name='1st Training Completed', image='https://res.cloudinary.com/dmoa45uta/image/upload/v1702637431/First-training---1st-2_vvsz1q.png'),
    'badge_2':Badge.objects.create(name='100 Exercise Completed', image='https://res.cloudinary.com/dmoa45uta/image/upload/v1702637631/Level-1-exercise_ackhw2.png'),
}
tracks={
    'track_1':Track.objects.create(
        special_target = SpecialTargetType.NONE,
        type_target = TrainingOrExerciseType.TRAINING,
        level_target = TrainingLevel.NONE,
        muscle_target = MuscleGroup.NONE,
        count_type = TargetCountType.COUNT,
        streak_count_required = 0
    ),
    'track_2':Track.objects.create(
        special_target = SpecialTargetType.NONE,
        type_target = TrainingOrExerciseType.EXERCISE,
        level_target = TrainingLevel.NONE,
        muscle_target = MuscleGroup.NONE,
        count_type = TargetCountType.COUNT,
        streak_count_required = 0
    ),
}

SkeletonAchivementBadge.objects.create(
    desp = "Completed Your 1st training of any level to earn this badge",
    required_value = 1,
    badge = badges['badge_1'],
    track = tracks['track_1']
)
SkeletonAchivementBadge.objects.create(
    desp = "Completed a total of 100 exercise of any level to earn this badge",
    required_value = 100,
    badge = badges['badge_2'],
    track = tracks['track_2']
)