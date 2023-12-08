from django.urls import reverse

from rest_framework.test import APITestCase


class TestRestTimeView(APITestCase):
    def test_retrieve_rest_time(self):
        resp = self.client.get(reverse("api:training:training_rest_time"))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(resp.json()['success'])
        self.assertEqual(
            resp.json()['data'],
            25
        )