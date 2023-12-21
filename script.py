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
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1702907338/gotBuff/workout_animation/jumping_jack_ntraxq.gif",
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
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1702907695/gotBuff/workout_animation/abdominal_crunches_wd2hym.gif",
    min_count = 0
)
abdominal_crunches.muscle_category.add(muscle_cat["abs"])
abdominal_crunches.muscle.add(muscle["abs"])
abdominal_crunches.save()

russian_twist = Exercise.objects.create(
    name = 'RUSSIAN TWISTS',
    explanation = "<p>Sit on the floor with your knees bent, feet lifted a little bit and back tilted backwards.</p>  <p>Then hold your hands together and twist from side to side.</p>",
    calculate_in = CalculatedIn.REPS,
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1702907798/gotBuff/workout_animation/russian_twist_rsx3fo.gif",
    min_count = 0
)
russian_twist.muscle_category.add(muscle_cat["abs"])
russian_twist.muscle.add(muscle["abs"])
russian_twist.save()

mountain_climber = Exercise.objects.create(
    name = 'MOUNTAIN CLIMBER',
    explanation = "<p>Start in the push-up position. Bend your right knees towards your left chest and keep your left leg straight, then quickly switch from one leg to yhe other.</p> <p>This exercise strengthens muscle groups.</p>",
    calculate_in = CalculatedIn.REPS,
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1702908476/gotBuff/workout_animation/mountain_climber_knpssl.gif",
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
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1702954337/gotBuff/workout_animation/heel_touch_gszagv.gif",
    min_count = 0
)
heel_touch.muscle_category.add(muscle_cat["abs"])
heel_touch.muscle.add(muscle["abs"])
heel_touch.save()

leg_raises = Exercise.objects.create(
    name = 'LEG RAISES',
    explanation = "<p>Lie down on your back, and put your hands beneath your hips for support.</p>  <p>Then lift your legs up until they form a right angle with the floor.</p> <p>Slowly bring your legs back down and repest the exercise.</p>",
    calculate_in = CalculatedIn.REPS,
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1702954600/gotBuff/workout_animation/leg_raises_owpcjv.gif",
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
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1702954783/gotBuff/workout_animation/plank_v00ose.gif",
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
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1702955206/gotBuff/workout_animation/cobra_stretch_dbf1yd.gif",
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
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1702956215/gotBuff/workout_animation/bent_leg_twist_buq6ma.gif",
    min_count = 0
)
bent_leg_twist.muscle_category.add(muscle_cat['abs'])
bent_leg_twist.muscle.add(muscle["abs"])
bent_leg_twist.save()

burpees = Exercise.objects.create(
    name = 'BURPEES',
    explanation = "<p>Stand with your feet together width apart, then put your hands on the ground and kick your feet backwards. Do a quick push-up and then jump up.</p>",
    calculate_in = CalculatedIn.SECONDS,
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1702956572/gotBuff/workout_animation/burpees_zvplgf.gif",
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
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1702983050/gotBuff/workout_animation/push_up_dpgle6.gif",
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
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1702983405/gotBuff/workout_animation/wide_push_up_b2qhrz.gif",
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
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1702989039/gotBuff/workout_animation/triceps_dips_d8jlcf.gif",
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
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1702989665/gotBuff/workout_animation/knee_push_up_zdgywg.gif",
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
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1702989865/gotBuff/workout_animation/chest_stretch_hyk05w.gif",
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

side_arm_raise = Exercise.objects.create(
    name = 'SIDE ARM RAISE',
    explanation = "<p>Stand with your feet and shoulder width apart.</p> <p>Raise your arms to the sides at the shoulder height, then put them down.</p> <p>Repeat the exercise. Keep yourr arms straight during exercise.</p>",
    calculate_in = CalculatedIn.SECONDS,
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1702990303/gotBuff/workout_animation/side_arm_raise_cwheps.gif",
    min_count = 0
)
side_arm_raise.muscle_category.add(muscle_cat['back_and_shoulder'])
side_arm_raise.muscle.add(muscle['shoulders'])
side_arm_raise.save()

arm_circle = Exercise.objects.create(
    name = 'ARM CIRCLE',
    explanation = "<p>Stand on the floor with your arms extended straight out to the sides at shoulder height.</p> <p>Move your arms cloclwise in circles fast.</p> <p>Try to do it as fast as you can.</p> <p>It's a great exercise for deltoid muscle.</p>",
    calculate_in = CalculatedIn.SECONDS,
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1702990498/gotBuff/workout_animation/arm_circle_tl8hen.gif",
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
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1702990649/gotBuff/workout_animation/diamond_push_up_rrku9q.gif",
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
    explanation = "<p>Sit down and lift your right leg up. Use your left hand to grab your right leg.</p> <p>Bring your leg towards yourself as much as you can, then lower it and repeat the exercise</p>",
    calculate_in = CalculatedIn.REPS,
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1702990885/gotBuff/workout_animation/biceps_legs_curl_right_wgzxvk.gif",
    min_count = 0
)
biceps_legs_curl_right.muscle_category.add(muscle_cat['arms'])
biceps_legs_curl_right.muscle.add(muscle['forearms'])
biceps_legs_curl_right.muscle.add(muscle['biceps'])
biceps_legs_curl_right.save()

biceps_legs_curl_left = Exercise.objects.create(
    name = 'BICEPS LEGS CURL LEFT',
    explanation = "<p>Sit down and lift your left leg up. Use your right hand to grab your left leg.</p> <p>Bring your leg towards yourself as much as you can, then lower it and repeat the exercise</p>",
    calculate_in = CalculatedIn.REPS,
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1702991043/gotBuff/workout_animation/biceps_legs_curl_left_wzlmvi.gif",
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
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1702991436/gotBuff/workout_animation/diagonal_plank_neronw.gif",
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
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1702991860/gotBuff/workout_animation/punches_zg0zbj.gif",
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
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1702992254/gotBuff/workout_animation/inchworms_klbmhe.gif",
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
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1703042970/gotBuff/workout_animation/triceps_stretch_left_ub1tpv.gif",
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
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1703043180/gotBuff/workout_animation/triceps_stretch_right_amlbnc.gif",
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
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1703043731/gotBuff/workout_animation/jumping_squats_ym1kfe.gif",
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
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1703044824/gotBuff/workout_animation/squats_bfhowb.gif",
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
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1703045645/gotBuff/workout_animation/side_lying_leg_lift_left_rkzw8k.gif",
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
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1703045732/gotBuff/workout_animation/side_lying_leg_lift_right_fylkcp.gif",
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
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1703053333/gotBuff/workout_animation/lunges_rdecyj.gif",
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
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1703054018/gotBuff/workout_animation/donkey_kick_left_bwxypu.gif",
    min_count = 0
)
donkey_kick_left.muscle_category.add(muscle_cat['legs'])
donkey_kick_left.muscle.add(muscle['glutes'])
donkey_kick_left.save()

donkey_kick_right= Exercise.objects.create(
    name = 'DONKEY KICK RIGHT',
    explanation = "<p>Start on all fours with your knees under your butt and your hands under your shoulders.</p> <p>Then lift your right leg and squeeze your butt as much as you can, Fo back to the start position and repeat the exercise.</p>",
    calculate_in = CalculatedIn.REPS,
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1703054087/gotBuff/workout_animation/donkey_kick_right_tuiqdg.gif",
    min_count = 0
)
donkey_kick_right.muscle_category.add(muscle_cat['legs'])
donkey_kick_right.muscle.add(muscle['glutes'])
donkey_kick_right.save()

left_quad_stretch= Exercise.objects.create(
    name = 'LEFT QUAD STRETCH',
    explanation = "<p>Bend your left leg and grasp your ankle or toes to bring your left calf close to your left thigh. Hold this position</p>",
    calculate_in = CalculatedIn.SECONDS,
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1703055072/gotBuff/workout_animation/left_quad_stretch_ye2zsu.gif",
    min_count = 0
)
left_quad_stretch.muscle_category.add(muscle_cat['legs'])
left_quad_stretch.muscle.add(muscle['quadriceps'])
left_quad_stretch.save()

right_quad_stretch= Exercise.objects.create(
    name = 'RIGHT QUAD STRETCH',
    explanation = "<p>Bend your right leg and grasp your ankle or toes to bring your right calf close to your right thigh. Hold this position</p>",
    calculate_in = CalculatedIn.SECONDS,
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1703055077/gotBuff/workout_animation/right_quad_stretch_d6gttq.gif",
    min_count = 0
)
right_quad_stretch.muscle_category.add(muscle_cat['legs'])
right_quad_stretch.muscle.add(muscle['quadriceps'])
right_quad_stretch.save()

knee_to_chest_stretch_left= Exercise.objects.create(
    name = 'KNEE TO CHEST STRETCH LEFT',
    explanation = "<p>Lie on the floor with your legs extended. Lift your left knee up and grab it with both hands.</p> <p>Pull yout left knee towards your chest as much as you can while keeping your right leg straight on the ground.</p> <p>Hold this position for a few seconds.</p>",
    calculate_in = CalculatedIn.SECONDS,
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1703056315/gotBuff/workout_animation/knee_to_chest_stretch_left_azoikl.gif",
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
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1703056429/gotBuff/workout_animation/knee_to_chest_stretch_right_bz1nbo.gif",
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
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1703057046/gotBuff/workout_animation/wall_calf_raise_ayisui.gif",
    min_count = 0
)
wall_calf_raise.muscle_category.add(muscle_cat['legs'])
wall_calf_raise.muscle.add(muscle['calves'])
wall_calf_raise.save()

superman_pulls= Exercise.objects.create(
    name = 'SUPERMAN PULLS',
    explanation = "<p>Lie on your stomach with your legs straight and your arms stretch and extended overhead.</p> <p>Lift your legs and arms upwards then pull your arms down to wards your back. Return to the starting position and repeat.</p>",
    calculate_in = CalculatedIn.REPS,
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1703057828/gotBuff/workout_animation/superman_pulls_mnu2me.gif",
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
    explanation = "<p>Lie on your right side. </p> <p>Straighten your left arm over your head and gently pull on your left wrist to stretch the left side of your body.</p> <p>Hold this position for a few seconds.</p>",
    calculate_in = CalculatedIn.SECONDS,
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1703057917/gotBuff/workout_animation/side_lying_floor_stretch_left_f8bnxr.gif",
    min_count = 0
)
side_lying_floor_stretch_left.muscle_category.add(muscle_cat['back_and_shoulder'])
side_lying_floor_stretch_left.muscle.add(muscle['back'])
side_lying_floor_stretch_left.save()

side_lying_floor_stretch_right= Exercise.objects.create(
    name = 'SIDE-LYING FLOOR STRETCH RIGHT',
    explanation = "<p>Lie on your left side. </p> <p>Straighten your right arm over your head and gently pull on your right wrist to stretch the right side of your body.</p> <p>Hold this position for a few seconds.</p>",
    calculate_in = CalculatedIn.SECONDS,
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1703057992/gotBuff/workout_animation/side_lying_floor_stretch_right_f1t1xr.gif",
    min_count = 0
)
side_lying_floor_stretch_right.muscle_category.add(muscle_cat['back_and_shoulder'])
side_lying_floor_stretch_right.muscle.add(muscle['back'])
side_lying_floor_stretch_right.save()

cat_cow_pose= Exercise.objects.create(
    name = 'CAT COW POSE',
    explanation = "<p>Start on all fours with your knees under your butt and your hands directly under your shoulders</p> <p>Then take a breath and make your belly fall down, shoulders roll back and head come up towards the ceiling.</p> <p>As you exhale, curve your back upwards and let your head come down. Repeat the exercise.</p> <p>Do it slowly with each step of this exercise</p> ",
    calculate_in = CalculatedIn.SECONDS,
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1703058702/gotBuff/workout_animation/cat_cow_pose_hnajge.gif",
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
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1703059040/gotBuff/workout_animation/triceps_push_up_bl2hv1.gif",
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
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1703059328/gotBuff/workout_animation/rhomboid_squeeze_x5tkju.gif",
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
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1703059857/gotBuff/workout_animation/child_pose_ekx1cv.gif",
    min_count = 0
)
child_pose.muscle_category.add(muscle_cat['back_and_shoulder'])
child_pose.muscle.add(muscle['back'])
child_pose.save()

crossover_crunch= Exercise.objects.create(
    name = 'CROSSOVER CRUNCH',
    explanation = "<p>Lie on your back with knees bent and your hands behind your ears.</p> <p>Raise and twist your torso so your right elbow moves to meet your left knee. Repeat with the other side.</p> ",
    calculate_in = CalculatedIn.REPS,
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1703060428/gotBuff/workout_animation/crossover_crunch_gc2vwg.gif",
    min_count = 0
)
crossover_crunch.muscle_category.add(muscle_cat['abs'])
crossover_crunch.muscle_category.add(muscle_cat['legs'])
crossover_crunch.muscle.add(muscle['abs'])
crossover_crunch.muscle.add(muscle['glutes'])
crossover_crunch.muscle.add(muscle['quadriceps'])
crossover_crunch.save()

side_bridges_left= Exercise.objects.create(
    name = 'SIDE BRIDGES LEFT',
    explanation = "<p>Lie on your right side. Put your right elbow directly under your shoulders and put your left hand on your waist. Place your left leg on your right leg.</p> <p>Raise your hips upward, hold for 2-4 seconds, then go back to the start position.</p> <p>Repeat this exercise.</p> <p># Dumbbell is optional</p>",
    calculate_in = CalculatedIn.REPS,
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1703060717/gotBuff/workout_animation/side_bridges_left_me8wtu.gif",
    min_count = 0
)
side_bridges_left.muscle_category.add(muscle_cat['abs'])
side_bridges_left.muscle_category.add(muscle_cat['legs'])
side_bridges_left.muscle.add(muscle['abs'])
side_bridges_left.muscle.add(muscle['glutes'])
side_bridges_left.muscle.add(muscle['adductors'])
side_bridges_left.save()

side_bridges_right= Exercise.objects.create(
    name = 'SIDE BRIDGES RIGHT',
    explanation = "<p>Lie on your left side. Put your left elbow directly under your shoulders and put your right hand on your waist. Place your right leg on your left leg.</p> <p>Raise your hips upward, hold for 2-4 seconds, then go back to the start position.</p> <p>Repeat this exercise.</p> <p># Dumbbell is optional</p>",
    calculate_in = CalculatedIn.REPS,
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1703061144/gotBuff/workout_animation/side_bridges_right_r4znoy.gif",
    min_count = 0
)
side_bridges_right.muscle_category.add(muscle_cat['abs'])
side_bridges_right.muscle_category.add(muscle_cat['legs'])
side_bridges_right.muscle.add(muscle['abs'])
side_bridges_right.muscle.add(muscle['glutes'])
side_bridges_right.muscle.add(muscle['adductors'])
side_bridges_right.save()

butt_bridges= Exercise.objects.create(
    name = 'BUTT BRIDGES',
    explanation = "<p>Lie on your back with knees bent and feet flat on the floor. Put your arms flat at your sides.</p> <p>Then lift your butt up and down.</p> <p># Dumbbell is optional</p>",
    calculate_in = CalculatedIn.REPS,
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1703061493/gotBuff/workout_animation/butt_bridges_vgnpsi.gif",
    min_count = 0
)
butt_bridges.muscle_category.add(muscle_cat['legs'])
butt_bridges.muscle.add(muscle['glutes'])
butt_bridges.muscle.add(muscle['hamstrings'])
butt_bridges.save()

bicycle_crunches= Exercise.objects.create(
    name = 'BICYCLE CRUNCHES',
    explanation = "<p>Lie on the floor with your hands behind your ears. Raise your knees and close your right elbow towards your left knee, then close your left elbow towards your right knee. Repeat the exercise.</p>",
    calculate_in = CalculatedIn.REPS,
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1703061867/gotBuff/workout_animation/bicycle_crunches_mdtiyf.gif",
    min_count = 0
)
bicycle_crunches.muscle_category.add(muscle_cat['legs'])
bicycle_crunches.muscle_category.add(muscle_cat['abs'])
bicycle_crunches.muscle.add(muscle['glutes'])
bicycle_crunches.muscle.add(muscle['abs'])
bicycle_crunches.muscle.add(muscle['quadriceps'])
bicycle_crunches.save()

v_up= Exercise.objects.create(
    name = 'V UP',
    explanation = "<p>Lie on your back with your arms and legs extended and your legs squeezed together.</p> <p>Raise your upper body and legs, use your arms to touch your toes, then go back to the start position and repeat the exercise.</p>",
    calculate_in = CalculatedIn.REPS,
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1703062942/gotBuff/workout_animation/v_up_p46f9r.gif",
    min_count = 0
)
v_up.muscle_category.add(muscle_cat['legs'])
v_up.muscle_category.add(muscle_cat['abs'])
v_up.muscle.add(muscle['abs'])
v_up.muscle.add(muscle['quadriceps'])
v_up.save()

push_up_and_rotation= Exercise.objects.create(
    name = 'PUSH-UP & ROTATION',
    explanation = "<p>Start in the push-up position. Then go down for a push-up and as you come up, rotate your upper body and extend your right arm upwards.</p> <p>Repeat the exercise with the other arm, It's a great exercise for the chest, shoulders, arms and core.</p>",
    calculate_in = CalculatedIn.REPS,
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1703063076/gotBuff/workout_animation/push_up_and_rotation_wnuz4r.gif",
    min_count = 0
)
push_up_and_rotation.muscle_category.add(muscle_cat['legs'])
push_up_and_rotation.muscle_category.add(muscle_cat['abs'])
push_up_and_rotation.muscle_category.add(muscle_cat['arms'])
push_up_and_rotation.muscle_category.add(muscle_cat['back_and_shoulder'])
push_up_and_rotation.muscle_category.add(muscle_cat['chest'])
push_up_and_rotation.muscle.add(muscle['chest'])
push_up_and_rotation.muscle.add(muscle['abs'])
push_up_and_rotation.muscle.add(muscle['shoulders'])
push_up_and_rotation.muscle.add(muscle['triceps'])
push_up_and_rotation.muscle.add(muscle['glutes'])
push_up_and_rotation.save()

side_plank_left= Exercise.objects.create(
    name = 'SIDE PLANK LEFT',
    explanation = "<p>Lie on your left side with your forearm supporting your body. Hold your body in a straight line.</p> <p>This exercise targets the abdominal muscles and obliques.</p>",
    calculate_in = CalculatedIn.SECONDS,
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1703063551/gotBuff/workout_animation/side_plank_left_hhffbi.gif",
    min_count = 0
)
side_plank_left.muscle_category.add(muscle_cat['abs'])
side_plank_left.muscle.add(muscle['abs'])
side_plank_left.save()

side_plank_right= Exercise.objects.create(
    name = 'SIDE PLANK RIGHT',
    explanation = "<p>Lie on your right side with your forearm supporting your body. Hold your body in a straight line.</p> <p>This exercise targets the abdominal muscles and obliques.</p>",
    calculate_in = CalculatedIn.SECONDS,
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1703063709/gotBuff/workout_animation/side_plank_right_r7wz0v.gif",
    min_count = 0
)
side_plank_right.muscle_category.add(muscle_cat['abs'])
side_plank_right.muscle.add(muscle['abs'])
side_plank_right.save()

hindu_push_up= Exercise.objects.create(
    name = 'HINDU PUSH-UP',
    explanation = "<p>Start with your hands and feet touching the floor, do a normal push-up, then bend your body and butt up in an upside down 'V' shape.</p> <p>Then bent your elbow to return to original position.</p>",
    calculate_in = CalculatedIn.REPS,
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1703064045/gotBuff/workout_animation/hindu_push_up_kfz0tw.gif",
    min_count = 0
)
hindu_push_up.muscle_category.add(muscle_cat['legs'])
hindu_push_up.muscle_category.add(muscle_cat['back_and_shoulder'])
hindu_push_up.muscle_category.add(muscle_cat['arms'])
hindu_push_up.muscle_category.add(muscle_cat['chest'])
hindu_push_up.muscle.add(muscle['back'])
hindu_push_up.muscle.add(muscle['chest'])
hindu_push_up.muscle.add(muscle['triceps'])
hindu_push_up.muscle.add(muscle['glutes'])
hindu_push_up.muscle.add(muscle['hamstrings'])
hindu_push_up.muscle.add(muscle['calves'])
hindu_push_up.muscle.add(muscle['shoulders'])
hindu_push_up.save()

pike_push_up= Exercise.objects.create(
    name = 'PIKE PUSH-UP',
    explanation = "<p>Start with your hands and feet on the floor. Put your hands shoulder width apart. bend your body, and lift your hips up in an upside down 'V' shape.</p> <p>Bend your elbows, and bring your head close to the floor. Push your body back, and repeat the exercise.</p>",
    calculate_in = CalculatedIn.REPS,
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1703064492/gotBuff/workout_animation/pike_push_up_acxlxi.gif",
    min_count = 0
)
pike_push_up.muscle_category.add(muscle_cat['back_and_shoulder'])
pike_push_up.muscle_category.add(muscle_cat['arms'])
pike_push_up.muscle_category.add(muscle_cat['chest'])
pike_push_up.muscle.add(muscle['chest'])
pike_push_up.muscle.add(muscle['triceps'])
pike_push_up.muscle.add(muscle['shoulders'])
pike_push_up.save()

decline_push_up= Exercise.objects.create(
    name = 'DECLINE PUSH-UP',
    explanation = "<p>Start on all fours with your knees under your butt and your hands under your shoulders.</p> <p>Then elevate your feet on a chair or bench, and push your body up and down mainly using your arm strength.</p> <p>Remember to keep your body straight.</p>",
    calculate_in = CalculatedIn.REPS,
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1703065095/gotBuff/workout_animation/decline_push_up_s2mrwx.gif",
    min_count = 0
)
decline_push_up.muscle_category.add(muscle_cat['back_and_shoulder'])
decline_push_up.muscle_category.add(muscle_cat['arms'])
decline_push_up.muscle_category.add(muscle_cat['chest'])
decline_push_up.muscle.add(muscle['chest'])
decline_push_up.muscle.add(muscle['triceps'])
decline_push_up.muscle.add(muscle['shoulders'])
decline_push_up.save()

right_hooks= Exercise.objects.create(
    name = 'RIGHT HOOKS',
    explanation = "<p>Stand with your feet shoulder-width apart, and place your dominant foor slightly forward. Slightly bend your knees, clench your fists and bend your elbows at 90 degrees.</p> <p>Raise your right arm to shoulder height and keep your forearm parallel to the ground. Rotate your shoulders and hips and punch towards the left.</p>",
    calculate_in = CalculatedIn.SECONDS,
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1703065140/gotBuff/workout_animation/right_hooks_hujsmq.gif",
    min_count = 0
)
right_hooks.muscle_category.add(muscle_cat['back_and_shoulder'])
right_hooks.muscle_category.add(muscle_cat['abs'])
right_hooks.muscle_category.add(muscle_cat['legs'])
right_hooks.muscle_category.add(muscle_cat['chest'])
right_hooks.muscle.add(muscle['chest'])
right_hooks.muscle.add(muscle['back'])
right_hooks.muscle.add(muscle['shoulders'])
right_hooks.muscle.add(muscle['abs'])
right_hooks.muscle.add(muscle['calves'])
right_hooks.save()

left_hooks= Exercise.objects.create(
    name = 'LEFT HOOKS',
    explanation = "<p>Stand with your feet shoulder-width apart, and place your dominant foor slightly forward. Slightly bend your knees, clench your fists and bend your elbows at 90 degrees.</p> <p>Raise your left arm to shoulder height and keep your forearm parallel to the ground. Rotate your shoulders and hips and punch towards the right.</p>",
    calculate_in = CalculatedIn.SECONDS,
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1703065235/gotBuff/workout_animation/left_hooks_rbhlhm.gif",
    min_count = 0
)
left_hooks.muscle_category.add(muscle_cat['back_and_shoulder'])
left_hooks.muscle_category.add(muscle_cat['abs'])
left_hooks.muscle_category.add(muscle_cat['legs'])
left_hooks.muscle_category.add(muscle_cat['chest'])
left_hooks.muscle.add(muscle['chest'])
left_hooks.muscle.add(muscle['back'])
left_hooks.muscle.add(muscle['shoulders'])
left_hooks.muscle.add(muscle['abs'])
left_hooks.muscle.add(muscle['calves'])
left_hooks.save()

skipping_without_ropes= Exercise.objects.create(
    name = 'SKIPPING WITHOUT ROPE',
    explanation = "<p>Place your arms at your sides and pretend to hold a skipping rope handle in each hand.</p> <p>Jump and alternatly land on the balls of your feet, rotating your wrist at the same time as if you were spinning a rope.</p>",
    calculate_in = CalculatedIn.SECONDS,
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1703065717/gotBuff/workout_animation/skipping_without_ropes_avfz6j.gif",
    min_count = 0
)
skipping_without_ropes.muscle_category.add(muscle_cat['legs'])
skipping_without_ropes.muscle.add(muscle['glutes'])
skipping_without_ropes.muscle.add(muscle['quadriceps'])
skipping_without_ropes.muscle.add(muscle['hamstrings'])
skipping_without_ropes.muscle.add(muscle['calves'])
skipping_without_ropes.save()

fire_hydrant_left= Exercise.objects.create(
    name = 'FIRE HYDRANT LEFT',
    explanation = "<p>Start on all four with your knees under your butt and your hands under your shoulders.</p> <p>Then lift your left leg to the side at a 90 degree angle.</p>",
    calculate_in = CalculatedIn.REPS,
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1703066336/gotBuff/workout_animation/fire_hydrant_left_ajk6j9.gif",
    min_count = 0
)
fire_hydrant_left.muscle_category.add(muscle_cat['legs'])
fire_hydrant_left.muscle.add(muscle['glutes'])
fire_hydrant_left.save()

fire_hydrant_right= Exercise.objects.create(
    name = 'FIRE HYDRANT RIGHT',
    explanation = "<p>Start on all four with your knees under your butt and your hands under your shoulders.</p> <p>Then lift your right leg to the side at a 90 degree angle.</p>",
    calculate_in = CalculatedIn.REPS,
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1703066424/gotBuff/workout_animation/fire_hydrant_right_ljnmtg.gif",
    min_count = 0
)
fire_hydrant_right.muscle_category.add(muscle_cat['legs'])
fire_hydrant_right.muscle.add(muscle['glutes'])
fire_hydrant_right.save()

sumo_squat= Exercise.objects.create(
    name = 'SUMO SQUAT',
    explanation = "<p>Stand with your feet 6-12 inches apart. Place your hands at the opposite shoulder to form an 'X'.</p> <p>Lower your body until your thighs are parallel to the floor. Return to the starting position and repeat the exercise.</p>",
    calculate_in = CalculatedIn.REPS,
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1703067284/gotBuff/workout_animation/sumo_squat_w6fdwc.gif",
    min_count = 0
)
sumo_squat.muscle_category.add(muscle_cat['legs'])
sumo_squat.muscle.add(muscle['glutes'])
sumo_squat.muscle.add(muscle['quadriceps'])
sumo_squat.muscle.add(muscle['adductors'])
sumo_squat.muscle.add(muscle['hamstrings'])
sumo_squat.muscle.add(muscle['calves'])
sumo_squat.save()

flutter_kick= Exercise.objects.create(
    name = 'FLUTTER KICKS',
    explanation = "<p>Lie down on the floor, and place your hands on the sides.</p> <p>Lift your leg up as much as you can. When you start to lower the raised leg, start to raise the other and repeat.</p>",
    calculate_in = CalculatedIn.REPS,
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1703067738/gotBuff/workout_animation/flutter_kick_fins2n.gif",
    min_count = 0
)
flutter_kick.muscle_category.add(muscle_cat['legs'])
flutter_kick.muscle.add(muscle['glutes'])
flutter_kick.muscle.add(muscle['hamstrings'])
flutter_kick.save()

wall_sit= Exercise.objects.create(
    name = 'WALL SIT',
    explanation = "<p>Start with your back against the wall, then slide down until your knees are at a 90 degree angle.</p> <p>Keep your back against the wall with your hands and arms away from the legs. Hold the position.</p> <p>The exercise is to strengthen the quadriceps muscles.</p>",
    calculate_in = CalculatedIn.REPS,
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1703067829/gotBuff/workout_animation/wall_sit_kc2vxo.gif",
    min_count = 0
)
wall_sit.muscle_category.add(muscle_cat['legs'])
wall_sit.muscle.add(muscle['glutes'])
wall_sit.muscle.add(muscle['quadriceps'])
wall_sit.muscle.add(muscle['calves'])
wall_sit.muscle.add(muscle['hamstrings'])
wall_sit.save()

triceps_kick_backs= Exercise.objects.create(
    name = 'TRICEPS KICK BACKS',
    explanation = "<p>Lean forward, bend your knees and your elbows.</p> <p>Extend your arms behind you and squeeze your triceps. Please make your arms parallel to the ground when extending them.</p> <p>Go back to the start position, and repeat this exercise.</p>",
    calculate_in = CalculatedIn.REPS,
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1703068299/gotBuff/workout_animation/triceps_kick_backs_oeavig.gif",
    min_count = 0
)
triceps_kick_backs.muscle_category.add(muscle_cat['arms'])
triceps_kick_backs.muscle.add(muscle['triceps'])
triceps_kick_backs.save()

supine_push_ups= Exercise.objects.create(
    name = 'SUPINE PUSH UP',
    explanation = "<p>Lie on your back with your feet flat on the floor and your arms bent on two sides.</p> <p>Push your cheest up as far as youcan, and then slowly go back to the start position.</p> <p>Repeat the exercise.</p>",
    calculate_in = CalculatedIn.REPS,
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1703068600/gotBuff/workout_animation/supine_push_ups_laje9s.gif",
    min_count = 0
)
supine_push_ups.muscle_category.add(muscle_cat['back_and_shoulder'])
supine_push_ups.muscle.add(muscle['back'])
supine_push_ups.muscle.add(muscle['traps'])
supine_push_ups.muscle.add(muscle['shoulders'])
supine_push_ups.save()

swimmer_and_superman= Exercise.objects.create(
    name = 'SWIMMER & SUPERMAN',
    explanation = "<p>Lie on your stomach with your arms extended straight overhead. Alternately lift your opposite arm and leg.</p>",
    calculate_in = CalculatedIn.REPS,
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1703068998/gotBuff/workout_animation/swimmer_and_superman_phwyp0.gif",
    min_count = 0
)
swimmer_and_superman.muscle_category.add(muscle_cat['back_and_shoulder'])
swimmer_and_superman.muscle_category.add(muscle_cat['legs'])
swimmer_and_superman.muscle.add(muscle['back'])
swimmer_and_superman.muscle.add(muscle['glutes'])
swimmer_and_superman.muscle.add(muscle['hamstrings'])
swimmer_and_superman.muscle.add(muscle['shoulders'])
swimmer_and_superman.save()

sit_up= Exercise.objects.create(
    name = 'SIT UP',
    explanation = "<p>Lie on your back with hands behind your ears.</p> <p>Then lift your upper body off the floor and slowly up to the sitting position and turn left. Dont tug your neck when you get up.</p> <p>Slowly go back to the start position and repeat the exercise but turn right this time.</p>",
    calculate_in = CalculatedIn.REPS,
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1703069692/gotBuff/workout_animation/sit_up_n7odb6.gif",
    min_count = 0
)
sit_up.muscle_category.add(muscle_cat['abs'])
sit_up.muscle.add(muscle['abs'])
sit_up.muscle.add(muscle['quadriceps'])
sit_up.save()

arm_curls_crunch_left= Exercise.objects.create(
    name = 'ARM CURLS CRUNCH LEFT',
    explanation = "<p>Lie on your left side with your knees bent and lifted. Place your left hand on the floor and put your right hand behind your head.</p> <p>Then raise your upper body by putting force in both your hands.</p>",
    calculate_in = CalculatedIn.REPS,
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1703070257/gotBuff/workout_animation/arm_curls_crunch_left_zfjj3l.gif",
    min_count = 0
)
arm_curls_crunch_left.muscle_category.add(muscle_cat['abs'])
arm_curls_crunch_left.muscle_category.add(muscle_cat['arms'])
arm_curls_crunch_left.muscle.add(muscle['abs'])
arm_curls_crunch_left.muscle.add(muscle['forearms'])
arm_curls_crunch_left.muscle.add(muscle['biceps'])
arm_curls_crunch_left.save()

arm_curls_crunch_right= Exercise.objects.create(
    name = 'ARM CURLS CRUNCH RIGHT',
    explanation = "<p>Lie on your right side with your knees bent and lifted. Place your right hand on the floor and put your left hand behind your head.</p> <p>Then raise your upper body by putting force in both your hands.</p>",
    calculate_in = CalculatedIn.REPS,
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1703070341/gotBuff/workout_animation/arm_curls_crunch_right_dznccv.gif",
    min_count = 0
)
arm_curls_crunch_right.muscle_category.add(muscle_cat['abs'])
arm_curls_crunch_right.muscle_category.add(muscle_cat['arms'])
arm_curls_crunch_right.muscle.add(muscle['abs'])
arm_curls_crunch_right.muscle.add(muscle['forearms'])
arm_curls_crunch_right.muscle.add(muscle['biceps'])
arm_curls_crunch_right.save()

doorways_curls= Exercise.objects.create(
    name = 'DOORWAY CURLS',
    explanation = "<p>Stand in a doorway. Grasp the doorframe using both your hands, and put your feet close to the bottom of the door.</p> <p>Extend your left arm and lean back, then pull at the doorframe and come back to the starting position. Repeat the exercise.</p>",
    calculate_in = CalculatedIn.REPS,
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1703070418/gotBuff/workout_animation/doorways_curls_zyto46.gif",
    min_count = 0
)
doorways_curls.muscle_category.add(muscle_cat['arms'])
doorways_curls.muscle.add(muscle['forearms'])
doorways_curls.muscle.add(muscle['biceps'])
doorways_curls.save()

curtsy_lunges= Exercise.objects.create(
    name = 'CURTSY LUNGES',
    explanation = "<p>Stand straight up. Then step back with your left leg to the right, bend your knees at the same time.</p> <p>Go back to the start position and switch to the other side.</p>",
    calculate_in = CalculatedIn.REPS,
    animation = "https://res.cloudinary.com/dmoa45uta/image/upload/v1703070559/gotBuff/workout_animation/curtsy_lunges_eyzpjp.gif",
    min_count = 0
)
curtsy_lunges.muscle_category.add(muscle_cat['legs'])
curtsy_lunges.muscle.add(muscle['quadriceps'])
curtsy_lunges.muscle.add(muscle['glutes'])
curtsy_lunges.muscle.add(muscle['adductors'])
curtsy_lunges.muscle.add(muscle['hamstrings'])
curtsy_lunges.muscle.add(muscle['calves'])
curtsy_lunges.save()

# abs beginner exercise
PresetTrainingExercise.objects.create(
    calculate_in = jumping_jack.calculate_in,
    required_value = 20,
    level = preset_training_set['preset_abs_beginner'].level,
    belong_to_training_set = preset_training_set['preset_abs_beginner'],
    exercise = jumping_jack,
    order=1
)
PresetTrainingExercise.objects.create(
    calculate_in = abdominal_crunches.calculate_in,
    required_value = 16,
    level = preset_training_set['preset_abs_beginner'].level,
    belong_to_training_set = preset_training_set['preset_abs_beginner'],
    exercise = abdominal_crunches,
    order=2
)
PresetTrainingExercise.objects.create(
    calculate_in = russian_twist.calculate_in,
    required_value = 20,
    level = preset_training_set['preset_abs_beginner'].level,
    belong_to_training_set = preset_training_set['preset_abs_beginner'],
    exercise = russian_twist,
    order=3
)
PresetTrainingExercise.objects.create(
    calculate_in = mountain_climber.calculate_in,
    required_value = 16,
    level = preset_training_set['preset_abs_beginner'].level,
    belong_to_training_set = preset_training_set['preset_abs_beginner'],
    exercise = mountain_climber,
    order=4
)
PresetTrainingExercise.objects.create(
    calculate_in = heel_touch.calculate_in,
    required_value = 20,
    level = preset_training_set['preset_abs_beginner'].level,
    belong_to_training_set = preset_training_set['preset_abs_beginner'],
    exercise = heel_touch,
    order=5
)
PresetTrainingExercise.objects.create(
    calculate_in = leg_raises.calculate_in,
    required_value = 16,
    level = preset_training_set['preset_abs_beginner'].level,
    belong_to_training_set = preset_training_set['preset_abs_beginner'],
    exercise = leg_raises,
    order=6
)
PresetTrainingExercise.objects.create(
    calculate_in = plank.calculate_in,
    required_value = 20,
    level = preset_training_set['preset_abs_beginner'].level,
    belong_to_training_set = preset_training_set['preset_abs_beginner'],
    exercise = plank,
    order=7
)
PresetTrainingExercise.objects.create(
    calculate_in = abdominal_crunches.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_abs_beginner'].level,
    belong_to_training_set = preset_training_set['preset_abs_beginner'],
    exercise = abdominal_crunches,
    order=8
)
PresetTrainingExercise.objects.create(
    calculate_in = russian_twist.calculate_in,
    required_value = 20,
    level = preset_training_set['preset_abs_beginner'].level,
    belong_to_training_set = preset_training_set['preset_abs_beginner'],
    exercise = russian_twist,
    order=9
)
PresetTrainingExercise.objects.create(
    calculate_in = mountain_climber.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_abs_beginner'].level,
    belong_to_training_set = preset_training_set['preset_abs_beginner'],
    exercise = mountain_climber,
    order=10
)
PresetTrainingExercise.objects.create(
    calculate_in = heel_touch.calculate_in,
    required_value = 20,
    level = preset_training_set['preset_abs_beginner'].level,
    belong_to_training_set = preset_training_set['preset_abs_beginner'],
    exercise = heel_touch,
    order=11
)
PresetTrainingExercise.objects.create(
    calculate_in = leg_raises.calculate_in,
    required_value = 14,
    level = preset_training_set['preset_abs_beginner'].level,
    belong_to_training_set = preset_training_set['preset_abs_beginner'],
    exercise = leg_raises,
    order=12
)
PresetTrainingExercise.objects.create(
    calculate_in = plank.calculate_in,
    required_value = 30,
    level = preset_training_set['preset_abs_beginner'].level,
    belong_to_training_set = preset_training_set['preset_abs_beginner'],
    exercise = plank,
    order=13
)
PresetTrainingExercise.objects.create(
    calculate_in = cobra_stretch.calculate_in,
    required_value = 30,
    level = preset_training_set['preset_abs_beginner'].level,
    belong_to_training_set = preset_training_set['preset_abs_beginner'],
    exercise = cobra_stretch,
    order=14
)
PresetTrainingExercise.objects.create(
    calculate_in = bent_leg_twist.calculate_in,
    required_value = 16,
    level = preset_training_set['preset_abs_beginner'].level,
    belong_to_training_set = preset_training_set['preset_abs_beginner'],
    exercise = bent_leg_twist,
    order=15
)
PresetTrainingExercise.objects.create(
    calculate_in = burpees.calculate_in,
    required_value = 16,
    level = preset_training_set['preset_abs_beginner'].level,
    belong_to_training_set = preset_training_set['preset_abs_beginner'],
    exercise = burpees,
    order=16
)

# chest beginner
PresetTrainingExercise.objects.create(
    calculate_in = jumping_jack.calculate_in,
    required_value = 30,
    level = preset_training_set['preset_chest_beginner'].level,
    belong_to_training_set = preset_training_set['preset_chest_beginner'],
    exercise = jumping_jack,
    order=1
)
PresetTrainingExercise.objects.create(
    calculate_in = push_up.calculate_in,
    required_value = 6,
    level = preset_training_set['preset_chest_beginner'].level,
    belong_to_training_set = preset_training_set['preset_chest_beginner'],
    exercise = push_up,
    order=2
)
PresetTrainingExercise.objects.create(
    calculate_in = diamond_push_up.calculate_in,
    required_value = 6,
    level = preset_training_set['preset_chest_beginner'].level,
    belong_to_training_set = preset_training_set['preset_chest_beginner'],
    exercise = diamond_push_up,
    order=3
)
PresetTrainingExercise.objects.create(
    calculate_in = wide_push_up.calculate_in,
    required_value = 6,
    level = preset_training_set['preset_chest_beginner'].level,
    belong_to_training_set = preset_training_set['preset_chest_beginner'],
    exercise = wide_push_up,
    order=4
)
PresetTrainingExercise.objects.create(
    calculate_in = triceps_dips.calculate_in,
    required_value = 6,
    level = preset_training_set['preset_chest_beginner'].level,
    belong_to_training_set = preset_training_set['preset_chest_beginner'],
    exercise = triceps_dips,
    order=5
)
PresetTrainingExercise.objects.create(
    calculate_in = wide_push_up.calculate_in,
    required_value = 6,
    level = preset_training_set['preset_chest_beginner'].level,
    belong_to_training_set = preset_training_set['preset_chest_beginner'],
    exercise = wide_push_up,
    order=6
)
PresetTrainingExercise.objects.create(
    calculate_in = push_up.calculate_in,
    required_value = 6,
    level = preset_training_set['preset_chest_beginner'].level,
    belong_to_training_set = preset_training_set['preset_chest_beginner'],
    exercise = push_up,
    order=7
)
PresetTrainingExercise.objects.create(
    calculate_in = triceps_dips.calculate_in,
    required_value = 6,
    level = preset_training_set['preset_chest_beginner'].level,
    belong_to_training_set = preset_training_set['preset_chest_beginner'],
    exercise = triceps_dips,
    order=8
)
PresetTrainingExercise.objects.create(
    calculate_in = knee_push_up.calculate_in,
    required_value = 6,
    level = preset_training_set['preset_chest_beginner'].level,
    belong_to_training_set = preset_training_set['preset_chest_beginner'],
    exercise = knee_push_up,
    order=9
)
PresetTrainingExercise.objects.create(
    calculate_in = cobra_stretch.calculate_in,
    required_value = 20,
    level = preset_training_set['preset_chest_beginner'].level,
    belong_to_training_set = preset_training_set['preset_chest_beginner'],
    exercise = cobra_stretch,
    order=10
)
PresetTrainingExercise.objects.create(
    calculate_in = chest_stretch.calculate_in,
    required_value = 20,
    level = preset_training_set['preset_chest_beginner'].level,
    belong_to_training_set = preset_training_set['preset_chest_beginner'],
    exercise = chest_stretch,
    order=11
)

# arm beginner
PresetTrainingExercise.objects.create(
    calculate_in = side_arm_raise.calculate_in,
    required_value = 30,
    level = preset_training_set['preset_arm_beginner'].level,
    belong_to_training_set = preset_training_set['preset_arm_beginner'],
    exercise = side_arm_raise,
    order=1
)
PresetTrainingExercise.objects.create(
    calculate_in = triceps_dips.calculate_in,
    required_value = 10,
    level = preset_training_set['preset_arm_beginner'].level,
    belong_to_training_set = preset_training_set['preset_arm_beginner'],
    exercise = triceps_dips,
    order=2
)
PresetTrainingExercise.objects.create(
    calculate_in = arm_circle.calculate_in,
    required_value = 30,
    level = preset_training_set['preset_arm_beginner'].level,
    belong_to_training_set = preset_training_set['preset_arm_beginner'],
    exercise = arm_circle,
    order=3
)
PresetTrainingExercise.objects.create(
    calculate_in = arm_circle.calculate_in,
    required_value = 30,
    level = preset_training_set['preset_arm_beginner'].level,
    belong_to_training_set = preset_training_set['preset_arm_beginner'],
    exercise = arm_circle,
    order=4
)
PresetTrainingExercise.objects.create(
    calculate_in = diamond_push_up.calculate_in,
    required_value = 6,
    level = preset_training_set['preset_arm_beginner'].level,
    belong_to_training_set = preset_training_set['preset_arm_beginner'],
    exercise = diamond_push_up,
    order=5
)
PresetTrainingExercise.objects.create(
    calculate_in = jumping_jack.calculate_in,
    required_value = 30,
    level = preset_training_set['preset_arm_beginner'].level,
    belong_to_training_set = preset_training_set['preset_arm_beginner'],
    exercise = jumping_jack,
    order=6
)
PresetTrainingExercise.objects.create(
    calculate_in = chest_stretch.calculate_in,
    required_value = 15,
    level = preset_training_set['preset_arm_beginner'].level,
    belong_to_training_set = preset_training_set['preset_arm_beginner'],
    exercise = chest_stretch,
    order=7
)
PresetTrainingExercise.objects.create(
    calculate_in = biceps_legs_curl_left.calculate_in,
    required_value = 8,
    level = preset_training_set['preset_arm_beginner'].level,
    belong_to_training_set = preset_training_set['preset_arm_beginner'],
    exercise = biceps_legs_curl_left,
    order=8
)
PresetTrainingExercise.objects.create(
    calculate_in = biceps_legs_curl_right.calculate_in,
    required_value = 8,
    level = preset_training_set['preset_arm_beginner'].level,
    belong_to_training_set = preset_training_set['preset_arm_beginner'],
    exercise = biceps_legs_curl_right,
    order=9
)
PresetTrainingExercise.objects.create(
    calculate_in = diagonal_plank.calculate_in,
    required_value = 10,
    level = preset_training_set['preset_arm_beginner'].level,
    belong_to_training_set = preset_training_set['preset_arm_beginner'],
    exercise = diagonal_plank,
    order=10
)
PresetTrainingExercise.objects.create(
    calculate_in = punches.calculate_in,
    required_value = 30,
    level = preset_training_set['preset_arm_beginner'].level,
    belong_to_training_set = preset_training_set['preset_arm_beginner'],
    exercise = punches,
    order=11
)
PresetTrainingExercise.objects.create(
    calculate_in = push_up.calculate_in,
    required_value = 10,
    level = preset_training_set['preset_arm_beginner'].level,
    belong_to_training_set = preset_training_set['preset_arm_beginner'],
    exercise = push_up,
    order=12
)
PresetTrainingExercise.objects.create(
    calculate_in = inchworms.calculate_in,
    required_value = 8,
    level = preset_training_set['preset_arm_beginner'].level,
    belong_to_training_set = preset_training_set['preset_arm_beginner'],
    exercise = inchworms,
    order=13
)
PresetTrainingExercise.objects.create(
    calculate_in = push_up.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_arm_beginner'].level,
    belong_to_training_set = preset_training_set['preset_arm_beginner'],
    exercise = push_up,
    order=14
)
PresetTrainingExercise.objects.create(
    calculate_in = triceps_stretch_left.calculate_in,
    required_value = 30,
    level = preset_training_set['preset_arm_beginner'].level,
    belong_to_training_set = preset_training_set['preset_arm_beginner'],
    exercise = triceps_stretch_left,
    order=15
)
PresetTrainingExercise.objects.create(
    calculate_in = triceps_stretch_right.calculate_in,
    required_value = 30,
    level = preset_training_set['preset_arm_beginner'].level,
    belong_to_training_set = preset_training_set['preset_arm_beginner'],
    exercise = triceps_stretch_right,
    order=16
)

# leg beginner
PresetTrainingExercise.objects.create(
    calculate_in = jumping_squats.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_leg_beginner'].level,
    belong_to_training_set = preset_training_set['preset_leg_beginner'],
    exercise = jumping_squats,
    order=1
)
PresetTrainingExercise.objects.create(
    calculate_in = squats.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_leg_beginner'].level,
    belong_to_training_set = preset_training_set['preset_leg_beginner'],
    exercise = squats,
    order=2
)
PresetTrainingExercise.objects.create(
    calculate_in = squats.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_leg_beginner'].level,
    belong_to_training_set = preset_training_set['preset_leg_beginner'],
    exercise = squats,
    order=3
)
PresetTrainingExercise.objects.create(
    calculate_in = side_lying_leg_lift_left.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_leg_beginner'].level,
    belong_to_training_set = preset_training_set['preset_leg_beginner'],
    exercise = side_lying_leg_lift_left,
    order=4
)
PresetTrainingExercise.objects.create(
    calculate_in = side_lying_leg_lift_right.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_leg_beginner'].level,
    belong_to_training_set = preset_training_set['preset_leg_beginner'],
    exercise = side_lying_leg_lift_right,
    order=5
)
PresetTrainingExercise.objects.create(
    calculate_in = side_lying_leg_lift_left.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_leg_beginner'].level,
    belong_to_training_set = preset_training_set['preset_leg_beginner'],
    exercise = side_lying_leg_lift_left,
    order=6
)
PresetTrainingExercise.objects.create(
    calculate_in = side_lying_leg_lift_right.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_leg_beginner'].level,
    belong_to_training_set = preset_training_set['preset_leg_beginner'],
    exercise = side_lying_leg_lift_right,
    order=7
)
PresetTrainingExercise.objects.create(
    calculate_in = lunges.calculate_in,
    required_value = 14,
    level = preset_training_set['preset_leg_beginner'].level,
    belong_to_training_set = preset_training_set['preset_leg_beginner'],
    exercise = lunges,
    order=8
)
PresetTrainingExercise.objects.create(
    calculate_in = lunges.calculate_in,
    required_value = 14,
    level = preset_training_set['preset_leg_beginner'].level,
    belong_to_training_set = preset_training_set['preset_leg_beginner'],
    exercise = lunges,
    order=9
)
PresetTrainingExercise.objects.create(
    calculate_in = donkey_kick_left.calculate_in,
    required_value = 14,
    level = preset_training_set['preset_leg_beginner'].level,
    belong_to_training_set = preset_training_set['preset_leg_beginner'],
    exercise = donkey_kick_left,
    order=10
)
PresetTrainingExercise.objects.create(
    calculate_in = donkey_kick_right.calculate_in,
    required_value = 14,
    level = preset_training_set['preset_leg_beginner'].level,
    belong_to_training_set = preset_training_set['preset_leg_beginner'],
    exercise = donkey_kick_right,
    order=11
)
PresetTrainingExercise.objects.create(
    calculate_in = donkey_kick_left.calculate_in,
    required_value = 14,
    level = preset_training_set['preset_leg_beginner'].level,
    belong_to_training_set = preset_training_set['preset_leg_beginner'],
    exercise = donkey_kick_left,
    order=12
)
PresetTrainingExercise.objects.create(
    calculate_in = donkey_kick_right.calculate_in,
    required_value = 14,
    level = preset_training_set['preset_leg_beginner'].level,
    belong_to_training_set = preset_training_set['preset_leg_beginner'],
    exercise = donkey_kick_right,
    order=13
)
PresetTrainingExercise.objects.create(
    calculate_in = left_quad_stretch.calculate_in,
    required_value = 30,
    level = preset_training_set['preset_leg_beginner'].level,
    belong_to_training_set = preset_training_set['preset_leg_beginner'],
    exercise = left_quad_stretch,
    order=14
)
PresetTrainingExercise.objects.create(
    calculate_in = right_quad_stretch.calculate_in,
    required_value = 30,
    level = preset_training_set['preset_leg_beginner'].level,
    belong_to_training_set = preset_training_set['preset_leg_beginner'],
    exercise = right_quad_stretch,
    order=15
)
PresetTrainingExercise.objects.create(
    calculate_in = knee_to_chest_stretch_left.calculate_in,
    required_value = 30,
    level = preset_training_set['preset_leg_beginner'].level,
    belong_to_training_set = preset_training_set['preset_leg_beginner'],
    exercise = knee_to_chest_stretch_left,
    order=16
)
PresetTrainingExercise.objects.create(
    calculate_in = knee_to_chest_stretch_right.calculate_in,
    required_value = 30,
    level = preset_training_set['preset_leg_beginner'].level,
    belong_to_training_set = preset_training_set['preset_leg_beginner'],
    exercise = knee_to_chest_stretch_right,
    order=17
)
PresetTrainingExercise.objects.create(
    calculate_in = wall_calf_raise.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_leg_beginner'].level,
    belong_to_training_set = preset_training_set['preset_leg_beginner'],
    exercise = wall_calf_raise,
    order=18
)
PresetTrainingExercise.objects.create(
    calculate_in = wall_calf_raise.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_leg_beginner'].level,
    belong_to_training_set = preset_training_set['preset_leg_beginner'],
    exercise = wall_calf_raise,
    order=19
)

# shoulder & back beginner
PresetTrainingExercise.objects.create(
    calculate_in = jumping_jack.calculate_in,
    required_value = 30,
    level = preset_training_set['preset_back_and_shoulder_beginner'].level,
    belong_to_training_set = preset_training_set['preset_back_and_shoulder_beginner'],
    exercise = jumping_jack,
    order=1
)
PresetTrainingExercise.objects.create(
    calculate_in = superman_pulls.calculate_in,
    required_value = 14,
    level = preset_training_set['preset_back_and_shoulder_beginner'].level,
    belong_to_training_set = preset_training_set['preset_back_and_shoulder_beginner'],
    exercise = superman_pulls,
    order=2
)
PresetTrainingExercise.objects.create(
    calculate_in = side_arm_raise.calculate_in,
    required_value = 20,
    level = preset_training_set['preset_back_and_shoulder_beginner'].level,
    belong_to_training_set = preset_training_set['preset_back_and_shoulder_beginner'],
    exercise = side_arm_raise,
    order=3
)
PresetTrainingExercise.objects.create(
    calculate_in = knee_push_up.calculate_in,
    required_value = 14,
    level = preset_training_set['preset_back_and_shoulder_beginner'].level,
    belong_to_training_set = preset_training_set['preset_back_and_shoulder_beginner'],
    exercise = knee_push_up,
    order=4
)
PresetTrainingExercise.objects.create(
    calculate_in = side_lying_floor_stretch_left.calculate_in,
    required_value = 30,
    level = preset_training_set['preset_back_and_shoulder_beginner'].level,
    belong_to_training_set = preset_training_set['preset_back_and_shoulder_beginner'],
    exercise = side_lying_floor_stretch_left,
    order=5
)
PresetTrainingExercise.objects.create(
    calculate_in = side_lying_floor_stretch_right.calculate_in,
    required_value = 30,
    level = preset_training_set['preset_back_and_shoulder_beginner'].level,
    belong_to_training_set = preset_training_set['preset_back_and_shoulder_beginner'],
    exercise = side_lying_floor_stretch_right,
    order=6
)
PresetTrainingExercise.objects.create(
    calculate_in = superman_pulls.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_back_and_shoulder_beginner'].level,
    belong_to_training_set = preset_training_set['preset_back_and_shoulder_beginner'],
    exercise = superman_pulls,
    order=7
)
PresetTrainingExercise.objects.create(
    calculate_in = side_arm_raise.calculate_in,
    required_value = 20,
    level = preset_training_set['preset_back_and_shoulder_beginner'].level,
    belong_to_training_set = preset_training_set['preset_back_and_shoulder_beginner'],
    exercise = side_arm_raise,
    order=8
)
PresetTrainingExercise.objects.create(
    calculate_in = knee_push_up.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_back_and_shoulder_beginner'].level,
    belong_to_training_set = preset_training_set['preset_back_and_shoulder_beginner'],
    exercise = knee_push_up,
    order=9
)
PresetTrainingExercise.objects.create(
    calculate_in = cat_cow_pose.calculate_in,
    required_value = 30,
    level = preset_training_set['preset_back_and_shoulder_beginner'].level,
    belong_to_training_set = preset_training_set['preset_back_and_shoulder_beginner'],
    exercise = cat_cow_pose,
    order=10
)
PresetTrainingExercise.objects.create(
    calculate_in = triceps_push_up.calculate_in,
    required_value = 14,
    level = preset_training_set['preset_back_and_shoulder_beginner'].level,
    belong_to_training_set = preset_training_set['preset_back_and_shoulder_beginner'],
    exercise = triceps_push_up,
    order=11
)
PresetTrainingExercise.objects.create(
    calculate_in = rhomboid_squeeze.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_back_and_shoulder_beginner'].level,
    belong_to_training_set = preset_training_set['preset_back_and_shoulder_beginner'],
    exercise = rhomboid_squeeze,
    order=12
)
PresetTrainingExercise.objects.create(
    calculate_in = triceps_push_up.calculate_in,
    required_value = 14,
    level = preset_training_set['preset_back_and_shoulder_beginner'].level,
    belong_to_training_set = preset_training_set['preset_back_and_shoulder_beginner'],
    exercise = triceps_push_up,
    order=13
)
PresetTrainingExercise.objects.create(
    calculate_in = rhomboid_squeeze.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_back_and_shoulder_beginner'].level,
    belong_to_training_set = preset_training_set['preset_back_and_shoulder_beginner'],
    exercise = rhomboid_squeeze,
    order=14
)
PresetTrainingExercise.objects.create(
    calculate_in = child_pose.calculate_in,
    required_value = 30,
    level = preset_training_set['preset_back_and_shoulder_beginner'].level,
    belong_to_training_set = preset_training_set['preset_back_and_shoulder_beginner'],
    exercise = child_pose,
    order=15
)

# abs intermediate
PresetTrainingExercise.objects.create(
    calculate_in = jumping_jack.calculate_in,
    required_value = 30,
    level = preset_training_set['preset_abs_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_abs_intermediate'],
    exercise = jumping_jack,
    order=1
)
PresetTrainingExercise.objects.create(
    calculate_in = heel_touch.calculate_in,
    required_value = 26,
    level = preset_training_set['preset_abs_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_abs_intermediate'],
    exercise = heel_touch,
    order=2
)
PresetTrainingExercise.objects.create(
    calculate_in = crossover_crunch.calculate_in,
    required_value = 20,
    level = preset_training_set['preset_abs_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_abs_intermediate'],
    exercise = crossover_crunch,
    order=3
)
PresetTrainingExercise.objects.create(
    calculate_in = mountain_climber.calculate_in,
    required_value = 20,
    level = preset_training_set['preset_abs_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_abs_intermediate'],
    exercise = mountain_climber,
    order=4
)
PresetTrainingExercise.objects.create(
    calculate_in = side_bridges_left.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_abs_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_abs_intermediate'],
    exercise = side_bridges_left,
    order=5
)
PresetTrainingExercise.objects.create(
    calculate_in = side_bridges_right.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_abs_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_abs_intermediate'],
    exercise = side_bridges_right,
    order=6
)
PresetTrainingExercise.objects.create(
    calculate_in = butt_bridges.calculate_in,
    required_value = 20,
    level = preset_training_set['preset_abs_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_abs_intermediate'],
    exercise = butt_bridges,
    order=7
)
PresetTrainingExercise.objects.create(
    calculate_in = bicycle_crunches.calculate_in,
    required_value = 20,
    level = preset_training_set['preset_abs_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_abs_intermediate'],
    exercise = bicycle_crunches,
    order=8
)
PresetTrainingExercise.objects.create(
    calculate_in = v_up.calculate_in,
    required_value = 20,
    level = preset_training_set['preset_abs_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_abs_intermediate'],
    exercise = v_up,
    order=9
)
PresetTrainingExercise.objects.create(
    calculate_in = heel_touch.calculate_in,
    required_value = 26,
    level = preset_training_set['preset_abs_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_abs_intermediate'],
    exercise = heel_touch,
    order=10
)
PresetTrainingExercise.objects.create(
    calculate_in = abdominal_crunches.calculate_in,
    required_value = 20,
    level = preset_training_set['preset_abs_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_abs_intermediate'],
    exercise = abdominal_crunches,
    order=11
)
PresetTrainingExercise.objects.create(
    calculate_in = plank.calculate_in,
    required_value = 30,
    level = preset_training_set['preset_abs_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_abs_intermediate'],
    exercise = plank,
    order=12
)
PresetTrainingExercise.objects.create(
    calculate_in = crossover_crunch.calculate_in,
    required_value = 20,
    level = preset_training_set['preset_abs_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_abs_intermediate'],
    exercise = crossover_crunch,
    order=13
)
PresetTrainingExercise.objects.create(
    calculate_in = leg_raises.calculate_in,
    required_value = 16,
    level = preset_training_set['preset_abs_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_abs_intermediate'],
    exercise = leg_raises,
    order=14
)
PresetTrainingExercise.objects.create(
    calculate_in = bicycle_crunches.calculate_in,
    required_value = 20,
    level = preset_training_set['preset_abs_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_abs_intermediate'],
    exercise = bicycle_crunches,
    order=15
)
PresetTrainingExercise.objects.create(
    calculate_in = push_up_and_rotation.calculate_in,
    required_value = 20,
    level = preset_training_set['preset_abs_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_abs_intermediate'],
    exercise = push_up_and_rotation,
    order=16
)
PresetTrainingExercise.objects.create(
    calculate_in = side_plank_left.calculate_in,
    required_value = 20,
    level = preset_training_set['preset_abs_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_abs_intermediate'],
    exercise = side_plank_left,
    order=17
)
PresetTrainingExercise.objects.create(
    calculate_in = side_plank_right.calculate_in,
    required_value = 20,
    level = preset_training_set['preset_abs_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_abs_intermediate'],
    exercise = side_plank_right,
    order=18
)
PresetTrainingExercise.objects.create(
    calculate_in = cobra_stretch.calculate_in,
    required_value = 30,
    level = preset_training_set['preset_abs_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_abs_intermediate'],
    exercise = cobra_stretch,
    order=19
)
PresetTrainingExercise.objects.create(
    calculate_in = burpees.calculate_in,
    required_value = 20,
    level = preset_training_set['preset_abs_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_abs_intermediate'],
    exercise = burpees,
    order=20
)
PresetTrainingExercise.objects.create(
    calculate_in = bent_leg_twist.calculate_in,
    required_value = 20,
    level = preset_training_set['preset_abs_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_abs_intermediate'],
    exercise = bent_leg_twist,
    order=21
)

# chest intermediate
PresetTrainingExercise.objects.create(
    calculate_in = jumping_jack.calculate_in,
    required_value = 30,
    level = preset_training_set['preset_chest_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_chest_intermediate'],
    exercise = jumping_jack,
    order=1
)
PresetTrainingExercise.objects.create(
    calculate_in = knee_push_up.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_chest_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_chest_intermediate'],
    exercise = knee_push_up,
    order=2
)
PresetTrainingExercise.objects.create(
    calculate_in = push_up.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_chest_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_chest_intermediate'],
    exercise = push_up,
    order=3
)
PresetTrainingExercise.objects.create(
    calculate_in = wide_push_up.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_chest_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_chest_intermediate'],
    exercise = wide_push_up,
    order=4
)
PresetTrainingExercise.objects.create(
    calculate_in = hindu_push_up.calculate_in,
    required_value = 10,
    level = preset_training_set['preset_chest_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_chest_intermediate'],
    exercise = hindu_push_up,
    order=5
)
PresetTrainingExercise.objects.create(
    calculate_in = pike_push_up.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_chest_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_chest_intermediate'],
    exercise = pike_push_up,
    order=6
)
PresetTrainingExercise.objects.create(
    calculate_in = push_up_and_rotation.calculate_in,
    required_value = 10,
    level = preset_training_set['preset_chest_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_chest_intermediate'],
    exercise = push_up_and_rotation,
    order=7
)
PresetTrainingExercise.objects.create(
    calculate_in = knee_push_up.calculate_in,
    required_value = 10,
    level = preset_training_set['preset_chest_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_chest_intermediate'],
    exercise = knee_push_up,
    order=8
)
PresetTrainingExercise.objects.create(
    calculate_in = hindu_push_up.calculate_in,
    required_value = 10,
    level = preset_training_set['preset_chest_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_chest_intermediate'],
    exercise = hindu_push_up,
    order=9
)
PresetTrainingExercise.objects.create(
    calculate_in = decline_push_up.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_chest_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_chest_intermediate'],
    exercise = decline_push_up,
    order=10
)
PresetTrainingExercise.objects.create(
    calculate_in = pike_push_up.calculate_in,
    required_value = 10,
    level = preset_training_set['preset_chest_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_chest_intermediate'],
    exercise = pike_push_up,
    order=11
)
PresetTrainingExercise.objects.create(
    calculate_in = push_up.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_chest_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_chest_intermediate'],
    exercise = push_up,
    order=12
)
PresetTrainingExercise.objects.create(
    calculate_in = cobra_stretch.calculate_in,
    required_value = 30,
    level = preset_training_set['preset_chest_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_chest_intermediate'],
    exercise = cobra_stretch,
    order=13
)
PresetTrainingExercise.objects.create(
    calculate_in = chest_stretch.calculate_in,
    required_value = 30,
    level = preset_training_set['preset_chest_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_chest_intermediate'],
    exercise = chest_stretch,
    order=14
)

# arm intermediate
PresetTrainingExercise.objects.create(
    calculate_in = arm_circle.calculate_in,
    required_value = 30,
    level = preset_training_set['preset_arm_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_arm_intermediate'],
    exercise = arm_circle,
    order=1
)
PresetTrainingExercise.objects.create(
    calculate_in = arm_circle.calculate_in,
    required_value = 30,
    level = preset_training_set['preset_arm_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_arm_intermediate'],
    exercise = arm_circle,
    order=2
)
PresetTrainingExercise.objects.create(
    calculate_in = triceps_dips.calculate_in,
    required_value = 14,
    level = preset_training_set['preset_arm_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_arm_intermediate'],
    exercise = triceps_dips,
    order=3
)
PresetTrainingExercise.objects.create(
    calculate_in = push_up.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_arm_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_arm_intermediate'],
    exercise = push_up,
    order=4
)
PresetTrainingExercise.objects.create(
    calculate_in = left_hooks.calculate_in,
    required_value = 30,
    level = preset_training_set['preset_arm_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_arm_intermediate'],
    exercise = left_hooks,
    order=5
)
PresetTrainingExercise.objects.create(
    calculate_in = right_hooks.calculate_in,
    required_value = 30,
    level = preset_training_set['preset_arm_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_arm_intermediate'],
    exercise = right_hooks,
    order=6
)
PresetTrainingExercise.objects.create(
    calculate_in = push_up_and_rotation.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_arm_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_arm_intermediate'],
    exercise = push_up_and_rotation,
    order=7
)
PresetTrainingExercise.objects.create(
    calculate_in = biceps_legs_curl_left.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_arm_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_arm_intermediate'],
    exercise = biceps_legs_curl_left,
    order=8
)
PresetTrainingExercise.objects.create(
    calculate_in = biceps_legs_curl_right.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_arm_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_arm_intermediate'],
    exercise = biceps_legs_curl_right,
    order=9
)
PresetTrainingExercise.objects.create(
    calculate_in = triceps_dips.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_arm_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_arm_intermediate'],
    exercise = triceps_dips,
    order=10
)
PresetTrainingExercise.objects.create(
    calculate_in = push_up.calculate_in,
    required_value = 10,
    level = preset_training_set['preset_arm_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_arm_intermediate'],
    exercise = push_up,
    order=11
)
PresetTrainingExercise.objects.create(
    calculate_in = push_up_and_rotation.calculate_in,
    required_value = 10,
    level = preset_training_set['preset_arm_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_arm_intermediate'],
    exercise = push_up_and_rotation,
    order=12
)
PresetTrainingExercise.objects.create(
    calculate_in = biceps_legs_curl_left.calculate_in,
    required_value = 10,
    level = preset_training_set['preset_arm_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_arm_intermediate'],
    exercise = biceps_legs_curl_left,
    order=13
)
PresetTrainingExercise.objects.create(
    calculate_in = biceps_legs_curl_right.calculate_in,
    required_value = 10,
    level = preset_training_set['preset_arm_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_arm_intermediate'],
    exercise = biceps_legs_curl_right,
    order=14
)
PresetTrainingExercise.objects.create(
    calculate_in = skipping_without_ropes.calculate_in,
    required_value = 30,
    level = preset_training_set['preset_arm_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_arm_intermediate'],
    exercise = skipping_without_ropes,
    order=15
)
PresetTrainingExercise.objects.create(
    calculate_in = push_up.calculate_in,
    required_value = 14,
    level = preset_training_set['preset_arm_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_arm_intermediate'],
    exercise = push_up,
    order=16
)
PresetTrainingExercise.objects.create(
    calculate_in = burpees.calculate_in,
    required_value = 10,
    level = preset_training_set['preset_arm_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_arm_intermediate'],
    exercise = burpees,
    order=17
)
PresetTrainingExercise.objects.create(
    calculate_in = skipping_without_ropes.calculate_in,
    required_value = 30,
    level = preset_training_set['preset_arm_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_arm_intermediate'],
    exercise = skipping_without_ropes,
    order=18
)
PresetTrainingExercise.objects.create(
    calculate_in = push_up.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_arm_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_arm_intermediate'],
    exercise = push_up,
    order=19
)
PresetTrainingExercise.objects.create(
    calculate_in = burpees.calculate_in,
    required_value = 8,
    level = preset_training_set['preset_arm_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_arm_intermediate'],
    exercise = burpees,
    order=20
)
PresetTrainingExercise.objects.create(
    calculate_in = triceps_stretch_left.calculate_in,
    required_value = 30,
    level = preset_training_set['preset_arm_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_arm_intermediate'],
    exercise = triceps_stretch_left,
    order=21
)
PresetTrainingExercise.objects.create(
    calculate_in = triceps_stretch_right.calculate_in,
    required_value = 30,
    level = preset_training_set['preset_arm_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_arm_intermediate'],
    exercise = triceps_stretch_right,
    order=22
)

# legs intermediate
PresetTrainingExercise.objects.create(
    calculate_in = jumping_jack.calculate_in,
    required_value = 30,
    level = preset_training_set['preset_leg_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_leg_intermediate'],
    exercise = jumping_jack,
    order=1
)
PresetTrainingExercise.objects.create(
    calculate_in = squats.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_leg_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_leg_intermediate'],
    exercise = squats,
    order=2
)
PresetTrainingExercise.objects.create(
    calculate_in = squats.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_leg_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_leg_intermediate'],
    exercise = squats,
    order=3
)
PresetTrainingExercise.objects.create(
    calculate_in = squats.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_leg_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_leg_intermediate'],
    exercise = squats,
    order=4
)
PresetTrainingExercise.objects.create(
    calculate_in = fire_hydrant_left.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_leg_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_leg_intermediate'],
    exercise = fire_hydrant_left,
    order=5
)
PresetTrainingExercise.objects.create(
    calculate_in = fire_hydrant_right.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_leg_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_leg_intermediate'],
    exercise = fire_hydrant_right,
    order=6
)
PresetTrainingExercise.objects.create(
    calculate_in = fire_hydrant_left.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_leg_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_leg_intermediate'],
    exercise = fire_hydrant_left,
    order=7
)
PresetTrainingExercise.objects.create(
    calculate_in = fire_hydrant_right.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_leg_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_leg_intermediate'],
    exercise = fire_hydrant_right,
    order=8
)
PresetTrainingExercise.objects.create(
    calculate_in = fire_hydrant_left.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_leg_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_leg_intermediate'],
    exercise = fire_hydrant_left,
    order=9
)
PresetTrainingExercise.objects.create(
    calculate_in = fire_hydrant_right.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_leg_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_leg_intermediate'],
    exercise = fire_hydrant_right,
    order=10
)
PresetTrainingExercise.objects.create(
    calculate_in = lunges.calculate_in,
    required_value = 14,
    level = preset_training_set['preset_leg_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_leg_intermediate'],
    exercise = lunges,
    order=11
)
PresetTrainingExercise.objects.create(
    calculate_in = lunges.calculate_in,
    required_value = 14,
    level = preset_training_set['preset_leg_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_leg_intermediate'],
    exercise = lunges,
    order=12
)
PresetTrainingExercise.objects.create(
    calculate_in = side_lying_leg_lift_left.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_leg_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_leg_intermediate'],
    exercise = side_lying_leg_lift_left,
    order=13
)
PresetTrainingExercise.objects.create(
    calculate_in = side_lying_floor_stretch_right.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_leg_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_leg_intermediate'],
    exercise = side_lying_floor_stretch_right,
    order=14
)
PresetTrainingExercise.objects.create(
    calculate_in = side_lying_leg_lift_left.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_leg_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_leg_intermediate'],
    exercise = side_lying_leg_lift_left,
    order=15
)
PresetTrainingExercise.objects.create(
    calculate_in = side_lying_floor_stretch_right.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_leg_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_leg_intermediate'],
    exercise = side_lying_floor_stretch_right,
    order=16
)
PresetTrainingExercise.objects.create(
    calculate_in = sumo_squat.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_leg_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_leg_intermediate'],
    exercise = sumo_squat,
    order=17
)
PresetTrainingExercise.objects.create(
    calculate_in = sumo_squat.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_leg_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_leg_intermediate'],
    exercise = sumo_squat,
    order=18
)
PresetTrainingExercise.objects.create(
    calculate_in = sumo_squat.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_leg_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_leg_intermediate'],
    exercise = sumo_squat,
    order=19
)
PresetTrainingExercise.objects.create(
    calculate_in = flutter_kick.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_leg_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_leg_intermediate'],
    exercise = flutter_kick,
    order=20
)
PresetTrainingExercise.objects.create(
    calculate_in = flutter_kick.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_leg_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_leg_intermediate'],
    exercise = flutter_kick,
    order=21
)
PresetTrainingExercise.objects.create(
    calculate_in = flutter_kick.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_leg_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_leg_intermediate'],
    exercise = flutter_kick,
    order=22
)
PresetTrainingExercise.objects.create(
    calculate_in = wall_sit.calculate_in,
    required_value = 30,
    level = preset_training_set['preset_leg_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_leg_intermediate'],
    exercise = wall_sit,
    order=23
)
PresetTrainingExercise.objects.create(
    calculate_in = left_quad_stretch.calculate_in,
    required_value = 30,
    level = preset_training_set['preset_leg_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_leg_intermediate'],
    exercise = left_quad_stretch,
    order=24
)
PresetTrainingExercise.objects.create(
    calculate_in = right_quad_stretch.calculate_in,
    required_value = 30,
    level = preset_training_set['preset_leg_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_leg_intermediate'],
    exercise = right_quad_stretch,
    order=25
)
PresetTrainingExercise.objects.create(
    calculate_in = knee_to_chest_stretch_left.calculate_in,
    required_value = 30,
    level = preset_training_set['preset_leg_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_leg_intermediate'],
    exercise = knee_to_chest_stretch_left,
    order=26
)
PresetTrainingExercise.objects.create(
    calculate_in = right_quad_stretch.calculate_in,
    required_value = 30,
    level = preset_training_set['preset_leg_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_leg_intermediate'],
    exercise = right_quad_stretch,
    order=27
)
PresetTrainingExercise.objects.create(
    calculate_in = wall_calf_raise.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_leg_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_leg_intermediate'],
    exercise = wall_calf_raise,
    order=28
)
PresetTrainingExercise.objects.create(
    calculate_in = wall_calf_raise.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_leg_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_leg_intermediate'],
    exercise = wall_calf_raise,
    order=29
)
PresetTrainingExercise.objects.create(
    calculate_in = wall_calf_raise.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_leg_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_leg_intermediate'],
    exercise = wall_calf_raise,
    order=30
)

# back & shoulder intermediate
PresetTrainingExercise.objects.create(
    calculate_in = jumping_jack.calculate_in,
    required_value = 30,
    level = preset_training_set['preset_back_and_shoulder_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_back_and_shoulder_intermediate'],
    exercise = jumping_jack,
    order=1
)
PresetTrainingExercise.objects.create(
    calculate_in = triceps_kick_backs.calculate_in,
    required_value = 14,
    level = preset_training_set['preset_back_and_shoulder_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_back_and_shoulder_intermediate'],
    exercise = triceps_kick_backs,
    order=2
)
PresetTrainingExercise.objects.create(
    calculate_in = diamond_push_up.calculate_in,
    required_value = 14,
    level = preset_training_set['preset_back_and_shoulder_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_back_and_shoulder_intermediate'],
    exercise = diamond_push_up,
    order=3
)
PresetTrainingExercise.objects.create(
    calculate_in = superman_pulls.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_back_and_shoulder_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_back_and_shoulder_intermediate'],
    exercise = superman_pulls,
    order=4
)
PresetTrainingExercise.objects.create(
    calculate_in = triceps_dips.calculate_in,
    required_value = 16,
    level = preset_training_set['preset_back_and_shoulder_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_back_and_shoulder_intermediate'],
    exercise = triceps_dips,
    order=5
)
PresetTrainingExercise.objects.create(
    calculate_in = cat_cow_pose.calculate_in,
    required_value = 30,
    level = preset_training_set['preset_back_and_shoulder_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_back_and_shoulder_intermediate'],
    exercise = cat_cow_pose,
    order=6
)
PresetTrainingExercise.objects.create(
    calculate_in = triceps_kick_backs.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_back_and_shoulder_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_back_and_shoulder_intermediate'],
    exercise = triceps_kick_backs,
    order=7
)
PresetTrainingExercise.objects.create(
    calculate_in = push_up.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_back_and_shoulder_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_back_and_shoulder_intermediate'],
    exercise = push_up,
    order=8
)
PresetTrainingExercise.objects.create(
    calculate_in = rhomboid_squeeze.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_back_and_shoulder_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_back_and_shoulder_intermediate'],
    exercise = rhomboid_squeeze,
    order=9
)
PresetTrainingExercise.objects.create(
    calculate_in = triceps_dips.calculate_in,
    required_value = 14,
    level = preset_training_set['preset_back_and_shoulder_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_back_and_shoulder_intermediate'],
    exercise = triceps_dips,
    order=10
)
PresetTrainingExercise.objects.create(
    calculate_in = side_lying_floor_stretch_left.calculate_in,
    required_value = 30,
    level = preset_training_set['preset_back_and_shoulder_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_back_and_shoulder_intermediate'],
    exercise = side_lying_floor_stretch_left,
    order=11
)
PresetTrainingExercise.objects.create(
    calculate_in = side_lying_floor_stretch_right.calculate_in,
    required_value = 30,
    level = preset_training_set['preset_back_and_shoulder_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_back_and_shoulder_intermediate'],
    exercise = side_lying_floor_stretch_right,
    order=12
)
PresetTrainingExercise.objects.create(
    calculate_in = hindu_push_up.calculate_in,
    required_value = 14,
    level = preset_training_set['preset_back_and_shoulder_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_back_and_shoulder_intermediate'],
    exercise = hindu_push_up,
    order=13
)
PresetTrainingExercise.objects.create(
    calculate_in = swimmer_and_superman.calculate_in,
    required_value = 14,
    level = preset_training_set['preset_back_and_shoulder_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_back_and_shoulder_intermediate'],
    exercise = swimmer_and_superman,
    order=14
)
PresetTrainingExercise.objects.create(
    calculate_in = hindu_push_up.calculate_in,
    required_value = 14,
    level = preset_training_set['preset_back_and_shoulder_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_back_and_shoulder_intermediate'],
    exercise = hindu_push_up,
    order=15
)
PresetTrainingExercise.objects.create(
    calculate_in = swimmer_and_superman.calculate_in,
    required_value = 14,
    level = preset_training_set['preset_back_and_shoulder_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_back_and_shoulder_intermediate'],
    exercise = swimmer_and_superman,
    order=16
)
PresetTrainingExercise.objects.create(
    calculate_in = child_pose.calculate_in,
    required_value = 30,
    level = preset_training_set['preset_back_and_shoulder_intermediate'].level,
    belong_to_training_set = preset_training_set['preset_back_and_shoulder_intermediate'],
    exercise = child_pose,
    order=17
)

# abs advance
PresetTrainingExercise.objects.create(
    calculate_in = jumping_jack.calculate_in,
    required_value = 30,
    level = preset_training_set['preset_abs_advance'].level,
    belong_to_training_set = preset_training_set['preset_abs_advance'],
    exercise = jumping_jack,
    order=1
)
PresetTrainingExercise.objects.create(
    calculate_in = sit_up.calculate_in,
    required_value = 20,
    level = preset_training_set['preset_abs_advance'].level,
    belong_to_training_set = preset_training_set['preset_abs_advance'],
    exercise = sit_up,
    order=2
)
PresetTrainingExercise.objects.create(
    calculate_in = side_bridges_left.calculate_in,
    required_value = 20,
    level = preset_training_set['preset_abs_advance'].level,
    belong_to_training_set = preset_training_set['preset_abs_advance'],
    exercise = side_bridges_left,
    order=3
)
PresetTrainingExercise.objects.create(
    calculate_in = side_bridges_right.calculate_in,
    required_value = 20,
    level = preset_training_set['preset_abs_advance'].level,
    belong_to_training_set = preset_training_set['preset_abs_advance'],
    exercise = side_bridges_right,
    order=4
)
PresetTrainingExercise.objects.create(
    calculate_in = abdominal_crunches.calculate_in,
    required_value = 16,
    level = preset_training_set['preset_abs_advance'].level,
    belong_to_training_set = preset_training_set['preset_abs_advance'],
    exercise = abdominal_crunches,
    order=5
)
PresetTrainingExercise.objects.create(
    calculate_in = bicycle_crunches.calculate_in,
    required_value = 24,
    level = preset_training_set['preset_abs_advance'].level,
    belong_to_training_set = preset_training_set['preset_abs_advance'],
    exercise = bicycle_crunches,
    order=6
)
PresetTrainingExercise.objects.create(
    calculate_in = side_plank_right.calculate_in,
    required_value = 20,
    level = preset_training_set['preset_abs_advance'].level,
    belong_to_training_set = preset_training_set['preset_abs_advance'],
    exercise = side_plank_right,
    order=7
)
PresetTrainingExercise.objects.create(
    calculate_in = side_plank_left.calculate_in,
    required_value = 20,
    level = preset_training_set['preset_abs_advance'].level,
    belong_to_training_set = preset_training_set['preset_abs_advance'],
    exercise = side_plank_left,
    order=8
)
PresetTrainingExercise.objects.create(
    calculate_in = v_up.calculate_in,
    required_value = 18,
    level = preset_training_set['preset_abs_advance'].level,
    belong_to_training_set = preset_training_set['preset_abs_advance'],
    exercise = v_up,
    order=9
)
PresetTrainingExercise.objects.create(
    calculate_in = push_up_and_rotation.calculate_in,
    required_value = 24,
    level = preset_training_set['preset_abs_advance'].level,
    belong_to_training_set = preset_training_set['preset_abs_advance'],
    exercise = push_up_and_rotation,
    order=10
)
PresetTrainingExercise.objects.create(
    calculate_in = russian_twist.calculate_in,
    required_value = 16,
    level = preset_training_set['preset_abs_advance'].level,
    belong_to_training_set = preset_training_set['preset_abs_advance'],
    exercise = russian_twist,
    order=11
)
PresetTrainingExercise.objects.create(
    calculate_in = abdominal_crunches.calculate_in,
    required_value = 16,
    level = preset_training_set['preset_abs_advance'].level,
    belong_to_training_set = preset_training_set['preset_abs_advance'],
    exercise = abdominal_crunches,
    order=12
)
PresetTrainingExercise.objects.create(
    calculate_in = butt_bridges.calculate_in,
    required_value = 20,
    level = preset_training_set['preset_abs_advance'].level,
    belong_to_training_set = preset_training_set['preset_abs_advance'],
    exercise = butt_bridges,
    order=13
)
PresetTrainingExercise.objects.create(
    calculate_in = heel_touch.calculate_in,
    required_value = 20,
    level = preset_training_set['preset_abs_advance'].level,
    belong_to_training_set = preset_training_set['preset_abs_advance'],
    exercise = heel_touch,
    order=14
)
PresetTrainingExercise.objects.create(
    calculate_in = mountain_climber.calculate_in,
    required_value = 20,
    level = preset_training_set['preset_abs_advance'].level,
    belong_to_training_set = preset_training_set['preset_abs_advance'],
    exercise = mountain_climber,
    order=15
)
PresetTrainingExercise.objects.create(
    calculate_in = crossover_crunch.calculate_in,
    required_value = 20,
    level = preset_training_set['preset_abs_advance'].level,
    belong_to_training_set = preset_training_set['preset_abs_advance'],
    exercise = crossover_crunch,
    order=16
)
PresetTrainingExercise.objects.create(
    calculate_in = v_up.calculate_in,
    required_value = 16,
    level = preset_training_set['preset_abs_advance'].level,
    belong_to_training_set = preset_training_set['preset_abs_advance'],
    exercise = v_up,
    order=17
)
PresetTrainingExercise.objects.create(
    calculate_in = plank.calculate_in,
    required_value = 60,
    level = preset_training_set['preset_abs_advance'].level,
    belong_to_training_set = preset_training_set['preset_abs_advance'],
    exercise = plank,
    order=18
)
PresetTrainingExercise.objects.create(
    calculate_in = cobra_stretch.calculate_in,
    required_value = 30,
    level = preset_training_set['preset_abs_advance'].level,
    belong_to_training_set = preset_training_set['preset_abs_advance'],
    exercise = cobra_stretch,
    order=19
)
PresetTrainingExercise.objects.create(
    calculate_in = burpees.calculate_in,
    required_value = 20,
    level = preset_training_set['preset_abs_advance'].level,
    belong_to_training_set = preset_training_set['preset_abs_advance'],
    exercise = burpees,
    order=20
)
PresetTrainingExercise.objects.create(
    calculate_in = bent_leg_twist.calculate_in,
    required_value = 20,
    level = preset_training_set['preset_abs_advance'].level,
    belong_to_training_set = preset_training_set['preset_abs_advance'],
    exercise = bent_leg_twist,
    order=21
)

# chest advance
PresetTrainingExercise.objects.create(
    calculate_in = jumping_jack.calculate_in,
    required_value = 30,
    level = preset_training_set['preset_chest_advance'].level,
    belong_to_training_set = preset_training_set['preset_chest_advance'],
    exercise = jumping_jack,
    order=1
)
PresetTrainingExercise.objects.create(
    calculate_in = arm_circle.calculate_in,
    required_value = 20,
    level = preset_training_set['preset_chest_advance'].level,
    belong_to_training_set = preset_training_set['preset_chest_advance'],
    exercise = arm_circle,
    order=2
)
PresetTrainingExercise.objects.create(
    calculate_in = pike_push_up.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_chest_advance'].level,
    belong_to_training_set = preset_training_set['preset_chest_advance'],
    exercise = pike_push_up,
    order=3
)
PresetTrainingExercise.objects.create(
    calculate_in = burpees.calculate_in,
    required_value = 10,
    level = preset_training_set['preset_chest_advance'].level,
    belong_to_training_set = preset_training_set['preset_chest_advance'],
    exercise = burpees,
    order=4
)
PresetTrainingExercise.objects.create(
    calculate_in = push_up.calculate_in,
    required_value =16,
    level = preset_training_set['preset_chest_advance'].level,
    belong_to_training_set = preset_training_set['preset_chest_advance'],
    exercise = push_up,
    order=5
)
PresetTrainingExercise.objects.create(
    calculate_in = hindu_push_up.calculate_in,
    required_value = 15,
    level = preset_training_set['preset_chest_advance'].level,
    belong_to_training_set = preset_training_set['preset_chest_advance'],
    exercise = hindu_push_up,
    order=6
)
PresetTrainingExercise.objects.create(
    calculate_in = push_up_and_rotation.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_chest_advance'].level,
    belong_to_training_set = preset_training_set['preset_chest_advance'],
    exercise = push_up_and_rotation,
    order=7
)
PresetTrainingExercise.objects.create(
    calculate_in = diamond_push_up.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_chest_advance'].level,
    belong_to_training_set = preset_training_set['preset_chest_advance'],
    exercise = diamond_push_up,
    order=8
)
PresetTrainingExercise.objects.create(
    calculate_in = diamond_push_up.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_chest_advance'].level,
    belong_to_training_set = preset_training_set['preset_chest_advance'],
    exercise = diamond_push_up,
    order=9
)
PresetTrainingExercise.objects.create(
    calculate_in = hindu_push_up.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_chest_advance'].level,
    belong_to_training_set = preset_training_set['preset_chest_advance'],
    exercise = hindu_push_up,
    order=10
)
PresetTrainingExercise.objects.create(
    calculate_in = supine_push_ups.calculate_in,
    required_value = 20,
    level = preset_training_set['preset_chest_advance'].level,
    belong_to_training_set = preset_training_set['preset_chest_advance'],
    exercise = supine_push_ups,
    order=11
)
PresetTrainingExercise.objects.create(
    calculate_in = decline_push_up.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_chest_advance'].level,
    belong_to_training_set = preset_training_set['preset_chest_advance'],
    exercise = decline_push_up,
    order=12
)
PresetTrainingExercise.objects.create(
    calculate_in = burpees.calculate_in,
    required_value = 10,
    level = preset_training_set['preset_chest_advance'].level,
    belong_to_training_set = preset_training_set['preset_chest_advance'],
    exercise = burpees,
    order=13
)
PresetTrainingExercise.objects.create(
    calculate_in = decline_push_up.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_chest_advance'].level,
    belong_to_training_set = preset_training_set['preset_chest_advance'],
    exercise = decline_push_up,
    order=14
)
PresetTrainingExercise.objects.create(
    calculate_in = cobra_stretch.calculate_in,
    required_value = 30,
    level = preset_training_set['preset_chest_advance'].level,
    belong_to_training_set = preset_training_set['preset_chest_advance'],
    exercise = cobra_stretch,
    order=15
)
PresetTrainingExercise.objects.create(
    calculate_in = chest_stretch.calculate_in,
    required_value = 30,
    level = preset_training_set['preset_chest_advance'].level,
    belong_to_training_set = preset_training_set['preset_chest_advance'],
    exercise = chest_stretch,
    order=16
)

# arm advance
PresetTrainingExercise.objects.create(
    calculate_in = arm_circle.calculate_in,
    required_value = 30,
    level = preset_training_set['preset_arm_advance'].level,
    belong_to_training_set = preset_training_set['preset_arm_advance'],
    exercise = arm_circle,
    order=1
)
PresetTrainingExercise.objects.create(
    calculate_in = arm_circle.calculate_in,
    required_value = 30,
    level = preset_training_set['preset_arm_advance'].level,
    belong_to_training_set = preset_training_set['preset_arm_advance'],
    exercise = arm_circle,
    order=2
)
PresetTrainingExercise.objects.create(
    calculate_in = skipping_without_ropes.calculate_in,
    required_value = 30,
    level = preset_training_set['preset_arm_advance'].level,
    belong_to_training_set = preset_training_set['preset_arm_advance'],
    exercise = skipping_without_ropes,
    order=3
)
PresetTrainingExercise.objects.create(
    calculate_in = biceps_legs_curl_left.calculate_in,
    required_value = 16,
    level = preset_training_set['preset_arm_advance'].level,
    belong_to_training_set = preset_training_set['preset_arm_advance'],
    exercise = biceps_legs_curl_left,
    order=4
)
PresetTrainingExercise.objects.create(
    calculate_in = biceps_legs_curl_right.calculate_in,
    required_value = 16,
    level = preset_training_set['preset_arm_advance'].level,
    belong_to_training_set = preset_training_set['preset_arm_advance'],
    exercise = biceps_legs_curl_right,
    order=5
)
PresetTrainingExercise.objects.create(
    calculate_in = burpees.calculate_in,
    required_value = 16,
    level = preset_training_set['preset_arm_advance'].level,
    belong_to_training_set = preset_training_set['preset_arm_advance'],
    exercise = burpees,
    order=6
)
PresetTrainingExercise.objects.create(
    calculate_in = arm_curls_crunch_left.calculate_in,
    required_value = 14,
    level = preset_training_set['preset_arm_advance'].level,
    belong_to_training_set = preset_training_set['preset_arm_advance'],
    exercise = arm_curls_crunch_left,
    order=7
)
PresetTrainingExercise.objects.create(
    calculate_in = arm_curls_crunch_right.calculate_in,
    required_value = 14,
    level = preset_training_set['preset_arm_advance'].level,
    belong_to_training_set = preset_training_set['preset_arm_advance'],
    exercise = arm_curls_crunch_right,
    order=8
)
PresetTrainingExercise.objects.create(
    calculate_in = triceps_dips.calculate_in,
    required_value = 18,
    level = preset_training_set['preset_arm_advance'].level,
    belong_to_training_set = preset_training_set['preset_arm_advance'],
    exercise = triceps_dips,
    order=9
)
PresetTrainingExercise.objects.create(
    calculate_in = left_hooks.calculate_in,
    required_value = 30,
    level = preset_training_set['preset_arm_advance'].level,
    belong_to_training_set = preset_training_set['preset_arm_advance'],
    exercise = left_hooks,
    order=10
)
PresetTrainingExercise.objects.create(
    calculate_in = right_hooks.calculate_in,
    required_value = 30,
    level = preset_training_set['preset_arm_advance'].level,
    belong_to_training_set = preset_training_set['preset_arm_advance'],
    exercise = right_hooks,
    order=11
)
PresetTrainingExercise.objects.create(
    calculate_in = diamond_push_up.calculate_in,
    required_value = 14,
    level = preset_training_set['preset_arm_advance'].level,
    belong_to_training_set = preset_training_set['preset_arm_advance'],
    exercise = diamond_push_up,
    order=12
)
PresetTrainingExercise.objects.create(
    calculate_in = triceps_kick_backs.calculate_in,
    required_value = 16,
    level = preset_training_set['preset_arm_advance'].level,
    belong_to_training_set = preset_training_set['preset_arm_advance'],
    exercise = triceps_kick_backs,
    order=13
)
PresetTrainingExercise.objects.create(
    calculate_in = triceps_dips.calculate_in,
    required_value = 16,
    level = preset_training_set['preset_arm_advance'].level,
    belong_to_training_set = preset_training_set['preset_arm_advance'],
    exercise = triceps_dips,
    order=14
)
PresetTrainingExercise.objects.create(
    calculate_in = burpees.calculate_in,
    required_value = 16,
    level = preset_training_set['preset_arm_advance'].level,
    belong_to_training_set = preset_training_set['preset_arm_advance'],
    exercise = burpees,
    order=16
)
PresetTrainingExercise.objects.create(
    calculate_in = arm_curls_crunch_left.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_arm_advance'].level,
    belong_to_training_set = preset_training_set['preset_arm_advance'],
    exercise = arm_curls_crunch_left,
    order=17
)
PresetTrainingExercise.objects.create(
    calculate_in = arm_curls_crunch_right.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_arm_advance'].level,
    belong_to_training_set = preset_training_set['preset_arm_advance'],
    exercise = arm_curls_crunch_right,
    order=18
)
PresetTrainingExercise.objects.create(
    calculate_in = push_up.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_arm_advance'].level,
    belong_to_training_set = preset_training_set['preset_arm_advance'],
    exercise = push_up,
    order=19
)
PresetTrainingExercise.objects.create(
    calculate_in = triceps_kick_backs.calculate_in,
    required_value = 16,
    level = preset_training_set['preset_arm_advance'].level,
    belong_to_training_set = preset_training_set['preset_arm_advance'],
    exercise = triceps_kick_backs,
    order=20
)
PresetTrainingExercise.objects.create(
    calculate_in = doorways_curls.calculate_in,
    required_value = 8,
    level = preset_training_set['preset_arm_advance'].level,
    belong_to_training_set = preset_training_set['preset_arm_advance'],
    exercise = doorways_curls,
    order=21
)
PresetTrainingExercise.objects.create(
    calculate_in = doorways_curls.calculate_in,
    required_value = 8,
    level = preset_training_set['preset_arm_advance'].level,
    belong_to_training_set = preset_training_set['preset_arm_advance'],
    exercise = doorways_curls,
    order=22
)
PresetTrainingExercise.objects.create(
    calculate_in = plank.calculate_in,
    required_value = 30,
    level = preset_training_set['preset_arm_advance'].level,
    belong_to_training_set = preset_training_set['preset_arm_advance'],
    exercise = plank,
    order=23
)
PresetTrainingExercise.objects.create(
    calculate_in = burpees.calculate_in,
    required_value = 20,
    level = preset_training_set['preset_arm_advance'].level,
    belong_to_training_set = preset_training_set['preset_arm_advance'],
    exercise = burpees,
    order=24
)
PresetTrainingExercise.objects.create(
    calculate_in = push_up_and_rotation.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_arm_advance'].level,
    belong_to_training_set = preset_training_set['preset_arm_advance'],
    exercise = push_up_and_rotation,
    order=25
)
PresetTrainingExercise.objects.create(
    calculate_in = triceps_stretch_left.calculate_in,
    required_value = 30,
    level = preset_training_set['preset_arm_advance'].level,
    belong_to_training_set = preset_training_set['preset_arm_advance'],
    exercise = triceps_stretch_left,
    order=26
)
PresetTrainingExercise.objects.create(
    calculate_in = triceps_stretch_right.calculate_in,
    required_value = 30,
    level = preset_training_set['preset_arm_advance'].level,
    belong_to_training_set = preset_training_set['preset_arm_advance'],
    exercise = triceps_stretch_right,
    order=27
)

# legs advance
PresetTrainingExercise.objects.create(
    calculate_in = burpees.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_leg_advance'].level,
    belong_to_training_set = preset_training_set['preset_leg_advance'],
    exercise = burpees,
    order=1
)
PresetTrainingExercise.objects.create(
    calculate_in = squats.calculate_in,
    required_value = 14,
    level = preset_training_set['preset_leg_advance'].level,
    belong_to_training_set = preset_training_set['preset_leg_advance'],
    exercise = squats,
    order=2
)
PresetTrainingExercise.objects.create(
    calculate_in = squats.calculate_in,
    required_value = 14,
    level = preset_training_set['preset_leg_advance'].level,
    belong_to_training_set = preset_training_set['preset_leg_advance'],
    exercise = squats,
    order=3
)
PresetTrainingExercise.objects.create(
    calculate_in = squats.calculate_in,
    required_value = 14,
    level = preset_training_set['preset_leg_advance'].level,
    belong_to_training_set = preset_training_set['preset_leg_advance'],
    exercise = squats,
    order=4
)
PresetTrainingExercise.objects.create(
    calculate_in = fire_hydrant_left.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_leg_advance'].level,
    belong_to_training_set = preset_training_set['preset_leg_advance'],
    exercise = fire_hydrant_left,
    order=5
)
PresetTrainingExercise.objects.create(
    calculate_in = fire_hydrant_right.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_leg_advance'].level,
    belong_to_training_set = preset_training_set['preset_leg_advance'],
    exercise = fire_hydrant_right,
    order=6
)
PresetTrainingExercise.objects.create(
    calculate_in = fire_hydrant_left.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_leg_advance'].level,
    belong_to_training_set = preset_training_set['preset_leg_advance'],
    exercise = fire_hydrant_left,
    order=7
)
PresetTrainingExercise.objects.create(
    calculate_in = fire_hydrant_right.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_leg_advance'].level,
    belong_to_training_set = preset_training_set['preset_leg_advance'],
    exercise = fire_hydrant_right,
    order=8
)
PresetTrainingExercise.objects.create(
    calculate_in = fire_hydrant_left.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_leg_advance'].level,
    belong_to_training_set = preset_training_set['preset_leg_advance'],
    exercise = fire_hydrant_left,
    order=9
)
PresetTrainingExercise.objects.create(
    calculate_in = fire_hydrant_right.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_leg_advance'].level,
    belong_to_training_set = preset_training_set['preset_leg_advance'],
    exercise = fire_hydrant_right,
    order=10
)
PresetTrainingExercise.objects.create(
    calculate_in = curtsy_lunges.calculate_in,
    required_value = 14,
    level = preset_training_set['preset_leg_advance'].level,
    belong_to_training_set = preset_training_set['preset_leg_advance'],
    exercise = curtsy_lunges,
    order=11
)
PresetTrainingExercise.objects.create(
    calculate_in = curtsy_lunges.calculate_in,
    required_value = 14,
    level = preset_training_set['preset_leg_advance'].level,
    belong_to_training_set = preset_training_set['preset_leg_advance'],
    exercise = curtsy_lunges,
    order=12
)
PresetTrainingExercise.objects.create(
    calculate_in = curtsy_lunges.calculate_in,
    required_value = 14,
    level = preset_training_set['preset_leg_advance'].level,
    belong_to_training_set = preset_training_set['preset_leg_advance'],
    exercise = curtsy_lunges,
    order=13
)
PresetTrainingExercise.objects.create(
    calculate_in = side_lying_leg_lift_left.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_leg_advance'].level,
    belong_to_training_set = preset_training_set['preset_leg_advance'],
    exercise = side_lying_leg_lift_left,
    order=14
)
PresetTrainingExercise.objects.create(
    calculate_in = side_lying_leg_lift_right.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_leg_advance'].level,
    belong_to_training_set = preset_training_set['preset_leg_advance'],
    exercise = side_lying_leg_lift_right,
    order=15
)
PresetTrainingExercise.objects.create(
    calculate_in = side_lying_leg_lift_left.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_leg_advance'].level,
    belong_to_training_set = preset_training_set['preset_leg_advance'],
    exercise = side_lying_leg_lift_left,
    order=16
)
PresetTrainingExercise.objects.create(
    calculate_in = side_lying_leg_lift_right.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_leg_advance'].level,
    belong_to_training_set = preset_training_set['preset_leg_advance'],
    exercise = side_lying_leg_lift_right,
    order=17
)
PresetTrainingExercise.objects.create(
    calculate_in = side_lying_leg_lift_left.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_leg_advance'].level,
    belong_to_training_set = preset_training_set['preset_leg_advance'],
    exercise = side_lying_leg_lift_left,
    order=18
)
PresetTrainingExercise.objects.create(
    calculate_in = side_lying_leg_lift_right.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_leg_advance'].level,
    belong_to_training_set = preset_training_set['preset_leg_advance'],
    exercise = side_lying_leg_lift_right,
    order=19
)
PresetTrainingExercise.objects.create(
    calculate_in = jumping_squats.calculate_in,
    required_value = 14,
    level = preset_training_set['preset_leg_advance'].level,
    belong_to_training_set = preset_training_set['preset_leg_advance'],
    exercise = jumping_squats,
    order=20
)
PresetTrainingExercise.objects.create(
    calculate_in = jumping_squats.calculate_in,
    required_value = 14,
    level = preset_training_set['preset_leg_advance'].level,
    belong_to_training_set = preset_training_set['preset_leg_advance'],
    exercise = jumping_squats,
    order=21
)
PresetTrainingExercise.objects.create(
    calculate_in = jumping_squats.calculate_in,
    required_value = 14,
    level = preset_training_set['preset_leg_advance'].level,
    belong_to_training_set = preset_training_set['preset_leg_advance'],
    exercise = jumping_squats,
    order=22
)
PresetTrainingExercise.objects.create(
    calculate_in = donkey_kick_left.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_leg_advance'].level,
    belong_to_training_set = preset_training_set['preset_leg_advance'],
    exercise = donkey_kick_left,
    order=23
)
PresetTrainingExercise.objects.create(
    calculate_in = donkey_kick_right.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_leg_advance'].level,
    belong_to_training_set = preset_training_set['preset_leg_advance'],
    exercise = donkey_kick_right,
    order=24
)
PresetTrainingExercise.objects.create(
    calculate_in = donkey_kick_left.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_leg_advance'].level,
    belong_to_training_set = preset_training_set['preset_leg_advance'],
    exercise = donkey_kick_left,
    order=25
)
PresetTrainingExercise.objects.create(
    calculate_in = donkey_kick_right.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_leg_advance'].level,
    belong_to_training_set = preset_training_set['preset_leg_advance'],
    exercise = donkey_kick_right,
    order=26
)
PresetTrainingExercise.objects.create(
    calculate_in = donkey_kick_left.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_leg_advance'].level,
    belong_to_training_set = preset_training_set['preset_leg_advance'],
    exercise = donkey_kick_left,
    order=27
)
PresetTrainingExercise.objects.create(
    calculate_in = donkey_kick_right.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_leg_advance'].level,
    belong_to_training_set = preset_training_set['preset_leg_advance'],
    exercise = donkey_kick_right,
    order=28
)
PresetTrainingExercise.objects.create(
    calculate_in = wall_sit.calculate_in,
    required_value = 30,
    level = preset_training_set['preset_leg_advance'].level,
    belong_to_training_set = preset_training_set['preset_leg_advance'],
    exercise = wall_sit,
    order=29
)
PresetTrainingExercise.objects.create(
    calculate_in = left_quad_stretch.calculate_in,
    required_value = 30,
    level = preset_training_set['preset_leg_advance'].level,
    belong_to_training_set = preset_training_set['preset_leg_advance'],
    exercise = left_quad_stretch,
    order=30
)
PresetTrainingExercise.objects.create(
    calculate_in = right_quad_stretch.calculate_in,
    required_value = 30,
    level = preset_training_set['preset_leg_advance'].level,
    belong_to_training_set = preset_training_set['preset_leg_advance'],
    exercise = right_quad_stretch,
    order=31
)
PresetTrainingExercise.objects.create(
    calculate_in = v_up.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_leg_advance'].level,
    belong_to_training_set = preset_training_set['preset_leg_advance'],
    exercise = v_up,
    order=32
)
PresetTrainingExercise.objects.create(
    calculate_in = wall_calf_raise.calculate_in,
    required_value = 16,
    level = preset_training_set['preset_leg_advance'].level,
    belong_to_training_set = preset_training_set['preset_leg_advance'],
    exercise = wall_calf_raise,
    order=33
)
PresetTrainingExercise.objects.create(
    calculate_in = wall_calf_raise.calculate_in,
    required_value = 16,
    level = preset_training_set['preset_leg_advance'].level,
    belong_to_training_set = preset_training_set['preset_leg_advance'],
    exercise = wall_calf_raise,
    order=34
)
PresetTrainingExercise.objects.create(
    calculate_in = wall_calf_raise.calculate_in,
    required_value = 16,
    level = preset_training_set['preset_leg_advance'].level,
    belong_to_training_set = preset_training_set['preset_leg_advance'],
    exercise = wall_calf_raise,
    order=35
)
PresetTrainingExercise.objects.create(
    calculate_in = wall_sit.calculate_in,
    required_value = 30,
    level = preset_training_set['preset_leg_advance'].level,
    belong_to_training_set = preset_training_set['preset_leg_advance'],
    exercise = wall_sit,
    order=36
)
PresetTrainingExercise.objects.create(
    calculate_in = swimmer_and_superman.calculate_in,
    required_value = 16,
    level = preset_training_set['preset_leg_advance'].level,
    belong_to_training_set = preset_training_set['preset_leg_advance'],
    exercise = swimmer_and_superman,
    order=37
)
PresetTrainingExercise.objects.create(
    calculate_in = bicycle_crunches.calculate_in,
    required_value = 16,
    level = preset_training_set['preset_leg_advance'].level,
    belong_to_training_set = preset_training_set['preset_leg_advance'],
    exercise = bicycle_crunches,
    order=38
)
PresetTrainingExercise.objects.create(
    calculate_in = swimmer_and_superman.calculate_in,
    required_value = 16,
    level = preset_training_set['preset_leg_advance'].level,
    belong_to_training_set = preset_training_set['preset_leg_advance'],
    exercise = swimmer_and_superman,
    order=39
)
PresetTrainingExercise.objects.create(
    calculate_in = bicycle_crunches.calculate_in,
    required_value = 16,
    level = preset_training_set['preset_leg_advance'].level,
    belong_to_training_set = preset_training_set['preset_leg_advance'],
    exercise = bicycle_crunches,
    order=40
)
PresetTrainingExercise.objects.create(
    calculate_in = wall_sit.calculate_in,
    required_value = 30,
    level = preset_training_set['preset_leg_advance'].level,
    belong_to_training_set = preset_training_set['preset_leg_advance'],
    exercise = wall_sit,
    order=41
)

# back & shoulder advance
PresetTrainingExercise.objects.create(
    calculate_in = jumping_jack.calculate_in,
    required_value = 30,
    level = preset_training_set['preset_back_and_shoulder_advance'].level,
    belong_to_training_set = preset_training_set['preset_back_and_shoulder_advance'],
    exercise = jumping_jack,
    order=1
)
PresetTrainingExercise.objects.create(
    calculate_in = rhomboid_squeeze.calculate_in,
    required_value = 14,
    level = preset_training_set['preset_back_and_shoulder_advance'].level,
    belong_to_training_set = preset_training_set['preset_back_and_shoulder_advance'],
    exercise = rhomboid_squeeze,
    order=2
)
PresetTrainingExercise.objects.create(
    calculate_in = pike_push_up.calculate_in,
    required_value = 14,
    level = preset_training_set['preset_back_and_shoulder_advance'].level,
    belong_to_training_set = preset_training_set['preset_back_and_shoulder_advance'],
    exercise = pike_push_up,
    order=3
)
PresetTrainingExercise.objects.create(
    calculate_in = cobra_stretch.calculate_in,
    required_value = 30,
    level = preset_training_set['preset_back_and_shoulder_advance'].level,
    belong_to_training_set = preset_training_set['preset_back_and_shoulder_advance'],
    exercise = cobra_stretch,
    order=4
)
PresetTrainingExercise.objects.create(
    calculate_in = inchworms.calculate_in,
    required_value = 16,
    level = preset_training_set['preset_back_and_shoulder_advance'].level,
    belong_to_training_set = preset_training_set['preset_back_and_shoulder_advance'],
    exercise = inchworms,
    order=5
)
PresetTrainingExercise.objects.create(
    calculate_in = side_lying_floor_stretch_left.calculate_in,
    required_value = 30,
    level = preset_training_set['preset_back_and_shoulder_advance'].level,
    belong_to_training_set = preset_training_set['preset_back_and_shoulder_advance'],
    exercise = side_lying_floor_stretch_left,
    order=6
)
PresetTrainingExercise.objects.create(
    calculate_in = side_lying_floor_stretch_right.calculate_in,
    required_value = 30,
    level = preset_training_set['preset_back_and_shoulder_advance'].level,
    belong_to_training_set = preset_training_set['preset_back_and_shoulder_advance'],
    exercise = side_lying_floor_stretch_right,
    order=7
)
PresetTrainingExercise.objects.create(
    calculate_in = rhomboid_squeeze.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_back_and_shoulder_advance'].level,
    belong_to_training_set = preset_training_set['preset_back_and_shoulder_advance'],
    exercise = rhomboid_squeeze,
    order=8
)
PresetTrainingExercise.objects.create(
    calculate_in = pike_push_up.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_back_and_shoulder_advance'].level,
    belong_to_training_set = preset_training_set['preset_back_and_shoulder_advance'],
    exercise = pike_push_up,
    order=9
)
PresetTrainingExercise.objects.create(
    calculate_in = superman_pulls.calculate_in,
    required_value = 10,
    level = preset_training_set['preset_back_and_shoulder_advance'].level,
    belong_to_training_set = preset_training_set['preset_back_and_shoulder_advance'],
    exercise = superman_pulls,
    order=10
)
PresetTrainingExercise.objects.create(
    calculate_in = inchworms.calculate_in,
    required_value = 14,
    level = preset_training_set['preset_back_and_shoulder_advance'].level,
    belong_to_training_set = preset_training_set['preset_back_and_shoulder_advance'],
    exercise = inchworms,
    order=11
)
PresetTrainingExercise.objects.create(
    calculate_in = cat_cow_pose.calculate_in,
    required_value = 30,
    level = preset_training_set['preset_back_and_shoulder_advance'].level,
    belong_to_training_set = preset_training_set['preset_back_and_shoulder_advance'],
    exercise = cat_cow_pose,
    order=12
)
PresetTrainingExercise.objects.create(
    calculate_in = supine_push_ups.calculate_in,
    required_value = 14,
    level = preset_training_set['preset_back_and_shoulder_advance'].level,
    belong_to_training_set = preset_training_set['preset_back_and_shoulder_advance'],
    exercise = supine_push_ups,
    order=13
)
PresetTrainingExercise.objects.create(
    calculate_in = superman_pulls.calculate_in,
    required_value = 14,
    level = preset_training_set['preset_back_and_shoulder_advance'].level,
    belong_to_training_set = preset_training_set['preset_back_and_shoulder_advance'],
    exercise = superman_pulls,
    order=14
)
PresetTrainingExercise.objects.create(
    calculate_in = supine_push_ups.calculate_in,
    required_value = 12,
    level = preset_training_set['preset_back_and_shoulder_advance'].level,
    belong_to_training_set = preset_training_set['preset_back_and_shoulder_advance'],
    exercise = supine_push_ups,
    order=15
)
PresetTrainingExercise.objects.create(
    calculate_in = plank.calculate_in,
    required_value = 30,
    level = preset_training_set['preset_back_and_shoulder_advance'].level,
    belong_to_training_set = preset_training_set['preset_back_and_shoulder_advance'],
    exercise = plank,
    order=16
)
PresetTrainingExercise.objects.create(
    calculate_in = child_pose.calculate_in,
    required_value = 30,
    level = preset_training_set['preset_back_and_shoulder_advance'].level,
    belong_to_training_set = preset_training_set['preset_back_and_shoulder_advance'],
    exercise = child_pose,
    order=17
)