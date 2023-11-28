from urllib.parse import urljoin
from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from user.models import UserProfile


class TestUserProfile(APITestCase):
    SIGN_UP_USER_URL = reverse('api:account:user_sign_up-list')
    USER_PROFILE_URL = reverse('api:user:user_profile-list')

    def setUp(self):
        url = reverse('api:account:user_sign_up-list')
        data = {
            "email": "uncleben@gmail.com", 
            "password": "JustPassword",
            "first_name": "Uncle",
            "last_name": "Ben",
            "gender":"male",
            "weight_in_kg":50.10,
            "height_in_cm":173
        }
        self.client.post(url, data)
        token = Token.objects.all().first()
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')

    def test_view_user_profile_list(self):
        resp = self.client.get(self.USER_PROFILE_URL)
        self.assertEqual(resp.status_code, 200)
        self.assertDictEqual(
            resp.json()[0],
            {
                "first_name": "Uncle",
                "last_name": "Ben",
                "gender":"male",
                "weight_in_kg":"50.10",
                "height_in_cm":173,
                "target_weight_in_kg":"50.10",
                "weight_target_status":"maintain"
            }
        )
    
    def test_view_user_profile_retrieve(self):
        resp = self.client.get(
            urljoin(self.USER_PROFILE_URL,f"{UserProfile.objects.all().first().id}/")
        )
        self.assertEqual(resp.status_code, 200)
        self.assertDictEqual(
            resp.json(),
            {
                "first_name": "Uncle",
                "last_name": "Ben",
                "gender":"male",
                "weight_in_kg":"50.10",
                "height_in_cm":173,
                "target_weight_in_kg":"50.10",
                "weight_target_status":"maintain"
            }
        )

    def test_update_user_profile(self):
        data={
            "gender":"male",
            "weight_in_kg":600,
            "height_in_cm":-173,
            "target_weight_in_kg":80,
        }
        resp = self.client.post(self.USER_PROFILE_URL, data, format='json')
        self.assertEqual(resp.status_code, 200)
        self.assertDictEqual(
            resp.json(),
            {
                "first_name": "Uncle",
                "last_name": "Ben",
                "gender":"male",
                "weight_in_kg":"60.00",
                "height_in_cm":170,
                "target_weight_in_kg":"80.00",
                "weight_target_status":"gain"
            }
        )
