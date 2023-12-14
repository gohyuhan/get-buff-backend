import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "get_buff.settings")
import django
django.setup()

from training.models import (
    Exercise,
    PresetTrainingSet,
    PresetTrainingExercise,
)
from muscle.models import (
    Muscle,
    MuscleCategory
)
from training.enums import (
    TrainingLevel,
    TrainingStatus,
    TrainingType,
    CalculatedIn
)
from muscle.enums import MuscleGroup

muscle_cat={
    "abs":MuscleCategory.objects.create(
        name = 'abs',
        type = MuscleGroup.ABS,
        image_url = ""
    ),
    "legs":MuscleCategory.objects.create(
        name = 'legs',
        type = MuscleGroup.LEGS,
        image_url = ""
    ),
    "chest":MuscleCategory.objects.create(
        name = 'chest',
        type = MuscleGroup.CHEST,
        image_url = ""
    ),
    "arms":MuscleCategory.objects.create(
        name = 'arms',
        type = MuscleGroup.ARMS,
        image_url = ""
    ),
    "back_and_shoulder":MuscleCategory.objects.create(
        name = 'back and shoulder',
        type = MuscleGroup.BACKNSHOULDER,
        image_url = ""
    ),
}

muscle={
    "shoulders":Muscle.objects.create(
        name = "Shoulder",
        front_image_url = "v1702096178/front_mus/shoulder_qgiv1v.png",
        back_image_url = "v1702096908/back_mus/shoulder_htgsbt.png",
        muscle_category = muscle_cat['back_and_shoulder']
    ),
    "quadriceps":Muscle.objects.create(
        name = "Quadriceps",
        front_image_url = "v1702096178/front_mus/quadriceps_k5dd3k.png",
        back_image_url = "",
        muscle_category = muscle_cat['legs']
    ),
    "adductors":Muscle.objects.create(
        name = "Adductors",
        front_image_url = "v1702096187/front_mus/adductors_qzgbvn.png",
        back_image_url = "",
        muscle_category = muscle_cat['legs']
    ),
    "calves":Muscle.objects.create(
        name = "Calves",
        front_image_url = "v1702096188/front_mus/calves_c93tid.png",
        back_image_url = "v1702096228/back_mus/calves_iks153.png",
        muscle_category = muscle_cat['legs']
    ),
    "chest":Muscle.objects.create(
        name = "Chest",
        front_image_url = "v1702096189/front_mus/chest_bbarf5.png",
        back_image_url = "",
        muscle_category = muscle_cat['chest']
    ),
    "abs":Muscle.objects.create(
        name = "abs",
        front_image_url = "v1702096187/front_mus/abs_g05kvf.png",
        back_image_url = "v1702096227/back_mus/abs_eki5ks.png",
        muscle_category = muscle_cat['abs']
    ),
    "traps":Muscle.objects.create(
        name = "Traps",
        front_image_url = "v1702096178/front_mus/traps_hfpg03.png",
        back_image_url = "v1702096210/back_mus/traps_wtvvpn.png",
        muscle_category = muscle_cat['back_and_shoulder']
    ),
    "biceps":Muscle.objects.create(
        name = "Biceps",
        front_image_url = "v1702096188/front_mus/biceps_d8tm5x.png",
        back_image_url = "",
        muscle_category = muscle_cat['arms']
    ),
    "forearms":Muscle.objects.create(
        name = "Forearms",
        front_image_url = "v1702096189/front_mus/forearm_ctwhlr.png",
        back_image_url = "v1702096229/back_mus/forearm_oigbse.png",
        muscle_category = muscle_cat['arms']
    ),
    "glutes":Muscle.objects.create(
        name = "Glutes",
        front_image_url = "",
        back_image_url = "v1702103841/back_mus/glutes_p55x0j.png",
        muscle_category = muscle_cat['legs']
    ),
    "hamstrings":Muscle.objects.create(
        name = "Hamstrings",
        front_image_url = "",
        back_image_url = "v1702096230/back_mus/hamstrings_i107aa.png",
        muscle_category = muscle_cat['legs']
    ),
    "triceps":Muscle.objects.create(
        name = "Triceps",
        front_image_url = "",
        back_image_url = "v1702096211/back_mus/triceps_jv9uop.png",
        muscle_category = muscle_cat['arms']
    ),
    "back":Muscle.objects.create(
        name = "Back",
        front_image_url = "",
        back_image_url = "v1702096227/back_mus/back_mpebeq.png",
        muscle_category = muscle_cat["back_and_shoulder"]
    ),
}

prest_training_set={
    'prest_abs_beginner':PresetTrainingSet.objects.create(
        name = "ABS BEGINNER",
        level = TrainingLevel.BEGINNER,
        muscle_category = muscle_cat['abs']
    ),
    'prest_chest_beginner':PresetTrainingSet.objects.create(
        name = "CHEST BEGINNER",
        level = TrainingLevel.BEGINNER,
        muscle_category = muscle_cat['chest']
    ),
    'prest_leg_beginner':PresetTrainingSet.objects.create(
        name = "LEG BEGINNER",
        level = TrainingLevel.BEGINNER,
        muscle_category = muscle_cat['legs']
    ),
    'prest_arm_beginner':PresetTrainingSet.objects.create(
        name = "ARM BEGINNER",
        level = TrainingLevel.BEGINNER,
        muscle_category = muscle_cat['arms']
    ),
    'prest_back_and_shoulder_beginner':PresetTrainingSet.objects.create(
        name = "BACK & SHOULDER BEGINNER",
        level = TrainingLevel.BEGINNER,
        muscle_category = muscle_cat["back_and_shoulder"]
    ),
    'prest_abs_intermediate':PresetTrainingSet.objects.create(
        name = "ABS INTERMEDIATE",
        level = TrainingLevel.INTERMEDIATE,
        muscle_category = muscle_cat['abs']
    ),
    'prest_chest_intermediate':PresetTrainingSet.objects.create(
        name = "CHEST INTERMEDIATE",
        level = TrainingLevel.INTERMEDIATE,
        muscle_category = muscle_cat['chest']
    ),
    'prest_leg_intermediate':PresetTrainingSet.objects.create(
        name = "LEG INTERMEDIATE",
        level = TrainingLevel.INTERMEDIATE,
        muscle_category = muscle_cat['legs']
    ),
    'prest_arm_intermediate':PresetTrainingSet.objects.create(
        name = "ARM INTERMEDIATE",
        level = TrainingLevel.INTERMEDIATE,
        muscle_category = muscle_cat['arms']
    ),
    'prest_back_and_shoulder_intermediate':PresetTrainingSet.objects.create(
        name = "BACK & SHOULDER INTERMEDIATE",
        level = TrainingLevel.INTERMEDIATE,
        muscle_category = muscle_cat["back_and_shoulder"]
    ),
    'prest_abs_advance':PresetTrainingSet.objects.create(
        name = "ABS ADVANCE",
        level = TrainingLevel.ADVANCE,
        muscle_category = muscle_cat['abs']
    ),
    'prest_chest_advance':PresetTrainingSet.objects.create(
        name = "CHEST ADVANCE",
        level = TrainingLevel.ADVANCE,
        muscle_category = muscle_cat['chest']
    ),
    'prest_leg_advance':PresetTrainingSet.objects.create(
        name = "LEG ADVANCE",
        level = TrainingLevel.ADVANCE,
        muscle_category = muscle_cat['legs']
    ),
    'prest_arm_advance':PresetTrainingSet.objects.create(
        name = "ARM ADVANCE",
        level = TrainingLevel.ADVANCE,
        muscle_category = muscle_cat['arms']
    ),
    'prest_back_and_shoulder_advance':PresetTrainingSet.objects.create(
        name = "BACK & SHOULDER ADVANCE",
        level = TrainingLevel.ADVANCE,
        muscle_category = muscle_cat["back_and_shoulder"]
    )
}

jumping_jack = Exercise.objects.create(
    name = 'JUMPING JACKS',
    explanation = "...exp",
    calculate_in = CalculatedIn.SECONDS,
    animation = "",
    min_count = 15
)
jumping_jack.muscle_category.add(muscle_cat['back_and_shoulder'])
jumping_jack.muscle_category.add(muscle_cat['arms'])
jumping_jack.muscle_category.add(muscle_cat['legs'])
jumping_jack.muscle.add(muscle['shoulders'])
jumping_jack.muscle.add(muscle["quadriceps"])
jumping_jack.muscle.add(muscle["adductors"])
jumping_jack.muscle.add(muscle["glutes"])
jumping_jack.muscle.add(muscle["calves"])
jumping_jack.muscle.add(muscle["chest"])
jumping_jack.save()


abdominal_crunches = Exercise.objects.create(
    name = 'ABDOMINAL CRUNCHES',
    explanation = "...exp",
    calculate_in = CalculatedIn.REPS,
    animation = "",
    min_count = 8
)
abdominal_crunches.muscle_category.add(muscle_cat["abs"])
abdominal_crunches.muscle.add(muscle["abs"])
abdominal_crunches.save()


incline_push = Exercise.objects.create(
    name = 'INCLINE PUSH',
    explanation = "...exp",
    calculate_in = CalculatedIn.REPS,
    animation = "",
    min_count = 8
)
incline_push.muscle_category.add(muscle_cat["chest"])
incline_push.muscle_category.add(muscle_cat["arms"])
incline_push.muscle.add(muscle["chest"])
incline_push.muscle.add(muscle["shoulders"])
incline_push.muscle.add(muscle["triceps"])
incline_push.save()


arm_raise = Exercise.objects.create(
    name = 'ARM RAISE',
    explanation = "...exp",
    calculate_in = CalculatedIn.SECONDS,
    animation = "",
    min_count = 15
)
arm_raise.muscle_category.add(muscle_cat["chest"])
arm_raise.muscle_category.add(muscle_cat["back_and_shoulder"])
arm_raise.muscle.add(muscle["chest"])
arm_raise.muscle.add(muscle["shoulders"])
arm_raise.save()


side_arm_raise = Exercise.objects.create(
    name = 'SIDE ARM RAISE',
    explanation = "...exp",
    calculate_in = CalculatedIn.SECONDS,
    animation = "",
    min_count = 15
)
side_arm_raise.muscle_category.add(muscle_cat["back_and_shoulder"])
side_arm_raise.muscle.add(muscle["shoulders"])
side_arm_raise.save()


side_hop = Exercise.objects.create(
    name = 'SIDE HOP',
    explanation = "...exp",
    calculate_in = CalculatedIn.SECONDS,
    animation = "",
    min_count = 15
)
side_hop.muscle_category.add(muscle_cat["legs"])
side_hop.muscle.add(muscle["glutes"])
side_hop.muscle.add(muscle["quadriceps"])
side_hop.muscle.add(muscle["hamstrings"])
side_hop.muscle.add(muscle["calves"])
side_hop.save()


squats = Exercise.objects.create(
    name = 'SQUATS',
    explanation = "...exp",
    calculate_in = CalculatedIn.REPS,
    animation = "",
    min_count = 8
)
squats.muscle_category.add(muscle_cat["legs"])
squats.muscle.add(muscle["glutes"])
squats.muscle.add(muscle["quadriceps"])
squats.muscle.add(muscle["hamstrings"])
squats.muscle.add(muscle["calves"])
squats.save()

# beginner preset exercise
PresetTrainingExercise.objects.create(
    calculate_in = jumping_jack.calculate_in,
    required_value = 20,
    level = TrainingLevel.BEGINNER,
    belong_to_training_set = prest_training_set['prest_abs_beginner'],
    exercise = jumping_jack,
    order=1
)
PresetTrainingExercise.objects.create(
    calculate_in = jumping_jack.calculate_in,
    required_value = 20,
    level = TrainingLevel.BEGINNER,
    belong_to_training_set = prest_training_set['prest_abs_beginner'],
    exercise = jumping_jack,
    order=2
)
PresetTrainingExercise.objects.create(
    calculate_in = jumping_jack.calculate_in,
    required_value = 20,
    level = TrainingLevel.BEGINNER,
    belong_to_training_set = prest_training_set['prest_abs_beginner'],
    exercise = jumping_jack,
    order=3
)
PresetTrainingExercise.objects.create(
    calculate_in = abdominal_crunches.calculate_in,
    required_value = 16,
    level = TrainingLevel.BEGINNER,
    belong_to_training_set = prest_training_set['prest_abs_beginner'],
    exercise = abdominal_crunches,
    order=4
)
PresetTrainingExercise.objects.create(
    calculate_in = abdominal_crunches.calculate_in,
    required_value = 16,
    level = TrainingLevel.BEGINNER,
    belong_to_training_set = prest_training_set['prest_abs_beginner'],
    exercise = abdominal_crunches,
    order=5
)


PresetTrainingExercise.objects.create(
    calculate_in = jumping_jack.calculate_in,
    required_value = 20,
    level = TrainingLevel.BEGINNER,
    belong_to_training_set = prest_training_set["prest_chest_beginner"],
    exercise = jumping_jack,
    order=1
)
PresetTrainingExercise.objects.create(
    calculate_in = jumping_jack.calculate_in,
    required_value = 20,
    level = TrainingLevel.BEGINNER,
    belong_to_training_set = prest_training_set["prest_chest_beginner"],
    exercise = jumping_jack,
    order=2
)
PresetTrainingExercise.objects.create(
    calculate_in = jumping_jack.calculate_in,
    required_value = 20,
    level = TrainingLevel.BEGINNER,
    belong_to_training_set = prest_training_set["prest_chest_beginner"],
    exercise = jumping_jack,
    order=3
)
PresetTrainingExercise.objects.create(
    calculate_in = incline_push.calculate_in,
    required_value = 16,
    level = TrainingLevel.BEGINNER,
    belong_to_training_set = prest_training_set["prest_chest_beginner"],
    exercise = incline_push,
    order=4
)
PresetTrainingExercise.objects.create(
    calculate_in = incline_push.calculate_in,
    required_value = 16,
    level = TrainingLevel.BEGINNER,
    belong_to_training_set = prest_training_set["prest_chest_beginner"],
    exercise = incline_push,
    order=5
)


PresetTrainingExercise.objects.create(
    calculate_in = arm_raise.calculate_in,
    required_value = 30,
    level = TrainingLevel.BEGINNER,
    belong_to_training_set = prest_training_set["prest_arm_beginner"],
    exercise = arm_raise,
    order=1
)
PresetTrainingExercise.objects.create(
    calculate_in = arm_raise.calculate_in,
    required_value = 30,
    level = TrainingLevel.BEGINNER,
    belong_to_training_set = prest_training_set["prest_arm_beginner"],
    exercise = arm_raise,
    order=2
)
PresetTrainingExercise.objects.create(
    calculate_in = arm_raise.calculate_in,
    required_value = 30,
    level = TrainingLevel.BEGINNER,
    belong_to_training_set = prest_training_set["prest_arm_beginner"],
    exercise = arm_raise,
    order=3
)
PresetTrainingExercise.objects.create(
    calculate_in = side_arm_raise.calculate_in,
    required_value = 30,
    level = TrainingLevel.BEGINNER,
    belong_to_training_set = prest_training_set["prest_arm_beginner"],
    exercise = side_arm_raise,
    order=4
)
PresetTrainingExercise.objects.create(
    calculate_in = side_arm_raise.calculate_in,
    required_value = 30,
    level = TrainingLevel.BEGINNER,
    belong_to_training_set = prest_training_set["prest_arm_beginner"],
    exercise = side_arm_raise,
    order=5
)


PresetTrainingExercise.objects.create(
    calculate_in = side_hop.calculate_in,
    required_value = 30,
    level = TrainingLevel.BEGINNER,
    belong_to_training_set = prest_training_set["prest_leg_beginner"],
    exercise = side_hop,
    order=1
)
PresetTrainingExercise.objects.create(
    calculate_in = side_hop.calculate_in,
    required_value = 30,
    level = TrainingLevel.BEGINNER,
    belong_to_training_set = prest_training_set["prest_leg_beginner"],
    exercise = side_hop,
    order=2
)
PresetTrainingExercise.objects.create(
    calculate_in = side_hop.calculate_in,
    required_value = 30,
    level = TrainingLevel.BEGINNER,
    belong_to_training_set = prest_training_set["prest_leg_beginner"],
    exercise = side_hop,
    order=3
)
PresetTrainingExercise.objects.create(
    calculate_in = squats.calculate_in,
    required_value = 16,
    level = TrainingLevel.BEGINNER,
    belong_to_training_set = prest_training_set["prest_leg_beginner"],
    exercise = squats,
    order=4
)
PresetTrainingExercise.objects.create(
    calculate_in = squats.calculate_in,
    required_value = 16,
    level = TrainingLevel.BEGINNER,
    belong_to_training_set = prest_training_set["prest_leg_beginner"],
    exercise = squats,
    order=5
)


PresetTrainingExercise.objects.create(
    calculate_in = jumping_jack.calculate_in,
    required_value = 30,
    level = TrainingLevel.BEGINNER,
    belong_to_training_set = prest_training_set["prest_back_and_shoulder_beginner"],
    exercise = jumping_jack,
    order=1
)
PresetTrainingExercise.objects.create(
    calculate_in = jumping_jack.calculate_in,
    required_value = 30,
    level = TrainingLevel.BEGINNER,
    belong_to_training_set = prest_training_set["prest_back_and_shoulder_beginner"],
    exercise = jumping_jack,
    order=2
)
PresetTrainingExercise.objects.create(
    calculate_in = jumping_jack.calculate_in,
    required_value = 30,
    level = TrainingLevel.BEGINNER,
    belong_to_training_set = prest_training_set["prest_back_and_shoulder_beginner"],
    exercise = jumping_jack,
    order=3
)
PresetTrainingExercise.objects.create(
    calculate_in = arm_raise.calculate_in,
    required_value = 16,
    level = TrainingLevel.BEGINNER,
    belong_to_training_set = prest_training_set["prest_back_and_shoulder_beginner"],
    exercise = arm_raise,
    order=4
)
PresetTrainingExercise.objects.create(
    calculate_in = arm_raise.calculate_in,
    required_value = 16,
    level = TrainingLevel.BEGINNER,
    belong_to_training_set = prest_training_set["prest_back_and_shoulder_beginner"],
    exercise = arm_raise,
    order=5
)


# intermediate preset exercise
PresetTrainingExercise.objects.create(
    calculate_in = jumping_jack.calculate_in,
    required_value = 40,
    level = TrainingLevel.INTERMEDIATE,
    belong_to_training_set = prest_training_set['prest_abs_intermediate'],
    exercise = jumping_jack,
    order=1
)
PresetTrainingExercise.objects.create(
    calculate_in = jumping_jack.calculate_in,
    required_value = 40,
    level = TrainingLevel.INTERMEDIATE,
    belong_to_training_set = prest_training_set['prest_abs_intermediate'],
    exercise = jumping_jack,
    order=2
)
PresetTrainingExercise.objects.create(
    calculate_in = jumping_jack.calculate_in,
    required_value = 40,
    level = TrainingLevel.INTERMEDIATE,
    belong_to_training_set = prest_training_set['prest_abs_intermediate'],
    exercise = jumping_jack,
    order=3
)
PresetTrainingExercise.objects.create(
    calculate_in = abdominal_crunches.calculate_in,
    required_value = 20,
    level = TrainingLevel.INTERMEDIATE,
    belong_to_training_set = prest_training_set['prest_abs_intermediate'],
    exercise = abdominal_crunches,
    order=4
)
PresetTrainingExercise.objects.create(
    calculate_in = abdominal_crunches.calculate_in,
    required_value = 20,
    level = TrainingLevel.INTERMEDIATE,
    belong_to_training_set = prest_training_set['prest_abs_intermediate'],
    exercise = abdominal_crunches,
    order=5
)


PresetTrainingExercise.objects.create(
    calculate_in = jumping_jack.calculate_in,
    required_value = 25,
    level = TrainingLevel.INTERMEDIATE,
    belong_to_training_set = prest_training_set["prest_chest_intermediate"],
    exercise = jumping_jack,
    order=1
)
PresetTrainingExercise.objects.create(
    calculate_in = jumping_jack.calculate_in,
    required_value = 25,
    level = TrainingLevel.INTERMEDIATE,
    belong_to_training_set = prest_training_set["prest_chest_intermediate"],
    exercise = jumping_jack,
    order=2
)
PresetTrainingExercise.objects.create(
    calculate_in = jumping_jack.calculate_in,
    required_value = 25,
    level = TrainingLevel.INTERMEDIATE,
    belong_to_training_set = prest_training_set["prest_chest_intermediate"],
    exercise = jumping_jack,
    order=3
)
PresetTrainingExercise.objects.create(
    calculate_in = incline_push.calculate_in,
    required_value = 18,
    level = TrainingLevel.INTERMEDIATE,
    belong_to_training_set = prest_training_set["prest_chest_intermediate"],
    exercise = incline_push,
    order=4
)
PresetTrainingExercise.objects.create(
    calculate_in = incline_push.calculate_in,
    required_value = 18,
    level = TrainingLevel.INTERMEDIATE,
    belong_to_training_set = prest_training_set["prest_chest_intermediate"],
    exercise = incline_push,
    order=5
)


PresetTrainingExercise.objects.create(
    calculate_in = arm_raise.calculate_in,
    required_value = 35,
    level = TrainingLevel.INTERMEDIATE,
    belong_to_training_set = prest_training_set["prest_arm_intermediate"],
    exercise = arm_raise,
    order=1
)
PresetTrainingExercise.objects.create(
    calculate_in = arm_raise.calculate_in,
    required_value = 35,
    level = TrainingLevel.INTERMEDIATE,
    belong_to_training_set = prest_training_set["prest_arm_intermediate"],
    exercise = arm_raise,
    order=2
)
PresetTrainingExercise.objects.create(
    calculate_in = arm_raise.calculate_in,
    required_value = 35,
    level = TrainingLevel.INTERMEDIATE,
    belong_to_training_set = prest_training_set["prest_arm_intermediate"],
    exercise = arm_raise,
    order=3
)
PresetTrainingExercise.objects.create(
    calculate_in = side_arm_raise.calculate_in,
    required_value = 35,
    level = TrainingLevel.INTERMEDIATE,
    belong_to_training_set = prest_training_set["prest_arm_intermediate"],
    exercise = side_arm_raise,
    order=4
)
PresetTrainingExercise.objects.create(
    calculate_in = side_arm_raise.calculate_in,
    required_value = 35,
    level = TrainingLevel.INTERMEDIATE,
    belong_to_training_set = prest_training_set["prest_arm_intermediate"],
    exercise = side_arm_raise,
    order=5
)


PresetTrainingExercise.objects.create(
    calculate_in = side_hop.calculate_in,
    required_value = 28,
    level = TrainingLevel.INTERMEDIATE,
    belong_to_training_set = prest_training_set["prest_leg_intermediate"],
    exercise = side_hop,
    order=1
)
PresetTrainingExercise.objects.create(
    calculate_in = side_hop.calculate_in,
    required_value = 28,
    level = TrainingLevel.INTERMEDIATE,
    belong_to_training_set = prest_training_set["prest_leg_intermediate"],
    exercise = side_hop,
    order=2
)
PresetTrainingExercise.objects.create(
    calculate_in = side_hop.calculate_in,
    required_value = 28,
    level = TrainingLevel.INTERMEDIATE,
    belong_to_training_set = prest_training_set["prest_leg_intermediate"],
    exercise = side_hop,
    order=3
)
PresetTrainingExercise.objects.create(
    calculate_in = squats.calculate_in,
    required_value = 22,
    level = TrainingLevel.INTERMEDIATE,
    belong_to_training_set = prest_training_set["prest_leg_intermediate"],
    exercise = squats,
    order=4
)
PresetTrainingExercise.objects.create(
    calculate_in = squats.calculate_in,
    required_value = 22,
    level = TrainingLevel.INTERMEDIATE,
    belong_to_training_set = prest_training_set["prest_leg_intermediate"],
    exercise = squats,
    order=5
)


PresetTrainingExercise.objects.create(
    calculate_in = jumping_jack.calculate_in,
    required_value = 30,
    level = TrainingLevel.INTERMEDIATE,
    belong_to_training_set = prest_training_set["prest_back_and_shoulder_intermediate"],
    exercise = jumping_jack,
    order=1
)
PresetTrainingExercise.objects.create(
    calculate_in = jumping_jack.calculate_in,
    required_value = 30,
    level = TrainingLevel.INTERMEDIATE,
    belong_to_training_set = prest_training_set["prest_back_and_shoulder_intermediate"],
    exercise = jumping_jack,
    order=2
)
PresetTrainingExercise.objects.create(
    calculate_in = jumping_jack.calculate_in,
    required_value = 30,
    level = TrainingLevel.INTERMEDIATE,
    belong_to_training_set = prest_training_set["prest_back_and_shoulder_intermediate"],
    exercise = jumping_jack,
    order=3
)
PresetTrainingExercise.objects.create(
    calculate_in = arm_raise.calculate_in,
    required_value = 22,
    level = TrainingLevel.INTERMEDIATE,
    belong_to_training_set = prest_training_set["prest_back_and_shoulder_intermediate"],
    exercise = arm_raise,
    order=4
)
PresetTrainingExercise.objects.create(
    calculate_in = arm_raise.calculate_in,
    required_value = 22,
    level = TrainingLevel.INTERMEDIATE,
    belong_to_training_set = prest_training_set["prest_back_and_shoulder_intermediate"],
    exercise = arm_raise,
    order=5
)



# advance preset exercise
PresetTrainingExercise.objects.create(
    calculate_in = jumping_jack.calculate_in,
    required_value = 40,
    level = TrainingLevel.ADVANCE,
    belong_to_training_set = prest_training_set['prest_abs_advance'],
    exercise = jumping_jack,
    order=1
)
PresetTrainingExercise.objects.create(
    calculate_in = jumping_jack.calculate_in,
    required_value = 40,
    level = TrainingLevel.ADVANCE,
    belong_to_training_set = prest_training_set['prest_abs_advance'],
    exercise = jumping_jack,
    order=2
)
PresetTrainingExercise.objects.create(
    calculate_in = jumping_jack.calculate_in,
    required_value = 40,
    level = TrainingLevel.ADVANCE,
    belong_to_training_set = prest_training_set['prest_abs_advance'],
    exercise = jumping_jack,
    order=3
)
PresetTrainingExercise.objects.create(
    calculate_in = abdominal_crunches.calculate_in,
    required_value = 20,
    level = TrainingLevel.ADVANCE,
    belong_to_training_set = prest_training_set['prest_abs_advance'],
    exercise = abdominal_crunches,
    order=4
)
PresetTrainingExercise.objects.create(
    calculate_in = abdominal_crunches.calculate_in,
    required_value = 20,
    level = TrainingLevel.ADVANCE,
    belong_to_training_set = prest_training_set['prest_abs_advance'],
    exercise = abdominal_crunches,
    order=5
)


PresetTrainingExercise.objects.create(
    calculate_in = jumping_jack.calculate_in,
    required_value = 25,
    level = TrainingLevel.ADVANCE,
    belong_to_training_set = prest_training_set["prest_chest_advance"],
    exercise = jumping_jack,
    order=1
)
PresetTrainingExercise.objects.create(
    calculate_in = jumping_jack.calculate_in,
    required_value = 25,
    level = TrainingLevel.ADVANCE,
    belong_to_training_set = prest_training_set["prest_chest_advance"],
    exercise = jumping_jack,
    order=2
)
PresetTrainingExercise.objects.create(
    calculate_in = jumping_jack.calculate_in,
    required_value = 25,
    level = TrainingLevel.ADVANCE,
    belong_to_training_set = prest_training_set["prest_chest_advance"],
    exercise = jumping_jack,
    order=3
)
PresetTrainingExercise.objects.create(
    calculate_in = incline_push.calculate_in,
    required_value = 18,
    level = TrainingLevel.ADVANCE,
    belong_to_training_set = prest_training_set["prest_chest_advance"],
    exercise = incline_push,
    order=4
)
PresetTrainingExercise.objects.create(
    calculate_in = incline_push.calculate_in,
    required_value = 18,
    level = TrainingLevel.ADVANCE,
    belong_to_training_set = prest_training_set["prest_chest_advance"],
    exercise = incline_push,
    order=5
)


PresetTrainingExercise.objects.create(
    calculate_in = arm_raise.calculate_in,
    required_value = 35,
    level = TrainingLevel.ADVANCE,
    belong_to_training_set = prest_training_set["prest_arm_advance"],
    exercise = arm_raise,
    order=1
)
PresetTrainingExercise.objects.create(
    calculate_in = arm_raise.calculate_in,
    required_value = 35,
    level = TrainingLevel.ADVANCE,
    belong_to_training_set = prest_training_set["prest_arm_advance"],
    exercise = arm_raise,
    order=2
)
PresetTrainingExercise.objects.create(
    calculate_in = arm_raise.calculate_in,
    required_value = 35,
    level = TrainingLevel.ADVANCE,
    belong_to_training_set = prest_training_set["prest_arm_advance"],
    exercise = arm_raise,
    order=3
)
PresetTrainingExercise.objects.create(
    calculate_in = side_arm_raise.calculate_in,
    required_value = 35,
    level = TrainingLevel.ADVANCE,
    belong_to_training_set = prest_training_set["prest_arm_advance"],
    exercise = side_arm_raise,
    order=4
)
PresetTrainingExercise.objects.create(
    calculate_in = side_arm_raise.calculate_in,
    required_value = 35,
    level = TrainingLevel.ADVANCE,
    belong_to_training_set = prest_training_set["prest_arm_advance"],
    exercise = side_arm_raise,
    order=5
)


PresetTrainingExercise.objects.create(
    calculate_in = side_hop.calculate_in,
    required_value = 28,
    level = TrainingLevel.ADVANCE,
    belong_to_training_set = prest_training_set["prest_leg_advance"],
    exercise = side_hop,
    order=1
)
PresetTrainingExercise.objects.create(
    calculate_in = side_hop.calculate_in,
    required_value = 28,
    level = TrainingLevel.ADVANCE,
    belong_to_training_set = prest_training_set["prest_leg_advance"],
    exercise = side_hop,
    order=2
)
PresetTrainingExercise.objects.create(
    calculate_in = side_hop.calculate_in,
    required_value = 28,
    level = TrainingLevel.ADVANCE,
    belong_to_training_set = prest_training_set["prest_leg_advance"],
    exercise = side_hop,
    order=3
)
PresetTrainingExercise.objects.create(
    calculate_in = squats.calculate_in,
    required_value = 22,
    level = TrainingLevel.ADVANCE,
    belong_to_training_set = prest_training_set["prest_leg_advance"],
    exercise = squats,
    order=4
)
PresetTrainingExercise.objects.create(
    calculate_in = squats.calculate_in,
    required_value = 22,
    level = TrainingLevel.ADVANCE,
    belong_to_training_set = prest_training_set["prest_leg_advance"],
    exercise = squats,
    order=5
)


PresetTrainingExercise.objects.create(
    calculate_in = jumping_jack.calculate_in,
    required_value = 30,
    level = TrainingLevel.ADVANCE,
    belong_to_training_set = prest_training_set["prest_back_and_shoulder_advance"],
    exercise = jumping_jack,
    order=1
)
PresetTrainingExercise.objects.create(
    calculate_in = jumping_jack.calculate_in,
    required_value = 30,
    level = TrainingLevel.ADVANCE,
    belong_to_training_set = prest_training_set["prest_back_and_shoulder_advance"],
    exercise = jumping_jack,
    order=2
)
PresetTrainingExercise.objects.create(
    calculate_in = jumping_jack.calculate_in,
    required_value = 30,
    level = TrainingLevel.ADVANCE,
    belong_to_training_set = prest_training_set["prest_back_and_shoulder_advance"],
    exercise = jumping_jack,
    order=3
)
PresetTrainingExercise.objects.create(
    calculate_in = arm_raise.calculate_in,
    required_value = 22,
    level = TrainingLevel.ADVANCE,
    belong_to_training_set = prest_training_set["prest_back_and_shoulder_advance"],
    exercise = arm_raise,
    order=4
)
PresetTrainingExercise.objects.create(
    calculate_in = arm_raise.calculate_in,
    required_value = 22,
    level = TrainingLevel.ADVANCE,
    belong_to_training_set = prest_training_set["prest_back_and_shoulder_advance"],
    exercise = arm_raise,
    order=5
)