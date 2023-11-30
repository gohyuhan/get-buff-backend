from urllib.parse import urljoin
from django.urls import reverse

from rest_framework.test import APITestCase
from .factories import (
    ExerciseFactory
)
from muscle.tests.factories import (
    MuscleFactory,
    MuscleCategoryFactory
)
from training.enums import (
    CalculatedIn
)


class TestPaginationView(APITestCase):
    URL = reverse("api:training:exercise-list")
    def setUp(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'')
        self.muscle_category={
            "shoulder_and_back":MuscleCategoryFactory(
                name = "shoulder and back",
                image_url = "http://test"
            )
        }

        self.muscle={
            "shoulder":MuscleFactory(
                name = "shoulder",
                front_image_url = "http://test-front",
                back_image_url = "http://test-back",
                muscle_category=self.muscle_category["shoulder_and_back"]
            )
        }

        
        for i in range(450):
            exercise=ExerciseFactory(
                name = "exercise_1",
                explanation = "exercise 1 explanation",
                calculate_in = CalculatedIn.SECONDS,
                animation = "https://test-animation",
                min_count = 15
            )
            
            exercise.muscle_category.add(self.muscle_category["shoulder_and_back"])
            exercise.muscle.add(self.muscle["shoulder"])
            exercise.save()

    def test_exercise_pagination_view(self):
        resp = self.client.get(
            self.URL
        )
        self.assertEqual(
            resp.status_code,200
        )
        self.assertEqual(
            resp.json()['previous'],None
        )
        self.assertEqual(
            resp.json()['count'], 450
        )
        self.assertEqual(
            len(resp.json()['results']),
            100
        )
        self.assertEqual(
            resp.json()['next'],
            "http://testserver"+ urljoin(self.URL, "?page=2")
        )