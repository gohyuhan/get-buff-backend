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
        image_url = "https://res.cloudinary.com/dmoa45uta/image/upload/q_auto:best/f_auto/v1702721592/gotBuff/training5_cnfopd.jpg"
    ),
    "legs":MuscleCategory.objects.create(
        name = 'legs',
        type = MuscleGroup.LEGS,
        image_url = "https://res.cloudinary.com/dmoa45uta/image/upload/q_auto:best/f_auto/v1702721590/gotBuff/training3_kctynn.jpg"
    ),
    "chest":MuscleCategory.objects.create(
        name = 'chest',
        type = MuscleGroup.CHEST,
        image_url = "https://res.cloudinary.com/dmoa45uta/image/upload/q_auto:best/f_auto/v1702721590/gotBuff/training2_ooqiv0.jpg"
    ),
    "arms":MuscleCategory.objects.create(
        name = 'arms',
        type = MuscleGroup.ARMS,
        image_url = "https://res.cloudinary.com/dmoa45uta/image/upload/q_auto:best/f_auto/v1702721591/gotBuff/training4_ttkpc6.jpg"
    ),
    "back_and_shoulder":MuscleCategory.objects.create(
        name = 'back and shoulder',
        type = MuscleGroup.BACKNSHOULDER,
        image_url = "https://res.cloudinary.com/dmoa45uta/image/upload/q_auto:best/f_auto/v1702721589/gotBuff/training1_roolxg.jpg"
    ),
}

muscle={
    "shoulders":Muscle.objects.create(
        name = "Shoulder",
        front_image_url = "https://res.cloudinary.com/dmoa45uta/image/upload/q_auto:best/f_auto/v1702096178/gotBuff/front_muscle/shoulder_qgiv1v.png",
        back_image_url = "https://res.cloudinary.com/dmoa45uta/image/upload/q_auto:best/f_auto/v1702096210/gotBuff/back_muscle/shoulder_pfdvzo.png",
        muscle_category = muscle_cat['back_and_shoulder']
    ),
    "quadriceps":Muscle.objects.create(
        name = "Quadriceps",
        front_image_url = "https://res.cloudinary.com/dmoa45uta/image/upload/q_auto:best/f_auto/v1702096178/gotBuff/front_muscle/quadriceps_k5dd3k.png",
        back_image_url = "",
        muscle_category = muscle_cat['legs']
    ),
    "adductors":Muscle.objects.create(
        name = "Adductors",
        front_image_url = "https://res.cloudinary.com/dmoa45uta/image/upload/q_auto:best/f_auto/v1702096187/gotBuff/front_muscle/adductors_qzgbvn.png",
        back_image_url = "",
        muscle_category = muscle_cat['legs']
    ),
    "calves":Muscle.objects.create(
        name = "Calves",
        front_image_url = "https://res.cloudinary.com/dmoa45uta/image/upload/q_auto:best/f_auto/v1702096188/gotBuff/front_muscle/calves_c93tid.png",
        back_image_url = "https://res.cloudinary.com/dmoa45uta/image/upload/q_auto:best/f_auto/v1702096228/gotBuff/back_muscle/calves_iks153.png",
        muscle_category = muscle_cat['legs']
    ),
    "chest":Muscle.objects.create(
        name = "Chest",
        front_image_url = "https://res.cloudinary.com/dmoa45uta/image/upload/q_auto:best/f_auto/v1702096189/gotBuff/front_muscle/chest_bbarf5.png",
        back_image_url = "",
        muscle_category = muscle_cat['chest']
    ),
    "abs":Muscle.objects.create(
        name = "abs",
        front_image_url = "https://res.cloudinary.com/dmoa45uta/image/upload/q_auto:best/f_auto/v1702096187/gotBuff/front_muscle/abs_g05kvf.png",
        back_image_url = "https://res.cloudinary.com/dmoa45uta/image/upload/q_auto:best/f_auto/v1702096227/gotBuff/back_muscle/abs_eki5ks.png",
        muscle_category = muscle_cat['abs']
    ),
    "traps":Muscle.objects.create(
        name = "Traps",
        front_image_url = "https://res.cloudinary.com/dmoa45uta/image/upload/q_auto:best/f_auto/v1702096178/gotBuff/front_muscle/traps_hfpg03.png",
        back_image_url = "https://res.cloudinary.com/dmoa45uta/image/upload/q_auto:best/f_auto/v1702096210/gotBuff/back_muscle/traps_wtvvpn.png",
        muscle_category = muscle_cat['back_and_shoulder']
    ),
    "biceps":Muscle.objects.create(
        name = "Biceps",
        front_image_url = "https://res.cloudinary.com/dmoa45uta/image/upload/q_auto:best/f_auto/v1702096188/gotBuff/front_muscle/biceps_d8tm5x.png",
        back_image_url = "",
        muscle_category = muscle_cat['arms']
    ),
    "forearms":Muscle.objects.create(
        name = "Forearms",
        front_image_url = "https://res.cloudinary.com/dmoa45uta/image/upload/q_auto:best/f_auto/v1702096189/gotBuff/front_muscle/forearm_ctwhlr.png",
        back_image_url = "https://res.cloudinary.com/dmoa45uta/image/upload/q_auto:best/f_auto/v1702096229/gotBuff/back_muscle/forearm_oigbse.png",
        muscle_category = muscle_cat['arms']
    ),
    "glutes":Muscle.objects.create(
        name = "Glutes",
        front_image_url = "",
        back_image_url = "https://res.cloudinary.com/dmoa45uta/image/upload/q_auto:best/f_auto/v1702103841/gotBuff/back_muscle/glutes_p55x0j.png",
        muscle_category = muscle_cat['legs']
    ),
    "hamstrings":Muscle.objects.create(
        name = "Hamstrings",
        front_image_url = "",
        back_image_url = "https://res.cloudinary.com/dmoa45uta/image/upload/q_auto:best/f_auto/v1702096230/gotBuff/back_muscle/hamstrings_i107aa.png",
        muscle_category = muscle_cat['legs']
    ),
    "triceps":Muscle.objects.create(
        name = "Triceps",
        front_image_url = "",
        back_image_url = "https://res.cloudinary.com/dmoa45uta/image/upload/q_auto:best/f_auto/v1702096211/gotBuff/back_muscle/triceps_jv9uop.png",
        muscle_category = muscle_cat['arms']
    ),
    "back":Muscle.objects.create(
        name = "Back",
        front_image_url = "",
        back_image_url = "https://res.cloudinary.com/dmoa45uta/image/upload/q_auto:best/f_auto/v1702096227/gotBuff/back_muscle/back_mpebeq.png",
        muscle_category = muscle_cat["back_and_shoulder"]
    ),
}

preset_training_set={
    'preset_abs_beginner':PresetTrainingSet.objects.create(
        name = "ABS BEGINNER",
        level = TrainingLevel.BEGINNER,
        muscle_category = muscle_cat['abs']
    ),
    'preset_chest_beginner':PresetTrainingSet.objects.create(
        name = "CHEST BEGINNER",
        level = TrainingLevel.BEGINNER,
        muscle_category = muscle_cat['chest']
    ),
    'preset_leg_beginner':PresetTrainingSet.objects.create(
        name = "LEG BEGINNER",
        level = TrainingLevel.BEGINNER,
        muscle_category = muscle_cat['legs']
    ),
    'preset_arm_beginner':PresetTrainingSet.objects.create(
        name = "ARM BEGINNER",
        level = TrainingLevel.BEGINNER,
        muscle_category = muscle_cat['arms']
    ),
    'preset_back_and_shoulder_beginner':PresetTrainingSet.objects.create(
        name = "BACK & SHOULDER BEGINNER",
        level = TrainingLevel.BEGINNER,
        muscle_category = muscle_cat["back_and_shoulder"]
    ),
    'preset_abs_intermediate':PresetTrainingSet.objects.create(
        name = "ABS INTERMEDIATE",
        level = TrainingLevel.INTERMEDIATE,
        muscle_category = muscle_cat['abs']
    ),
    'preset_chest_intermediate':PresetTrainingSet.objects.create(
        name = "CHEST INTERMEDIATE",
        level = TrainingLevel.INTERMEDIATE,
        muscle_category = muscle_cat['chest']
    ),
    'preset_leg_intermediate':PresetTrainingSet.objects.create(
        name = "LEG INTERMEDIATE",
        level = TrainingLevel.INTERMEDIATE,
        muscle_category = muscle_cat['legs']
    ),
    'preset_arm_intermediate':PresetTrainingSet.objects.create(
        name = "ARM INTERMEDIATE",
        level = TrainingLevel.INTERMEDIATE,
        muscle_category = muscle_cat['arms']
    ),
    'preset_back_and_shoulder_intermediate':PresetTrainingSet.objects.create(
        name = "BACK & SHOULDER INTERMEDIATE",
        level = TrainingLevel.INTERMEDIATE,
        muscle_category = muscle_cat["back_and_shoulder"]
    ),
    'preset_abs_advance':PresetTrainingSet.objects.create(
        name = "ABS ADVANCE",
        level = TrainingLevel.ADVANCE,
        muscle_category = muscle_cat['abs']
    ),
    'preset_chest_advance':PresetTrainingSet.objects.create(
        name = "CHEST ADVANCE",
        level = TrainingLevel.ADVANCE,
        muscle_category = muscle_cat['chest']
    ),
    'preset_leg_advance':PresetTrainingSet.objects.create(
        name = "LEG ADVANCE",
        level = TrainingLevel.ADVANCE,
        muscle_category = muscle_cat['legs']
    ),
    'preset_arm_advance':PresetTrainingSet.objects.create(
        name = "ARM ADVANCE",
        level = TrainingLevel.ADVANCE,
        muscle_category = muscle_cat['arms']
    ),
    'preset_back_and_shoulder_advance':PresetTrainingSet.objects.create(
        name = "BACK & SHOULDER ADVANCE",
        level = TrainingLevel.ADVANCE,
        muscle_category = muscle_cat["back_and_shoulder"]
    )
}

jumping_jack = Exercise.objects.create(
    name = 'JUMPING JACKS',
    explanation = "<p>Start with your feet together and your arms by your sides, then jump up with your feet apart and your hands overhead.</p> <p>Return to the start position then do the next rep. This exercise provides a full-body workout and works all your large muscle groups.</p>",
    calculate_in = CalculatedIn.SECONDS,
    animation = "",
    min_count = 0
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
    explanation = "<p>Lie on your back with your knees bent and your arms stretched forward.</p>  <p>Then lift your upper body off the floor. Hold for a few seconds and slowly return.</p> <p>It primarily works the rectus abdominis muscle and the obliques.</p>",
    calculate_in = CalculatedIn.REPS,
    animation = "",
    min_count = 0
)
abdominal_crunches.muscle_category.add(muscle_cat["abs"])
abdominal_crunches.muscle.add(muscle["abs"])
abdominal_crunches.save()

russian_twist = Exercise.objects.create(
    name = 'RUSSIAN TWISTS',
    explanation = "<p>Sit on the floor with your knees bent, feet lifted a little bit and back tilted backwards.</p>  <p>Then hold your hands together and twist from side to side.</p>",
    calculate_in = CalculatedIn.REPS,
    animation = "",
    min_count = 0
)
russian_twist.muscle_category.add(muscle_cat["abs"])
russian_twist.muscle.add(muscle["abs"])
russian_twist.save()

mountain_climber = Exercise.objects.create(
    name = 'MOUNTAIN CLIMBER',
    explanation = "<p>Start in the push-up position. Bend your right knees towards your left chest and keep your left leg straight, then quickly switch from one leg to yhe other.</p> <p>This exercise strengthens muscle groups.</p>",
    calculate_in = CalculatedIn.REPS,
    animation = "",
    min_count = 0
)
mountain_climber.muscle_category.add(muscle_cat["back_and_shoulder"])
mountain_climber.muscle_category.add(muscle_cat['abs'])
mountain_climber.muscle_category.add(muscle_cat['legs'])
mountain_climber.muscle.add(muscle["back"])
mountain_climber.muscle.add(muscle["quadriceps"])
mountain_climber.muscle.add(muscle["glutes"])
mountain_climber.muscle.add(muscle["calves"])
mountain_climber.muscle.add(muscle["abs"])
mountain_climber.save()

heel_touch = Exercise.objects.create(
    name = 'HEEL TOUCH',
    explanation = "<p>Lie on the ground with your legsbent and your arms by your sides.</p>  <p>Slightly lift your upper body off the floor and make sure your hands alternately reach your heels.</p>",
    calculate_in = CalculatedIn.SECONDS,
    animation = "",
    min_count = 0
)
heel_touch.muscle_category.add(muscle_cat["abs"])
heel_touch.muscle.add(muscle["abs"])
heel_touch.save()

leg_raises = Exercise.objects.create(
    name = 'LEG RAISES',
    explanation = "<p>Lie down on your back, and put your hands beneath your hips for support.</p>  <p>Then lift your legs up until they form a right angle with the floor.</p> <p>Slowly bring your legs back down and repest the exercise.</p>",
    calculate_in = CalculatedIn.REPS,
    animation = "",
    min_count = 0
)
leg_raises.muscle_category.add(muscle_cat['abs'])
leg_raises.muscle_category.add(muscle_cat['legs'])
leg_raises.muscle.add(muscle["quadriceps"])
leg_raises.muscle.add(muscle["glutes"])
leg_raises.muscle.add(muscle["abs"])
leg_raises.save()

plank = Exercise.objects.create(
    name = 'PLANK',
    explanation = "<p>Lie on the floor with your toes and forearms on the ground. keep your body straight and hold this position as long as you can.</p>  <p>Don't hold your breath. Breathe normally from your abdomen instead of your chest</p> <p>This exercise strengthens the abdome, back and shoulders.</p>",
    calculate_in = CalculatedIn.SECONDS,
    animation = "",
    min_count = 0
)
plank.muscle_category.add(muscle_cat['abs'])
plank.muscle_category.add(muscle_cat['legs'])
plank.muscle_category.add(muscle_cat['back_and_shoulder'])
plank.muscle.add(muscle["shoulders"])
plank.muscle.add(muscle["glutes"])
plank.muscle.add(muscle["abs"])
plank.save()

cobra_stretch = Exercise.objects.create(
    name = 'COBRA STRETCH',
    explanation = "<p>Lie down on your stomach and bend your elbows with your hands beneath your shoulders.</p>  <p>Then push your chest up off the ground as far as possible. Hold this position for seconds.</p>",
    calculate_in = CalculatedIn.SECONDS,
    animation = "",
    min_count = 0
)
cobra_stretch.muscle_category.add(muscle_cat['abs'])
cobra_stretch.muscle_category.add(muscle_cat['legs'])
cobra_stretch.muscle_category.add(muscle_cat['back_and_shoulder'])
cobra_stretch.muscle.add(muscle['back'])
cobra_stretch.muscle.add(muscle['hamstrings'])
cobra_stretch.muscle.add(muscle["glutes"])
cobra_stretch.muscle.add(muscle["abs"])
cobra_stretch.save()

bent_leg_twist = Exercise.objects.create(
    name = 'BENT LEG TWIST',
    explanation = "<p>Lie on your back with your knees up at a 90 degree angle.</p>  <p>Extend your arms to the sides and put your palms down to the ground.</p> <p>Twists your legs to the left while keeping your upper body in place and your knees and feet together.</p> <p>Hold it for one second, then return and twist to the other side. Repeat the exercise.</p>",
    calculate_in = CalculatedIn.REPS,
    animation = "",
    min_count = 0
)
bent_leg_twist.muscle_category.add(muscle_cat['abs'])
bent_leg_twist.muscle.add(muscle["abs"])
bent_leg_twist.save()

bent_leg_twist = Exercise.objects.create(
    name = 'BENT LEG TWIST',
    explanation = "<p>Lie on your back with your knees up at a 90 degree angle.</p>  <p>Extend your arms to the sides and put your palms down to the ground.</p> <p>Twists your legs to the left while keeping your upper body in place and your knees and feet together.</p> <p>Hold it for one second, then return and twist to the other side. Repeat the exercise.</p>",
    calculate_in = CalculatedIn.REPS,
    animation = "",
    min_count = 0
)
bent_leg_twist.muscle_category.add(muscle_cat['abs'])
bent_leg_twist.muscle.add(muscle["abs"])
bent_leg_twist.save()

burpees = Exercise.objects.create(
    name = 'BURPEES',
    explanation = "<p>Stand with your feet together width apart, then put your hands on the ground and kick your feet backwards. Do a quick push-up and then jump up.</p>",
    calculate_in = CalculatedIn.SECONDS,
    animation = "",
    min_count = 0
)
burpees.muscle_category.add(muscle_cat['back_and_shoulder'])
burpees.muscle_category.add(muscle_cat['arms'])
burpees.muscle_category.add(muscle_cat['legs'])
burpees.muscle_category.add(muscle_cat['abs'])
burpees.muscle_category.add(muscle_cat['chest'])
burpees.muscle.add(muscle['chest'])
burpees.muscle.add(muscle['abs'])
burpees.muscle.add(muscle['quadriceps'])
burpees.muscle.add(muscle["glutes"])
burpees.muscle.add(muscle['hamstrings'])
burpees.muscle.add(muscle['shoulders'])
burpees.muscle.add(muscle['triceps'])
burpees.muscle.add(muscle['calves'])
burpees.save()

push_up = Exercise.objects.create(
    name = 'PUSH-UPS',
    explanation = "<p>Keep your body straight while raising and lowering your body with your arms.</p> <p>This exercise works the chest, shoulders, triceps, back and legs</p>",
    calculate_in = CalculatedIn.REPS,
    animation = "",
    min_count = 0
)
push_up.muscle_category.add(muscle_cat['back_and_shoulder'])
push_up.muscle_category.add(muscle_cat['arms'])
push_up.muscle_category.add(muscle_cat['chest'])
push_up.muscle.add(muscle['chest'])
push_up.muscle.add(muscle['shoulders'])
push_up.muscle.add(muscle['triceps'])
push_up.save()

wide_push_up = Exercise.objects.create(
    name = 'WIDE ARM PUSH-UPS',
    explanation = "<p>Start in the regular push-up position but with your hands spread wider than your shoulders.</p> <p>Then push your body up and down, Remember to keep your body straight</p>",
    calculate_in = CalculatedIn.REPS,
    animation = "",
    min_count = 0
)
wide_push_up.muscle_category.add(muscle_cat['back_and_shoulder'])
wide_push_up.muscle_category.add(muscle_cat['arms'])
wide_push_up.muscle_category.add(muscle_cat['chest'])
wide_push_up.muscle.add(muscle['chest'])
wide_push_up.muscle.add(muscle['shoulders'])
wide_push_up.muscle.add(muscle['triceps'])
wide_push_up.save()

triceps_dips = Exercise.objects.create(
    name = 'TRICEPS DIPS',
    explanation = "<p>For the start position, sit on the chair. Then move your hip off the chair with your hands holding the edge of the chair.</p> <p>Slowly bend and stretch your arms to make your body go up and down. This is a great exercise for the triceps.</p>",
    calculate_in = CalculatedIn.REPS,
    animation = "",
    min_count = 0
)
triceps_dips.muscle_category.add(muscle_cat['back_and_shoulder'])
triceps_dips.muscle_category.add(muscle_cat['arms'])
triceps_dips.muscle_category.add(muscle_cat['chest'])
triceps_dips.muscle.add(muscle['chest'])
triceps_dips.muscle.add(muscle['shoulders'])
triceps_dips.muscle.add(muscle['triceps'])
triceps_dips.muscle.add(muscle['back'])
triceps_dips.save()

knee_push_up = Exercise.objects.create(
    name = 'KNEE PUSH-UPS',
    explanation = "<p>Start in the regular push-up position, then let your knees touch the floor and raise your feet up off the floor. next push your body up and down</p> <p>Next push your body up and down.</p>",
    calculate_in = CalculatedIn.REPS,
    animation = "",
    min_count = 0
)
knee_push_up.muscle_category.add(muscle_cat['back_and_shoulder'])
knee_push_up.muscle_category.add(muscle_cat['arms'])
knee_push_up.muscle_category.add(muscle_cat['chest'])
knee_push_up.muscle.add(muscle['chest'])
knee_push_up.muscle.add(muscle['shoulders'])
knee_push_up.muscle.add(muscle['triceps'])
knee_push_up.save()

chest_stretch = Exercise.objects.create(
    name = 'CHEST STRETCH',
    explanation = "<p>Find a corner, place your hands on each wall and keep your arms straight, then slowly bring your chest forward.</p> <p>Hold this position for a while. Then slowly come out of it, bring your arms down and do a couple of shoulder rolls.</p> <p>Don't pull your head forward, and keep your neck relaxed.</p>",
    calculate_in = CalculatedIn.SECONDS,
    animation = "",
    min_count = 0
)
chest_stretch.muscle_category.add(muscle_cat['back_and_shoulder'])
chest_stretch.muscle_category.add(muscle_cat['arms'])
chest_stretch.muscle_category.add(muscle_cat['chest'])
chest_stretch.muscle.add(muscle['chest'])
chest_stretch.muscle.add(muscle['shoulders'])
chest_stretch.muscle.add(muscle['back'])
chest_stretch.muscle.add(muscle['biceps'])
chest_stretch.save()

arm_scissors = Exercise.objects.create(
    name = 'ARM SCISSORS',
    explanation = "<p>Stand upright with your feet shoulder width apart.</p> <p>Stretch your arms in front of you at shoulder height with one arm overlap the other in the shape of the letter 'X', and then spread apart.</p> <p>Switch arms, and repeat the exercise.</p>",
    calculate_in = CalculatedIn.SECONDS,
    animation = "",
    min_count = 0
)
arm_scissors.muscle_category.add(muscle_cat['back_and_shoulder'])
arm_scissors.muscle_category.add(muscle_cat['chest'])
arm_scissors.muscle.add(muscle['chest'])
arm_scissors.muscle.add(muscle['shoulders'])
arm_scissors.save()

side_arm_raise = Exercise.objects.create(
    name = 'SIDE ARM RAISE',
    explanation = "<p>Stand with your feet and shoulder width apart.</p> <p>Raise your arms to the sides at the shoulder height, then put them down.</p> <p>Repeat the exercise. Keep yourr arms straight during exercise.</p>",
    calculate_in = CalculatedIn.SECONDS,
    animation = "",
    min_count = 0
)
side_arm_raise.muscle_category.add(muscle_cat['back_and_shoulder'])
side_arm_raise.muscle.add(muscle['shoulders'])
side_arm_raise.save()

arm_circle = Exercise.objects.create(
    name = 'ARM CIRCLE',
    explanation = "<p>Stand on the floor with your arms extended straight out to the sides at shoulder height.</p> <p>Move your arms cloclwise in circles fast.</p> <p>Try to do it as fast as you can.</p> <p>It's a great exercise for deltoid muscle.</p>",
    calculate_in = CalculatedIn.SECONDS,
    animation = "",
    min_count = 0
)
arm_circle.muscle_category.add(muscle_cat['back_and_shoulder'])
arm_circle.muscle_category.add(muscle_cat['arms'])
arm_circle.muscle.add(muscle['biceps'])
arm_circle.muscle.add(muscle['shoulders'])
arm_circle.save()

diamond_push_up = Exercise.objects.create(
    name = 'DIAMOND PUSH UP',
    explanation = "<p>Stand in the push-up position. Make a diamond shape with your forefingers and thumbs together under your chest.</p> <p>Then push your body up and down. Remember to keep your body straight</p>",
    calculate_in = CalculatedIn.REPS,
    animation = "",
    min_count = 0
)
diamond_push_up.muscle_category.add(muscle_cat['back_and_shoulder'])
diamond_push_up.muscle_category.add(muscle_cat['arms'])
diamond_push_up.muscle_category.add(muscle_cat['chest'])
diamond_push_up.muscle.add(muscle['chest'])
diamond_push_up.muscle.add(muscle['biceps'])
diamond_push_up.muscle.add(muscle['shoulders'])
diamond_push_up.save()

biceps_legs_curl_right = Exercise.objects.create(
    name = 'BICEPS LEGS CURL RIGHT',
    explanation = "<p>Sit down and lift your right leg up. Use your left hand to grab your right leg.</p> <p>Bring your leg towards yourself as much as youcan, then lower it and repeat the exercise</p>",
    calculate_in = CalculatedIn.REPS,
    animation = "",
    min_count = 0
)
biceps_legs_curl_right.muscle_category.add(muscle_cat['arms'])
biceps_legs_curl_right.muscle.add(muscle['forearms'])
biceps_legs_curl_right.muscle.add(muscle['biceps'])
biceps_legs_curl_right.save()

biceps_legs_curl_left = Exercise.objects.create(
    name = 'BICEPS LEGS CURL LEFT',
    explanation = "<p>Sit down and lift your left leg up. Use your right hand to grab your left leg.</p> <p>Bring your leg towards yourself as much as youcan, then lower it and repeat the exercise</p>",
    calculate_in = CalculatedIn.REPS,
    animation = "",
    min_count = 0
)
biceps_legs_curl_left.muscle_category.add(muscle_cat['arms'])
biceps_legs_curl_left.muscle.add(muscle['forearms'])
biceps_legs_curl_left.muscle.add(muscle['biceps'])
biceps_legs_curl_left.save()

diagonal_plank = Exercise.objects.create(
    name = 'DIAGONAL PLANK',
    explanation = "<p>Sit in the straight arm plank position.</p> <p>Lift your right arm and left leg until they are parallel with the ground.</p> <p>Return to the start position and repeat with the other side</p>",
    calculate_in = CalculatedIn.REPS,
    animation = "",
    min_count = 0
)
diagonal_plank.muscle_category.add(muscle_cat['back_and_shoulder'])
diagonal_plank.muscle_category.add(muscle_cat["legs"])
diagonal_plank.muscle_category.add(muscle_cat['abs'])
diagonal_plank.muscle.add(muscle['abs'])
diagonal_plank.muscle.add(muscle['glutes'])
diagonal_plank.muscle.add(muscle['quadriceps'])
diagonal_plank.muscle.add(muscle['hamstrings'])
diagonal_plank.muscle.add(muscle['back'])
diagonal_plank.save()

punches = Exercise.objects.create(
    name = 'PUNCHES',
    explanation = "<p>Stand with one of your legs forward and your knees bent slightly. Bend your elbows and clench your fists in front of you.</p> <p>Extend one arm forward with the palm facing the floor. Take the arm back and repeat with the other arm.</p>",
    calculate_in = CalculatedIn.SECONDS,
    animation = "",
    min_count = 0
)
punches.muscle_category.add(muscle_cat['back_and_shoulder'])
punches.muscle_category.add(muscle_cat['arms'])
punches.muscle_category.add(muscle_cat['chest'])
punches.muscle.add(muscle['shoulders'])
punches.muscle.add(muscle['triceps'])
punches.muscle.add(muscle['chest'])
punches.save()

inchworms = Exercise.objects.create(
    name = 'INCHWORMS',
    explanation = "<p>Start with your feet shoulder width apart.</p> <p>Bend your body and walk your hands in front of you as far as you can, then walk your hands back. Repeat the exercise</p>",
    calculate_in = CalculatedIn.REPS,
    animation = "",
    min_count = 0
)
inchworms.muscle_category.add(muscle_cat['back_and_shoulder'])
inchworms.muscle_category.add(muscle_cat['arms'])
inchworms.muscle_category.add(muscle_cat['chest'])
inchworms.muscle_category.add(muscle_cat['abs'])
inchworms.muscle_category.add(muscle_cat['legs'])
inchworms.muscle.add(muscle['abs'])
inchworms.muscle.add(muscle['chest'])
inchworms.muscle.add(muscle['triceps'])
inchworms.muscle.add(muscle['glutes'])
inchworms.muscle.add(muscle['quadriceps'])
inchworms.muscle.add(muscle['hamstrings'])
inchworms.muscle.add(muscle['traps'])
inchworms.muscle.add(muscle['shoulders'])
inchworms.save()

triceps_stretch_left = Exercise.objects.create(
    name = 'TRICEPS STRETCH LEFT',
    explanation = "<p>Put your left hand on your back, use your right hand to grab your left elbow and gently pull it.</p> <p>Hold this position for a few seconds.</p>",
    calculate_in = CalculatedIn.SECONDS,
    animation = "",
    min_count = 0
)
triceps_stretch_left.muscle_category.add(muscle_cat['back_and_shoulder'])
triceps_stretch_left.muscle_category.add(muscle_cat['arms'])
triceps_stretch_left.muscle.add(muscle['back'])
triceps_stretch_left.muscle.add(muscle['triceps'])
triceps_stretch_left.save()

triceps_stretch_right = Exercise.objects.create(
    name = 'TRICEPS STRETCH RIGHT',
    explanation = "<p>Put your right hand on your back, use your left hand to grab your right elbow and gently pull it.</p> <p>Hold this position for a few seconds.</p>",
    calculate_in = CalculatedIn.SECONDS,
    animation = "",
    min_count = 0
)
triceps_stretch_right.muscle_category.add(muscle_cat['back_and_shoulder'])
triceps_stretch_right.muscle_category.add(muscle_cat['arms'])
triceps_stretch_right.muscle.add(muscle['back'])
triceps_stretch_right.muscle.add(muscle['triceps'])
triceps_stretch_right.save()

jumping_squats = Exercise.objects.create(
    name = 'JUMPING SQUATS',
    explanation = "<p>Start in the squat position, then jump up using your abdominal muscles for strength. This exercise works your abdomen.</p>",
    calculate_in = CalculatedIn.REPS,
    animation = "",
    min_count = 0
)
jumping_squats.muscle_category.add(muscle_cat['legs'])
jumping_squats.muscle.add(muscle['glutes'])
jumping_squats.muscle.add(muscle['quadriceps'])
jumping_squats.muscle.add(muscle['hamstrings'])
jumping_squats.muscle.add(muscle['calves'])
jumping_squats.save()

squats = Exercise.objects.create(
    name = 'SQUATS',
    explanation = "<p>Stand with your feet shoulder width apart and your arms stretched forward, then lower your body until your thighs are parallel with the floor.</p> <p>Your knees should be extended in the same direction as your toes. Return to the start position and do the next rep.</p> <p>This works the thighs, hips buttocks, quads, hamstring and lower body.</p>",
    calculate_in = CalculatedIn.REPS,
    animation = "",
    min_count = 0
)
squats.muscle_category.add(muscle_cat['legs'])
squats.muscle.add(muscle['glutes'])
squats.muscle.add(muscle['quadriceps'])
squats.muscle.add(muscle['hamstrings'])
squats.muscle.add(muscle['calves'])
squats.save()

side_lying_leg_lift_left = Exercise.objects.create(
    name = 'SIDE-LYING LEG LIFT LEFT',
    explanation = "<p>Lie down on your side with your head rested on your right hand. Lift your upper leg up and return to the start position</p> <p>make sure your left leg goes straight up and down during the exercise.</p> <p>It's a great exercise for glutes</p>",
    calculate_in = CalculatedIn.REPS,
    animation = "",
    min_count = 0
)
side_lying_leg_lift_left.muscle_category.add(muscle_cat['legs'])
side_lying_leg_lift_left.muscle.add(muscle['glutes'])
side_lying_leg_lift_left.muscle.add(muscle['adductors'])
side_lying_leg_lift_left.save()

side_lying_leg_lift_right = Exercise.objects.create(
    name = 'SIDE-LYING LEG LIFT RIGHT',
    explanation = "<p>Lie down on your side with your head rested on your left hand. Lift your upper leg up and return to the start position</p> <p>Make sure your right leg goes straight up and down during the exercise.</p> <p>It's a great exercise for glutes</p>",
    calculate_in = CalculatedIn.REPS,
    animation = "",
    min_count = 0
)
side_lying_leg_lift_right.muscle_category.add(muscle_cat['legs'])
side_lying_leg_lift_right.muscle.add(muscle['glutes'])
side_lying_leg_lift_right.muscle.add(muscle['adductors'])
side_lying_leg_lift_right.save()

lunges= Exercise.objects.create(
    name = 'LUNGES',
    explanation = "<p>Stand with your feet shoulder width apart and your hands on your hips.</p> <p>Take a steap forward with your right leg and lower your body until your right thigh is parallel with the floor.</p> <p>Then return and switch to the other leg. This exercise strengthens the quadriceps, glutes maximus and hamstrings.</p>",
    calculate_in = CalculatedIn.REPS,
    animation = "",
    min_count = 0
)
lunges.muscle_category.add(muscle_cat['legs'])
lunges.muscle.add(muscle['glutes'])
lunges.muscle.add(muscle['quadriceps'])
lunges.muscle.add(muscle['hamstrings'])
lunges.muscle.add(muscle['calves'])
lunges.save()

donkey_kick_left= Exercise.objects.create(
    name = 'DONKEY KICK LEFT',
    explanation = "<p>Start on all fours with your knees under your butt and your hands under your shoulders.</p> <p>Then lift your left leg and squeeze your butt as much as you can, Fo back to the start position and repeat the exercise.</p>",
    calculate_in = CalculatedIn.REPS,
    animation = "",
    min_count = 0
)
donkey_kick_left.muscle_category.add(muscle_cat['legs'])
donkey_kick_left.muscle.add(muscle['glutes'])
donkey_kick_left.save()

donkey_kick_right= Exercise.objects.create(
    name = 'DONKEY KICK RIGHT',
    explanation = "<p>Start on all fours with your knees under your butt and your hands under your shoulders.</p> <p>Then lift your right leg and squeeze your butt as much as you can, Fo back to the start position and repeat the exercise.</p>",
    calculate_in = CalculatedIn.REPS,
    animation = "",
    min_count = 0
)
donkey_kick_right.muscle_category.add(muscle_cat['legs'])
donkey_kick_right.muscle.add(muscle['glutes'])
donkey_kick_right.save()

left_quad_stretch= Exercise.objects.create(
    name = 'LEFT QUAD STRETCH',
    explanation = "<p>Bend your left leg and grasp your ankle or toes to bring your left calf close to your left thigh. Hold this position</p>",
    calculate_in = CalculatedIn.SECONDS,
    animation = "",
    min_count = 0
)
left_quad_stretch.muscle_category.add(muscle_cat['legs'])
left_quad_stretch.muscle.add(muscle['quadriceps'])
left_quad_stretch.save()

right_quad_stretch= Exercise.objects.create(
    name = 'RIGHT QUAD STRETCH',
    explanation = "<p>Bend your right leg and grasp your ankle or toes to bring your right calf close to your right thigh. Hold this position</p>",
    calculate_in = CalculatedIn.SECONDS,
    animation = "",
    min_count = 0
)
right_quad_stretch.muscle_category.add(muscle_cat['legs'])
right_quad_stretch.muscle.add(muscle['quadriceps'])
right_quad_stretch.save()

knee_to_chest_stretch_left= Exercise.objects.create(
    name = 'KNEE TO CHEST STRETCH LEFT',
    explanation = "<p>Lie on the floor with your legs extended. Lift your left knee up and grab it with both hands.</p> <p>Pull yout left knee towards your chest as much as you can while keeping your right leg straight on the ground.</p> <p>Hold this position for a few seconds.</p>",
    calculate_in = CalculatedIn.SECONDS,
    animation = "",
    min_count = 0
)
knee_to_chest_stretch_left.muscle_category.add(muscle_cat['legs'])
knee_to_chest_stretch_left.muscle.add(muscle['glutes'])
knee_to_chest_stretch_left.muscle.add(muscle['hamstrings'])
knee_to_chest_stretch_left.save()

knee_to_chest_stretch_right= Exercise.objects.create(
    name = 'KNEE TO CHEST STRETCH RIGHT',
    explanation = "<p>Lie on the floor with your legs extended. Lift your right knee up and grab it with both hands.</p> <p>Pull yout right knee towards your chest as much as you can while keeping your left leg straight on the ground.</p> <p>Hold this position for a few seconds.</p>",
    calculate_in = CalculatedIn.SECONDS,
    animation = "",
    min_count = 0
)
knee_to_chest_stretch_right.muscle_category.add(muscle_cat['legs'])
knee_to_chest_stretch_right.muscle.add(muscle['glutes'])
knee_to_chest_stretch_right.muscle.add(muscle['hamstrings'])
knee_to_chest_stretch_right.save()

wall_calf_raise= Exercise.objects.create(
    name = 'WALL CALF RAISE',
    explanation = "<p>Stand straight with your hands on the wall and feet shoulder width apart.</p> <p>Lift your heels and stand on your toes. Lift your heels and stand on your toes. Then drop your heels down. Repeat the exercise.</p>",
    calculate_in = CalculatedIn.REPS,
    animation = "",
    min_count = 0
)
wall_calf_raise.muscle_category.add(muscle_cat['legs'])
wall_calf_raise.muscle.add(muscle['calves'])
wall_calf_raise.save()

superman_pulls= Exercise.objects.create(
    name = 'SUPERMAN PULLS',
    explanation = "<p>Lie on your stomach with your legs straight and your arms stretch and extended overhead.</p> <p>Lift your legs and arms upwards then pull your arms down to wards your back. Return to the starting position and repeat.</p>",
    calculate_in = CalculatedIn.REPS,
    animation = "",
    min_count = 0
)
superman_pulls.muscle_category.add(muscle_cat['legs'])
superman_pulls.muscle_category.add(muscle_cat['abs'])
superman_pulls.muscle_category.add(muscle_cat['back_and_shoulder'])
superman_pulls.muscle.add(muscle['abs'])
superman_pulls.muscle.add(muscle['back'])
superman_pulls.muscle.add(muscle['shoulders'])
superman_pulls.muscle.add(muscle['traps'])
superman_pulls.muscle.add(muscle['hamstrings'])
superman_pulls.muscle.add(muscle['quadriceps'])
superman_pulls.muscle.add(muscle['glutes'])
superman_pulls.save()

side_lying_floor_stretch_left= Exercise.objects.create(
    name = 'SIDE-LYING FLOOR STRETCH LEFT',
    explanation = "<p>Lie on your right side with your right knee slightly bent in front of you and your left leg stretched behind the right leg</p> <p>Straighten your left arm over your head and gently pull on your left wrist to stretch the left side of your body.</p> <p>Hold this position for a few seconds.</p>",
    calculate_in = CalculatedIn.SECONDS,
    animation = "",
    min_count = 0
)
side_lying_floor_stretch_left.muscle_category.add(muscle_cat['back_and_shoulder'])
side_lying_floor_stretch_left.muscle.add(muscle['back'])
side_lying_floor_stretch_left.save()

side_lying_floor_stretch_right= Exercise.objects.create(
    name = 'SIDE-LYING FLOOR STRETCH RIGHT',
    explanation = "<p>Lie on your left side with your left knee slightly bent in front of you and your right leg stretched behind the left leg</p> <p>Straighten your right arm over your head and gently pull on your right wrist to stretch the right side of your body.</p> <p>Hold this position for a few seconds.</p>",
    calculate_in = CalculatedIn.SECONDS,
    animation = "",
    min_count = 0
)
side_lying_floor_stretch_right.muscle_category.add(muscle_cat['back_and_shoulder'])
side_lying_floor_stretch_right.muscle.add(muscle['back'])
side_lying_floor_stretch_right.save()

cat_cow_pose= Exercise.objects.create(
    name = 'CAT COW POSE',
    explanation = "<p>Start on all fours with your knees under your butt and your hands directly under your shoulders</p> <p>Then take a breath and make your belly fall down, shoulders roll back and head come up towards the ceiling.</p> <p>As you exhale, curve your back upwards and let your head come down. Repeat the exercise.</p> <p>Do it slowly with each step of this exercise</p> ",
    calculate_in = CalculatedIn.SECONDS,
    animation = "",
    min_count = 0
)
cat_cow_pose.muscle_category.add(muscle_cat['back_and_shoulder'])
cat_cow_pose.muscle_category.add(muscle_cat['abs'])
cat_cow_pose.muscle.add(muscle['abs'])
cat_cow_pose.muscle.add(muscle['back'])
cat_cow_pose.save()

triceps_push_up= Exercise.objects.create(
    name = 'TRICEPS PUSH UP',
    explanation = "<p>Lie on your stomach with your hands underneath your shoulders and your elbows bent.</p> <p>Raise your chest up, and then go back to the start position</p> <p>Repeat this exercise.</p>",
    calculate_in = CalculatedIn.REPS,
    animation = "",
    min_count = 0
)
triceps_push_up.muscle_category.add(muscle_cat['back_and_shoulder'])
triceps_push_up.muscle_category.add(muscle_cat['chest'])
triceps_push_up.muscle_category.add(muscle_cat['arms'])
triceps_push_up.muscle.add(muscle['triceps'])
triceps_push_up.muscle.add(muscle['shoulders'])
triceps_push_up.muscle.add(muscle['chest'])
triceps_push_up.save()

rhomboid_squeeze= Exercise.objects.create(
    name = 'RHOMBOID SQUEEZES',
    explanation = "<p>Sit with you back straight.</p> <p>Stretch your arms in front of you, then pull your elbows back to make your elbows at a 90 degree angle and squeze your shoulder blades.</p> <p>Repeat this exercise.</p>",
    calculate_in = CalculatedIn.REPS,
    animation = "",
    min_count = 0
)
rhomboid_squeeze.muscle_category.add(muscle_cat['back_and_shoulder'])
rhomboid_squeeze.muscle.add(muscle['back'])
rhomboid_squeeze.muscle.add(muscle['shoulders'])
rhomboid_squeeze.muscle.add(muscle['traps'])
rhomboid_squeeze.save()

child_pose= Exercise.objects.create(
    name = 'CHILD POSE',
    explanation = "<p>Start with your knees and hands on the floor. Put your hands a little forward, widen your knees and put your toes together.</p> <p>Take a breath, then exhale and sit back. Try to make your butt touch your heels, Relax your elbows make your forehead touch the floor and try to lower your chest close to the floor. Hold this position.</p> <p>Keep your arms stretched forward as you sit back. Make sure there is enough space between your shoulders and ears during the exercise.</p> ",
    calculate_in = CalculatedIn.SECONDS,
    animation = "",
    min_count = 0
)
child_pose.muscle_category.add(muscle_cat['back_and_shoulder'])
child_pose.muscle.add(muscle['back'])
child_pose.save()