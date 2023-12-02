from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

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
    CalculatedIn,
    TrainingStatus
)
from training.models import(
    CustomTrainingSet,
    CustomTrainingExercise
)
from user.models import TrainingSetCompletedRecord 
from user.models import UserProfile



class TrainingTest(APITestCase):
    URL = reverse("api:training:custom_preset_training_set-list")
    URL2 = reverse("api:training:custom_training_set-list")
    def setUp(self):
        url = reverse('api:account:user_sign_up-list')
        data = {
            "email": "uncleben@gmail.com", 
            "password": "JustPassword123",
            "first_name": "Uncle",
            "last_name": "Ben",
            "gender":"male",
            "weight_in_kg":50.10,
            "height_in_cm":173
        } 
        self.client.post(url, data)
        self.user_profile = UserProfile.objects.all().first()
        self.token = Token.objects.all().first()
        url = reverse('api:account:user_sign_up-list')
        data2 = {
            "email": "uncleben2@gmail.com", 
            "password": "JustPassword123",
            "first_name": "Uncle2",
            "last_name": "Ben2",
            "gender":"male",
            "weight_in_kg":52.10,
            "height_in_cm":172        
        }
        self.client.post(url, data2)
        self.token2 = Token.objects.all().order_by('user__id').last()

        self.muscle_category={
            "shoulder_and_back":MuscleCategoryFactory(
                name = "shoulder and back",
                image_url = "http://test"
            ),
            "legs":MuscleCategoryFactory(
                name = "legs",
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
                muscle_category=self.muscle_category["legs"]
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
        self.exercise['exercise_2'].muscle_category.add(self.muscle_category["legs"])
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
                muscle_category =self.muscle_category["legs"]
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

    def test_create_list_retrieve_training_set(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')
        data={
            "profile":self.user_profile.uuid,
            "name":"test custom training set",
            "level":"advance",
            "muscle_category":{
                'id':self.muscle_category["shoulder_and_back"].id,
                'name':self.muscle_category["shoulder_and_back"].name,
                'image_url':self.muscle_category["shoulder_and_back"].image_url
            },
            "exercise":[
                {
                    "id":self.preset_training_exercise["preset_exercise_3"].id,
                    "calculate_in":"reps", 
                    "required_value":self.preset_training_exercise["preset_exercise_3"].required_value,
                    "level":'intermidiate',
                    "exercise":{
                        "id":self.preset_training_exercise["preset_exercise_3"].exercise.id,
                        "name":self.preset_training_exercise["preset_exercise_3"].exercise.name,
                        "explanation":self.preset_training_exercise["preset_exercise_3"].exercise.explanation,
                        "calculate_in":"reps", 
                        "animation":self.preset_training_exercise["preset_exercise_3"].exercise.animation,
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
                                "name":"legs",
                                "image_url":"http://test"
                            }
                        ],
                        "min_count":self.preset_training_exercise["preset_exercise_3"].exercise.min_count
                    },
                    "order":1,
                },
                {
                    "id":self.preset_training_exercise["preset_exercise_3"].id,
                    "calculate_in":"reps", 
                    "required_value":self.preset_training_exercise["preset_exercise_3"].required_value,
                    "level":'intermidiate',
                    "exercise":{
                        "id":self.preset_training_exercise["preset_exercise_3"].exercise.id,
                        "name":self.preset_training_exercise["preset_exercise_3"].exercise.name,
                        "explanation":self.preset_training_exercise["preset_exercise_3"].exercise.explanation,
                        "calculate_in":"reps", 
                        "animation":self.preset_training_exercise["preset_exercise_3"].exercise.animation,
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
                                "name":"legs",
                                "image_url":"http://test"
                            }
                        ],
                        "min_count":self.preset_training_exercise["preset_exercise_3"].exercise.min_count
                    },
                    "order":2,
                },
                {
                    "id":self.preset_training_exercise["preset_exercise_3"].id,
                    "calculate_in":"reps", 
                    "required_value":self.preset_training_exercise["preset_exercise_3"].required_value,
                    "level":'intermidiate',
                    "exercise":{
                        "id":self.preset_training_exercise["preset_exercise_3"].exercise.id,
                        "name":self.preset_training_exercise["preset_exercise_3"].exercise.name,
                        "explanation":self.preset_training_exercise["preset_exercise_3"].exercise.explanation,
                        "calculate_in":"reps", 
                        "animation":self.preset_training_exercise["preset_exercise_3"].exercise.animation,
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
                                "name":"legs",
                                "image_url":"http://test"
                            }
                        ],
                        "min_count":self.preset_training_exercise["preset_exercise_3"].exercise.min_count
                    },
                    "order":3,
                },
                {
                    "id":self.preset_training_exercise["preset_exercise_3"].id,
                    "calculate_in":"reps", 
                    "required_value":self.preset_training_exercise["preset_exercise_3"].required_value,
                    "level":'intermidiate',
                    "exercise":{
                        "id":self.preset_training_exercise["preset_exercise_3"].exercise.id,
                        "name":self.preset_training_exercise["preset_exercise_3"].exercise.name,
                        "explanation":self.preset_training_exercise["preset_exercise_3"].exercise.explanation,
                        "calculate_in":"reps", 
                        "animation":self.preset_training_exercise["preset_exercise_3"].exercise.animation,
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
                                "name":"legs",
                                "image_url":"http://test"
                            }
                        ],
                        "min_count":self.preset_training_exercise["preset_exercise_3"].exercise.min_count
                    },
                    "order":4,
                },
                {
                    "id":self.preset_training_exercise["preset_exercise_3"].id,
                    "calculate_in":"reps", 
                    "required_value":self.preset_training_exercise["preset_exercise_3"].required_value,
                    "level":'intermidiate',
                    "exercise":{
                        "id":self.preset_training_exercise["preset_exercise_3"].exercise.id,
                        "name":self.preset_training_exercise["preset_exercise_3"].exercise.name,
                        "explanation":self.preset_training_exercise["preset_exercise_3"].exercise.explanation,
                        "calculate_in":"reps", 
                        "animation":self.preset_training_exercise["preset_exercise_3"].exercise.animation,
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
                                "name":"legs",
                                "image_url":"http://test"
                            }
                        ],
                        "min_count":self.preset_training_exercise["preset_exercise_3"].exercise.min_count
                    },
                    "order":5,
                },
            ]
        }

        resp = self.client.post(self.URL, data, format='json')
        self.assertEqual(resp.status_code, 201)

        resp = self.client.get(self.URL, args=[1])
        self.assertEqual(resp.status_code, 200)

        resp = self.client.get(self.URL)
        self.assertEqual(resp.status_code, 200)

        self.assertEqual(
            len(CustomTrainingSet.objects.all()),
            1
        )
        self.assertEqual(
            len(CustomTrainingExercise.objects.all()),
            5
        )

        # retrieve as other user which didn't have any customtrainingset
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token2.key}')
        resp = self.client.get(self.URL)
        self.assertEqual(resp.json(), [])

    def test_exercise_less_than_default_minimum_error_api_view(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')
        data={
            "profile":self.user_profile.uuid,
            "name":"test custom training set",
            "level":"advance",
            "muscle_category":{
                'id':self.muscle_category["shoulder_and_back"].id,
                'name':self.muscle_category["shoulder_and_back"].name,
                'image_url':self.muscle_category["shoulder_and_back"].image_url
            },
            "exercise":[
                {
                    "id":self.preset_training_exercise["preset_exercise_3"].id,
                    "calculate_in":"reps", 
                    "required_value":self.preset_training_exercise["preset_exercise_3"].required_value,
                    "level":'intermidiate',
                    "exercise":{
                        "id":self.preset_training_exercise["preset_exercise_3"].exercise.id,
                        "name":self.preset_training_exercise["preset_exercise_3"].exercise.name,
                        "explanation":self.preset_training_exercise["preset_exercise_3"].exercise.explanation,
                        "calculate_in":"reps", 
                        "animation":self.preset_training_exercise["preset_exercise_3"].exercise.animation,
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
                                "name":"legs",
                                "image_url":"http://test"
                            }
                        ],
                        "min_count":self.preset_training_exercise["preset_exercise_3"].exercise.min_count
                    },
                    "order":1,
                }
            ]
        }

        resp = self.client.post(self.URL, data, format='json')
        self.assertEqual(resp.status_code, 400)
        self.assertTrue(resp.json()['error'], "Exercise count should more than or equal 5")

    def test_customization_training_view_set(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')
        data={
            "profile":self.user_profile.uuid,
            "name":"test customize training set",
            "exercise":[
                {
                    "id":self.exercise['exercise_1'].id,
                    "count":15
                },
                {
                    "id":self.exercise['exercise_2'].id,
                    "count":8
                },
                {
                    "id":self.exercise['exercise_2'].id,
                    "count":8
                },
                {
                    "id":self.exercise['exercise_1'].id,
                    "count":15
                },
                {
                    "id":self.exercise['exercise_1'].id,
                    "count":15
                }
            ]
        }

        resp = self.client.post(self.URL2, data, format='json')
        self.assertEqual(resp.status_code, 201)

        self.assertEqual(
            len(CustomTrainingSet.objects.all()),
            1
        )
        self.assertEqual(
            len(CustomTrainingExercise.objects.all()),
            5
        )


    def test_customization_training_view_min_requirement_not_reach_set(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')
        data={
            "profile":self.user_profile.uuid,
            "name":"test customize training set",
            "exercise":[
                {
                    "id":self.exercise['exercise_1'].id,
                    "count":1
                },
                {
                    "id":self.exercise['exercise_2'].id,
                    "count":1
                },
                {
                    "id":self.exercise['exercise_2'].id,
                    "count":1
                },
                {
                    "id":self.exercise['exercise_1'].id,
                    "count":1
                },
                {
                    "id":self.exercise['exercise_1'].id,
                    "count":1
                }
            ]
        }

        resp = self.client.post(self.URL2, data, format='json')
        self.assertEqual(resp.status_code, 400)

        self.assertEqual(
            len(CustomTrainingSet.objects.all()),
            0
        )
        self.assertEqual(
            len(CustomTrainingExercise.objects.all()),
            0
        )

    def test_customization_training_view_set_get_permission_not_allowed(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')
        resp = self.client.get(self.URL2)
        self.assertEqual(resp.status_code, 403)

    def test_customization_training_view_set_auth_user_and_profile_not_match(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token2.key}')
        data={
            "profile":self.user_profile.uuid,
            "name":"test customize training set",
            "exercise":[
                {
                    "id":self.exercise['exercise_1'].id,
                    "count":15
                },
                {
                    "id":self.exercise['exercise_2'].id,
                    "count":8
                },
                {
                    "id":self.exercise['exercise_2'].id,
                    "count":8
                },
                {
                    "id":self.exercise['exercise_1'].id,
                    "count":15
                },
                {
                    "id":self.exercise['exercise_1'].id,
                    "count":15
                }
            ]
        }

        resp = self.client.post(self.URL2, data, format='json')
        self.assertEqual(resp.status_code, 400)
        self.assertEqual(resp.json()['error'], "Error on authentication, please logout and login again ")

    def test_pause_training_set(self):
        # create training set and exercise first
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')
        data={
            "profile":self.user_profile.uuid,
            "name":"test customize training set",
            "exercise":[
                {
                    "id":self.exercise['exercise_1'].id,
                    "count":15
                },
                {
                    "id":self.exercise['exercise_2'].id,
                    "count":8
                },
                {
                    "id":self.exercise['exercise_2'].id,
                    "count":8
                },
                {
                    "id":self.exercise['exercise_1'].id,
                    "count":15
                },
                {
                    "id":self.exercise['exercise_1'].id,
                    "count":15
                }
            ]
        }

        self.client.post(self.URL2, data, format='json')
        self.assertEqual(
            len(CustomTrainingExercise.objects.filter(status = TrainingStatus.ONGOING)),
            5
        )

        custom_training_set = CustomTrainingSet.objects.all().first()
        custom_training_exercise_id = [exe.id for exe in CustomTrainingExercise.objects.all()]

        data={
            "profile":self.user_profile.uuid,
            "custom_training_set":custom_training_set.id,
            "exercise":[
                {
                    "id":custom_training_exercise_id[0],
                    "status":"completed"
                },
                {
                    "id":custom_training_exercise_id[1],
                    "status":"completed"
                },
                {
                    "id":custom_training_exercise_id[2],
                    "status":"completed"
                },
                {
                    "id":custom_training_exercise_id[3],
                    "status":"ongoing"
                },
                {
                    "id":custom_training_exercise_id[4],
                    "status":"ongoing"
                }
            ]
        }

        resp = self.client.post(reverse("api:training:training_pause"), data, format='json')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(
            len(CustomTrainingExercise.objects.filter(status = TrainingStatus.COMPLETED)),
            3
        )
        self.assertEqual(
            len(CustomTrainingExercise.objects.filter(status = TrainingStatus.ONGOING)),
            2
        )

    def test_conclude_training_set(self):
        # create training set and exercise first
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')
        data={
            "profile":self.user_profile.uuid,
            "name":"test customize training set",
            "exercise":[
                {
                    "id":self.exercise['exercise_1'].id,
                    "count":15
                },
                {
                    "id":self.exercise['exercise_2'].id,
                    "count":8
                },
                {
                    "id":self.exercise['exercise_2'].id,
                    "count":8
                },
                {
                    "id":self.exercise['exercise_1'].id,
                    "count":15
                },
                {
                    "id":self.exercise['exercise_1'].id,
                    "count":15
                }
            ]
        }

        self.client.post(self.URL2, data, format='json')
        self.client.post(self.URL2, data, format='json')
        self.assertEqual(
            len(CustomTrainingExercise.objects.filter(status = TrainingStatus.ONGOING)),
            10
        )

        custom_training_set_1 = CustomTrainingSet.objects.all().order_by('id').first()
        custom_training_set_2 = CustomTrainingSet.objects.all().order_by('-id').first()

        data_1={
            "profile":self.user_profile.uuid,
            "custom_training_set":custom_training_set_1.id,
        }
        data_2={
            "profile":self.user_profile.uuid,
            "custom_training_set":custom_training_set_2.id,
        }
        resp = self.client.post(reverse("api:training:training_conclude"), data_1, format='json')
        self.assertEqual(resp.status_code, 200)
        resp = self.client.post(reverse("api:training:training_conclude"), data_2, format='json')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(
            len(CustomTrainingExercise.objects.filter(status = TrainingStatus.COMPLETED)),
            10
        )
        self.assertEqual(
            len(CustomTrainingSet.objects.filter(status = TrainingStatus.COMPLETED)),
            2
        )
        self.assertEqual(
            len(TrainingSetCompletedRecord.objects.all()),
            2
        )

    def test_give_up_brand_new_training_set(self):
        # create training set and exercise first
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')
        data={
            "profile":self.user_profile.uuid,
            "name":"test customize training set",
            "exercise":[
                {
                    "id":self.exercise['exercise_1'].id,
                    "count":15
                },
                {
                    "id":self.exercise['exercise_2'].id,
                    "count":8
                },
                {
                    "id":self.exercise['exercise_2'].id,
                    "count":8
                },
                {
                    "id":self.exercise['exercise_1'].id,
                    "count":15
                },
                {
                    "id":self.exercise['exercise_1'].id,
                    "count":15
                }
            ]
        }

        self.client.post(self.URL2, data, format='json')
        self.assertEqual(
            len(CustomTrainingExercise.objects.filter(status = TrainingStatus.ONGOING)),
            5
        )

        custom_training_set = CustomTrainingSet.objects.all().first()

        data={
            "profile":self.user_profile.uuid,
            "custom_training_set":custom_training_set.id,
        }
        resp = self.client.post(reverse("api:training:training_give_up"), data, format='json')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(
            len(CustomTrainingExercise.objects.filter(status = TrainingStatus.GIVEUP)),
            5
        )
        self.assertEqual(
            len(CustomTrainingSet.objects.filter(status = TrainingStatus.GIVEUP)),
            1
        )

    def test_give_up_in_progress_training_set(self):
        # create training set and exercise first
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')
        data={
            "profile":self.user_profile.uuid,
            "name":"test customize training set",
            "exercise":[
                {
                    "id":self.exercise['exercise_1'].id,
                    "count":15
                },
                {
                    "id":self.exercise['exercise_2'].id,
                    "count":8
                },
                {
                    "id":self.exercise['exercise_2'].id,
                    "count":8
                },
                {
                    "id":self.exercise['exercise_1'].id,
                    "count":15
                },
                {
                    "id":self.exercise['exercise_1'].id,
                    "count":15
                }
            ]
        }

        self.client.post(self.URL2, data, format='json')
        self.assertEqual(
            len(CustomTrainingExercise.objects.filter(status = TrainingStatus.ONGOING)),
            5
        )

        custom_training_set = CustomTrainingSet.objects.all().first()
        custom_training_exercise_id = [exe.id for exe in CustomTrainingExercise.objects.all()]

        data={
            "profile":self.user_profile.uuid,
            "custom_training_set":custom_training_set.id,
            "exercise":[
                {
                    "id":custom_training_exercise_id[0],
                    "status":"completed"
                },
                {
                    "id":custom_training_exercise_id[1],
                    "status":"completed"
                },
                {
                    "id":custom_training_exercise_id[2],
                    "status":"completed"
                },
                {
                    "id":custom_training_exercise_id[3],
                    "status":"ongoing"
                },
                {
                    "id":custom_training_exercise_id[4],
                    "status":"ongoing"
                }
            ]
        }

        resp = self.client.post(reverse("api:training:training_pause"), data, format='json')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(
            len(CustomTrainingExercise.objects.filter(status = TrainingStatus.COMPLETED)),
            3
        )
        self.assertEqual(
            len(CustomTrainingExercise.objects.filter(status = TrainingStatus.ONGOING)),
            2
        )

        data={
            "profile":self.user_profile.uuid,
            "custom_training_set":custom_training_set.id,
        }

        resp = self.client.post(reverse("api:training:training_give_up"), data, format='json')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(
            len(CustomTrainingExercise.objects.filter(status = TrainingStatus.COMPLETED)),
            3
        )
        self.assertEqual(
            len(CustomTrainingExercise.objects.filter(status = TrainingStatus.GIVEUP)),
            2
        )
        self.assertEqual(
            len(CustomTrainingSet.objects.filter(status = TrainingStatus.GIVEUP)),
            1
        )
