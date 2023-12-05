from django.urls import reverse

from rest_framework.test import APITestCase
from .factories import (
    ExerciseFactory,
    PresetTrainingExerciseFactory,
    PresetTrainingSetFactory
)
from muscle.tests.factories import (
    MuscleFactory,
    MuscleCategoryFactory
)
from training.enums import (
    TrainingLevel, 
    CalculatedIn
)
from muscle.enums import MuscleGroup


class TestPresetTraining(APITestCase):
    URL = reverse("api:training:preset_training_set-list")
    def setUp(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'')
        self.muscle_category={
            "shoulder_and_back":MuscleCategoryFactory(
                name= 'back and shoulder',
                type = MuscleGroup.BACKNSHOULDER,
                image_url = "http://test"
            ),
            "legs":MuscleCategoryFactory(
                name = 'legs',
                type = MuscleGroup.LEGS,
                image_url = "http://test"
            )
        }

        self.muscle={
            "shoulder":MuscleFactory(
                name = "shoulder",
                front_image_url = "http://test-front",
                back_image_url = "http://test-back",
                muscle_category=self.muscle_category["shoulder_and_back"]
            ),
            "calves":MuscleFactory(
                name = "calves",
                front_image_url = "http://test-front",
                back_image_url = "http://test-back",
                muscle_category=self.muscle_category[MuscleGroup.LEGS.label]
            )
        }

        self.exercise={
            "exercise_1":ExerciseFactory(
                name = "exercise_1",
                explanation = "exercise 1 explanation",
                calculate_in = CalculatedIn.SECONDS,
                animation = "https://test-animation",
                min_count = 15
            ),
            "exercise_2":ExerciseFactory(
                name = "exercise_2",
                explanation = "exercise 2 explanation",
                calculate_in = CalculatedIn.REPS,
                animation = "https://test-animation",
                min_count = 8
            )
        }
        self.exercise['exercise_1'].muscle_category.add(self.muscle_category["shoulder_and_back"])
        self.exercise['exercise_1'].muscle.add(self.muscle["shoulder"])
        self.exercise['exercise_1'].save()
        self.exercise['exercise_2'].muscle_category.add(self.muscle_category[MuscleGroup.LEGS.label])
        self.exercise['exercise_2'].muscle.add(self.muscle["calves"])
        self.exercise['exercise_2'].save()

        self.preset_training_set={
            "preset_training_set_1":PresetTrainingSetFactory(
                name = 'set 1 (advance)',
                level = TrainingLevel.ADVANCED,
                muscle_category =self.muscle_category["shoulder_and_back"]
            ),
            "preset_training_set_2":PresetTrainingSetFactory(
                name = 'set 2 (advance)',
                level = TrainingLevel.INTERMEDIATE,
                muscle_category =self.muscle_category[MuscleGroup.LEGS.label]
            )
        }

        self.preset_training_exercise={
            # for preset training set 1
            "preset_exercise_1":PresetTrainingExerciseFactory(
                calculate_in = self.exercise['exercise_1'].calculate_in,
                required_value = 30,
                level = self.preset_training_set["preset_training_set_1"].level,
                belong_to_training_set = self.preset_training_set["preset_training_set_1"],
                exercise = self.exercise['exercise_1'],
                order=1
            ),
            "preset_exercise_2":PresetTrainingExerciseFactory(
                calculate_in = self.exercise['exercise_1'].calculate_in,
                required_value = 40,
                level = self.preset_training_set["preset_training_set_1"].level,
                belong_to_training_set = self.preset_training_set["preset_training_set_1"],
                exercise = self.exercise['exercise_1'],
                order=2
            ),
            # for preset training set 2
            "preset_exercise_3":PresetTrainingExerciseFactory(
                calculate_in = self.exercise['exercise_2'].calculate_in,
                required_value = 20,
                level = self.preset_training_set["preset_training_set_2"].level,
                belong_to_training_set = self.preset_training_set["preset_training_set_2"],
                exercise = self.exercise['exercise_2'],
                order=1
            ),
            "preset_exercise_4":PresetTrainingExerciseFactory(
                calculate_in = self.exercise['exercise_2'].calculate_in,
                required_value = 25,
                level = self.preset_training_set["preset_training_set_2"].level,
                belong_to_training_set = self.preset_training_set["preset_training_set_2"],
                exercise = self.exercise['exercise_2'],
                order=2
            )
        }

    def test_preset_training_set_api_view(self):
        expected_results=[
            {
                "id":1,
                "name":"set 1 (advance)",
                "level":"advanced",
                "muscle_category":{
                    "id":1,
                    "name":'back and shoulder',
                    "type":MuscleGroup.BACKNSHOULDER.label,
                    "image_url":"http://test"
                },
                "exercise":[
                    {
                        "id":1,
                        "calculate_in":"seconds",
                        "required_value":30,
                        "level":"advanced",
                        "exercise":{
                            "id":1,
                            "name":"exercise_1",
                            "explanation":"exercise 1 explanation",
                            "calculate_in":"seconds",
                            "animation":"https://test-animation",
                            "muscle":[
                            {
                                "id":1,
                                "name":"shoulder",
                                "front_image_url":"http://test-front",
                                "back_image_url":"http://test-back"
                            }
                            ],
                            "muscle_category":[
                            {
                                "id":1,
                                "name":'back and shoulder',
                                "type":MuscleGroup.BACKNSHOULDER.label,
                                "image_url":"http://test"
                            }
                            ],
                            "min_count":15
                        },
                        "order":1
                    },
                    {
                        "id":2,
                        "calculate_in":"seconds",
                        "required_value":40,
                        "level":"advanced",
                        "exercise":{
                            "id":1,
                            "name":"exercise_1",
                            "explanation":"exercise 1 explanation",
                            "calculate_in":"seconds",
                            "animation":"https://test-animation",
                            "muscle":[
                            {
                                "id":1,
                                "name":"shoulder",
                                "front_image_url":"http://test-front",
                                "back_image_url":"http://test-back"
                            }
                            ],
                            "muscle_category":[
                            {
                                "id":1,
                                "name":'back and shoulder',
                                "type":MuscleGroup.BACKNSHOULDER.label,
                                "image_url":"http://test"
                            }
                            ],
                            "min_count":15
                        },
                        "order":2
                    }
                ]
            },
            {
                "id":2,
                "name":"set 2 (advance)",
                "level":"intermediate",
                "muscle_category":{
                    "id":2,
                    "name":'legs',
                    "type":MuscleGroup.LEGS.label,
                    "image_url":"http://test"
                },
                "exercise":[
                    {
                        "id":3,
                        "calculate_in":"reps",
                        "required_value":20,
                        "level":"intermediate",
                        "exercise":{
                            "id":2,
                            "name":"exercise_2",
                            "explanation":"exercise 2 explanation",
                            "calculate_in":"reps",
                            "animation":"https://test-animation",
                            "muscle":[
                            {
                                "id":2,
                                "name":"calves",
                                "front_image_url":"http://test-front",
                                "back_image_url":"http://test-back"
                            }
                            ],
                            "muscle_category":[
                            {
                                "id":2,
                                "name":'legs',
                                "type":MuscleGroup.LEGS.label,
                                "image_url":"http://test"
                            }
                            ],
                            "min_count":8
                        },
                        "order":1
                    },
                    {
                        "id":4,
                        "calculate_in":"reps",
                        "required_value":25,
                        "level":"intermediate",
                        "exercise":{
                            "id":2,
                            "name":"exercise_2",
                            "explanation":"exercise 2 explanation",
                            "calculate_in":"reps",
                            "animation":"https://test-animation",
                            "muscle":[
                            {
                                "id":2,
                                "name":"calves",
                                "front_image_url":"http://test-front",
                                "back_image_url":"http://test-back"
                            }
                            ],
                            "muscle_category":[
                            {
                                "id":2,
                                "name":'legs',
                                "type":MuscleGroup.LEGS.label,
                                "image_url":"http://test"
                            }
                            ],
                            "min_count":8
                        },
                        "order":2
                    }
                ]
            }
        ]
        resp = self.client.get(self.URL)
        self.assertEqual(resp.status_code, 200)
        for i,result in enumerate(expected_results):
            self.assertDictEqual(
                resp.json()[i],
                result
            )