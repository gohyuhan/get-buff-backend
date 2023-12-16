import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "get_buff.settings")
import django
django.setup()

from badges.enums import SpecialTargetType, TargetCountType

from badges.models import Badge, SkeletonAchivementBadge, Track
from muscle.enums import MuscleGroup
from training.enums import TrainingLevel, TrainingOrExerciseType


badges={
    # User complete first training (1st)
    'badge_1':Badge.objects.create(name='1st Training Completed', image='https://res.cloudinary.com/dmoa45uta/image/upload/q_auto:best/f_auto/v1702720500/gotBuff/medals/First-training---1st-2_uknb9b.png'),
    # User complete level 1000  exercise
    # User complete level 2500 exercise 
    # User complete level 5000 exercise
    'badge_2':Badge.objects.create(name='1000 Exercise Completed', image='https://res.cloudinary.com/dmoa45uta/image/upload/q_auto:best/f_auto/v1702720504/gotBuff/medals/Level-1-exercise_x1eyim.png'),
    'badge_3':Badge.objects.create(name='2500 Exercise Completed', image='https://res.cloudinary.com/dmoa45uta/image/upload/q_auto:best/f_auto/v1702720513/gotBuff/medals/Level-2-exercise_rfhu4u.png'),
    'badge_4':Badge.objects.create(name='5000 Exercise Completed', image='https://res.cloudinary.com/dmoa45uta/image/upload/q_auto:best/f_auto/v1702720521/gotBuff/medals/Level-3-exercise_klgg6m.png'),
    # User complete level 100 training
    # User complete level 500  training
    # User complete level 1000 training
    'badge_5':Badge.objects.create(name='100 Training Completed', image='https://res.cloudinary.com/dmoa45uta/image/upload/q_auto:best/f_auto/v1702720508/gotBuff/medals/Level-1-training_eohnyr.png'),
    'badge_6':Badge.objects.create(name='250 Training Completed', image='https://res.cloudinary.com/dmoa45uta/image/upload/q_auto:best/f_auto/v1702720517/gotBuff/medals/Level-2-training_uwww7j.png'),
    'badge_7':Badge.objects.create(name='500 Training Completed', image='https://res.cloudinary.com/dmoa45uta/image/upload/q_auto:best/f_auto/v1702720525/gotBuff/medals/Level-3-training_vldx4v.png'),
    # User complete level 50 training (beginner)
    # User complete level 100 training (beginner)
    # User complete level 200 training (beginner)
    'badge_8':Badge.objects.create(name='50 Beginner Training Completed', image='https://res.cloudinary.com/dmoa45uta/image/upload/q_auto:best/f_auto/v1702720507/gotBuff/medals/Level-1-training---Beginner_z1w7h3.png'),
    'badge_9':Badge.objects.create(name='100 Beginner Training Completed', image='https://res.cloudinary.com/dmoa45uta/image/upload/q_auto:best/f_auto/v1702720515/gotBuff/medals/Level-2-training---Beginner_byudgt.png'),
    'badge_10':Badge.objects.create(name='200 Beginner Training Completed', image='https://res.cloudinary.com/dmoa45uta/image/upload/q_auto:best/f_auto/v1702720523/gotBuff/medals/Level-3-training---Beginner_erhw76.png'),
    # User complete level 50 training (intermediate)
    # User complete level 100 training (intermediate)
    # User complete level 200 training (intermediate)
    'badge_11':Badge.objects.create(name='50 Intermediate Training Completed', image='https://res.cloudinary.com/dmoa45uta/image/upload/q_auto:best/f_auto/v1702720507/gotBuff/medals/Level-1-training---Intermediate_uig6q6.png'),
    'badge_12':Badge.objects.create(name='100 Intermediate Training Completed', image='https://res.cloudinary.com/dmoa45uta/image/upload/q_auto:best/f_auto/v1702720516/gotBuff/medals/Level-2-training---Intermediate_rghine.png'),
    'badge_13':Badge.objects.create(name='200 Intermediate Training Completed', image='https://res.cloudinary.com/dmoa45uta/image/upload/q_auto:best/f_auto/v1702720524/gotBuff/medals/Level-3-training---Intermediate_geex3n.png'),
    # User complete level 50 training (advance)
    # User complete level 100 training (advance)
    # User complete level 200 training (advance)
    'badge_14':Badge.objects.create(name='50 Advance Training Completed', image='https://res.cloudinary.com/dmoa45uta/image/upload/q_auto:best/f_auto/v1702720509/gotBuff/medals/Level-1-training---Advance_wmtzot.png'),
    'badge_15':Badge.objects.create(name='100 Advance Training Completed', image='https://res.cloudinary.com/dmoa45uta/image/upload/q_auto:best/f_auto/v1702720514/gotBuff/medals/Level-2-training---Advance_isvyww.png'),
    'badge_16':Badge.objects.create(name='200 Advance Training Completed', image='https://res.cloudinary.com/dmoa45uta/image/upload/q_auto:best/f_auto/v1702720523/gotBuff/medals/Level-3-training---Advance_qpkejz.png'),
    # User complete level 10 legs training 
    # User complete level 50 legs training 
    # User complete level 100 legs training 
    'badge_17':Badge.objects.create(name='10 Legs Training Completed', image='https://res.cloudinary.com/dmoa45uta/image/upload/q_auto:best/f_auto/v1702720505/gotBuff/medals/Level-1-Legs-training_hi3xyz.png'),
    'badge_18':Badge.objects.create(name='50 Legs Training Completed', image='https://res.cloudinary.com/dmoa45uta/image/upload/q_auto:best/f_auto/v1702720513/gotBuff/medals/Level-2-Legs-training_avhau3.png'),
    'badge_19':Badge.objects.create(name='100 Legs Training Completed', image='https://res.cloudinary.com/dmoa45uta/image/upload/q_auto:best/f_auto/v1702720522/gotBuff/medals/Level-3-Legs-training_frvmuy.png'),
    # User complete level 10 chest training 
    # User complete level 50 chest training 
    # User complete level 100 chest training 
    'badge_20':Badge.objects.create(name='10 Chest Training Completed', image='https://res.cloudinary.com/dmoa45uta/image/upload/q_auto:best/f_auto/v1702720503/gotBuff/medals/Level-1-chest-training_cqiynz.png'),
    'badge_21':Badge.objects.create(name='50 Chest Training Completed', image='https://res.cloudinary.com/dmoa45uta/image/upload/q_auto:best/f_auto/v1702720512/gotBuff/medals/Level-2-chest-training_aznlfq.png'),
    'badge_22':Badge.objects.create(name='100 Chest Training Completed', image='https://res.cloudinary.com/dmoa45uta/image/upload/q_auto:best/f_auto/v1702720520/gotBuff/medals/Level-3-chest-training_yiqejw.png'),
    # User complete level 10 arm training 
    # User complete level 50 arm training 
    # User complete level 100 arm training 
    'badge_23':Badge.objects.create(name='10 Arm Training Completed', image='https://res.cloudinary.com/dmoa45uta/image/upload/q_auto:best/f_auto/v1702720502/gotBuff/medals/Level-1-arm-training_nbpf3y.png'),
    'badge_24':Badge.objects.create(name='50 Arm Training Completed', image='https://res.cloudinary.com/dmoa45uta/image/upload/q_auto:best/f_auto/v1702720510/gotBuff/medals/Level-2-arm-training_xipre1.png'),
    'badge_25':Badge.objects.create(name='100 Arm Training Completed', image='https://res.cloudinary.com/dmoa45uta/image/upload/q_auto:best/f_auto/v1702720519/gotBuff/medals/Level-3-arm-training_pqha6e.png'),
    # User complete level 10 back and shoulder training 
    # User complete level 50 back and shoulder training 
    # User complete level 100 back and shoulder training 
    'badge_26':Badge.objects.create(name='10 Back & Shoulder Training Completed', image='https://res.cloudinary.com/dmoa45uta/image/upload/q_auto:best/f_auto/v1702720503/gotBuff/medals/Level-1-Back-training_qhsw80.png'),
    'badge_27':Badge.objects.create(name='50 Back & Shoulder Training Completed', image='https://res.cloudinary.com/dmoa45uta/image/upload/q_auto:best/f_auto/v1702720511/gotBuff/medals/Level-2-Back-training_da5xuv.png'),
    'badge_28':Badge.objects.create(name='100 Back & Shoulder Training Completed', image='https://res.cloudinary.com/dmoa45uta/image/upload/q_auto:best/f_auto/v1702720519/gotBuff/medals/Level-3-Back-training_s3lbuw.png'),
    # User complete level 10 abs training 
    # User complete level 50 abs training 
    # User complete level 100 abs training 
    'badge_29':Badge.objects.create(name='10 Abs Training Completed', image='https://res.cloudinary.com/dmoa45uta/image/upload/q_auto:best/f_auto/v1702720501/gotBuff/medals/Level-1-Abs-training_cobyyb.png'),
    'badge_30':Badge.objects.create(name='50 Abs Training Completed', image='https://res.cloudinary.com/dmoa45uta/image/upload/q_auto:best/f_auto/v1702720509/gotBuff/medals/Level-2-Abs-training_ef2ztj.png'),
    'badge_31':Badge.objects.create(name='100 Abs Training Completed', image='https://res.cloudinary.com/dmoa45uta/image/upload/q_auto:best/f_auto/v1702720517/gotBuff/medals/Level-3-Abs-training_ko2ebp.png'),
    # User Obtain All Other Badges
    'badge_32':Badge.objects.create(name='All Achivement Badge Obtained', image='https://res.cloudinary.com/dmoa45uta/image/upload/q_auto:best/f_auto/v1702720500/gotBuff/medals/Done-training-for-365-days-without-stop_w2ubpd.png'),
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
    'track_3':Track.objects.create(
        special_target = SpecialTargetType.NONE,
        type_target = TrainingOrExerciseType.TRAINING,
        level_target = TrainingLevel.BEGINNER,
        muscle_target = MuscleGroup.NONE,
        count_type = TargetCountType.COUNT,
        streak_count_required = 0
    ),
    'track_4':Track.objects.create(
        special_target = SpecialTargetType.NONE,
        type_target = TrainingOrExerciseType.TRAINING,
        level_target = TrainingLevel.INTERMEDIATE,
        muscle_target = MuscleGroup.NONE,
        count_type = TargetCountType.COUNT,
        streak_count_required = 0
    ),
    'track_5':Track.objects.create(
        special_target = SpecialTargetType.NONE,
        type_target = TrainingOrExerciseType.TRAINING,
        level_target = TrainingLevel.ADVANCE,
        muscle_target = MuscleGroup.NONE,
        count_type = TargetCountType.COUNT,
        streak_count_required = 0
    ),
    'track_6':Track.objects.create(
        special_target = SpecialTargetType.NONE,
        type_target = TrainingOrExerciseType.TRAINING,
        level_target = TrainingLevel.NONE,
        muscle_target = MuscleGroup.ABS,
        count_type = TargetCountType.COUNT,
        streak_count_required = 0
    ),
    'track_7':Track.objects.create(
        special_target = SpecialTargetType.NONE,
        type_target = TrainingOrExerciseType.TRAINING,
        level_target = TrainingLevel.NONE,
        muscle_target = MuscleGroup.LEGS,
        count_type = TargetCountType.COUNT,
        streak_count_required = 0
    ),
    'track_8':Track.objects.create(
        special_target = SpecialTargetType.NONE,
        type_target = TrainingOrExerciseType.TRAINING,
        level_target = TrainingLevel.NONE,
        muscle_target = MuscleGroup.CHEST,
        count_type = TargetCountType.COUNT,
        streak_count_required = 0
    ),
    'track_9':Track.objects.create(
        special_target = SpecialTargetType.NONE,
        type_target = TrainingOrExerciseType.TRAINING,
        level_target = TrainingLevel.NONE,
        muscle_target = MuscleGroup.ARMS,
        count_type = TargetCountType.COUNT,
        streak_count_required = 0
    ),
    'track_10':Track.objects.create(
        special_target = SpecialTargetType.NONE,
        type_target = TrainingOrExerciseType.TRAINING,
        level_target = TrainingLevel.NONE,
        muscle_target = MuscleGroup.BACKNSHOULDER,
        count_type = TargetCountType.COUNT,
        streak_count_required = 0
    ),
    'track_11':Track.objects.create(
        special_target = SpecialTargetType.ALL,
        type_target = TrainingOrExerciseType.NONE,
        level_target = TrainingLevel.NONE,
        muscle_target = MuscleGroup.NONE,
        count_type = TargetCountType.NONE,
        streak_count_required = 0
    ),
}

# track 1 
SkeletonAchivementBadge.objects.create(
    desp = "Completed Your 1st training of any level to earn this badge",
    required_value = 1,
    badge = badges['badge_1'],
    track = tracks['track_1']
)
SkeletonAchivementBadge.objects.create(
    desp = "Completed a total of 100 training of any level to earn this badge",
    required_value = 100,
    badge = badges['badge_5'],
    track = tracks['track_1']
)
SkeletonAchivementBadge.objects.create(
    desp = "Completed a total of 250 training of any level to earn this badge",
    required_value = 250,
    badge = badges['badge_6'],
    track = tracks['track_1']
)
SkeletonAchivementBadge.objects.create(
    desp = "Completed a total of 500 training of any level to earn this badge",
    required_value = 500,
    badge = badges['badge_7'],
    track = tracks['track_1']
)
# track 2
SkeletonAchivementBadge.objects.create(
    desp = "Completed a total of 1000 exercise of any level to earn this badge",
    required_value = 1000,
    badge = badges['badge_2'],
    track = tracks['track_2']
)
SkeletonAchivementBadge.objects.create(
    desp = "Completed a total of 2500 exercise of any level to earn this badge",
    required_value = 2500,
    badge = badges['badge_3'],
    track = tracks['track_2']
)
SkeletonAchivementBadge.objects.create(
    desp = "Completed a total of 5000 exercise of any level to earn this badge",
    required_value = 5000,
    badge = badges['badge_4'],
    track = tracks['track_2']
)

# track 3
SkeletonAchivementBadge.objects.create(
    desp = "Completed a total of 50 beginner level training to earn this badge",
    required_value = 50,
    badge = badges['badge_8'],
    track = tracks['track_3']
)
SkeletonAchivementBadge.objects.create(
    desp = "Completed a total of 100 beginner level training to earn this badge",
    required_value = 100,
    badge = badges['badge_9'],
    track = tracks['track_3']
)
SkeletonAchivementBadge.objects.create(
    desp = "Completed a total of 200 beginner level training to earn this badge",
    required_value = 200,
    badge = badges['badge_10'],
    track = tracks['track_3']
)
# track 4
SkeletonAchivementBadge.objects.create(
    desp = "Completed a total of 50 intermediate level training to earn this badge",
    required_value = 50,
    badge = badges['badge_11'],
    track = tracks['track_4']
)
SkeletonAchivementBadge.objects.create(
    desp = "Completed a total of 100 intermediate level training to earn this badge",
    required_value = 100,
    badge = badges['badge_12'],
    track = tracks['track_4']
)
SkeletonAchivementBadge.objects.create(
    desp = "Completed a total of 200 intermediate level training to earn this badge",
    required_value = 200,
    badge = badges['badge_13'],
    track = tracks['track_4']
)
# track 5
SkeletonAchivementBadge.objects.create(
    desp = "Completed a total of 50 advance level training to earn this badge",
    required_value = 50,
    badge = badges['badge_14'],
    track = tracks['track_5']
)
SkeletonAchivementBadge.objects.create(
    desp = "Completed a total of 100 advance level training to earn this badge",
    required_value = 100,
    badge = badges['badge_15'],
    track = tracks['track_5']
)
SkeletonAchivementBadge.objects.create(
    desp = "Completed a total of 200 advance level training to earn this badge",
    required_value = 200,
    badge = badges['badge_16'],
    track = tracks['track_5']
)
# track 6
SkeletonAchivementBadge.objects.create(
    desp = "Completed a total of 10 abs training to earn this badge",
    required_value = 10,
    badge = badges['badge_29'],
    track = tracks['track_6']
)
SkeletonAchivementBadge.objects.create(
    desp = "Completed a total of 50 abs training to earn this badge",
    required_value = 50,
    badge = badges['badge_30'],
    track = tracks['track_6']
)
SkeletonAchivementBadge.objects.create(
    desp = "Completed a total of 100 abs training to earn this badge",
    required_value = 100,
    badge = badges['badge_31'],
    track = tracks['track_6']
)
# track 7
SkeletonAchivementBadge.objects.create(
    desp = "Completed a total of 10 legs training to earn this badge",
    required_value = 10,
    badge = badges['badge_17'],
    track = tracks['track_7']
)
SkeletonAchivementBadge.objects.create(
    desp = "Completed a total of 50 legs training to earn this badge",
    required_value = 50,
    badge = badges['badge_18'],
    track = tracks['track_7']
)
SkeletonAchivementBadge.objects.create(
    desp = "Completed a total of 100 legs training to earn this badge",
    required_value = 100,
    badge = badges['badge_19'],
    track = tracks['track_7']
)
# track 8
SkeletonAchivementBadge.objects.create(
    desp = "Completed a total of 10 chest training to earn this badge",
    required_value = 10,
    badge = badges['badge_20'],
    track = tracks['track_8']
)
SkeletonAchivementBadge.objects.create(
    desp = "Completed a total of 50 chest training to earn this badge",
    required_value = 50,
    badge = badges['badge_21'],
    track = tracks['track_8']
)
SkeletonAchivementBadge.objects.create(
    desp = "Completed a total of 100 chest training to earn this badge",
    required_value = 100,
    badge = badges['badge_22'],
    track = tracks['track_8']
)
# track 9
SkeletonAchivementBadge.objects.create(
    desp = "Completed a total of 10 arms training to earn this badge",
    required_value = 10,
    badge = badges['badge_23'],
    track = tracks['track_9']
)
SkeletonAchivementBadge.objects.create(
    desp = "Completed a total of 50 arms training to earn this badge",
    required_value = 50,
    badge = badges['badge_24'],
    track = tracks['track_9']
)
SkeletonAchivementBadge.objects.create(
    desp = "Completed a total of 100 arms training to earn this badge",
    required_value = 100,
    badge = badges['badge_25'],
    track = tracks['track_9']
)
# track 10
SkeletonAchivementBadge.objects.create(
    desp = "Completed a total of 10 back & shoulder training to earn this badge",
    required_value = 10,
    badge = badges['badge_26'],
    track = tracks['track_10']
)
SkeletonAchivementBadge.objects.create(
    desp = "Completed a total of 50 back & shoulder training to earn this badge",
    required_value = 50,
    badge = badges['badge_27'],
    track = tracks['track_10']
)
SkeletonAchivementBadge.objects.create(
    desp = "Completed a total of 100 back & shoulder training to earn this badge",
    required_value = 100,
    badge = badges['badge_28'],
    track = tracks['track_10']
)
# track 11
SkeletonAchivementBadge.objects.create(
    desp = "Obtain all other achivement badges to earn this badge",
    required_value = 31,
    badge = badges['badge_32'],
    track = tracks['track_11']
)