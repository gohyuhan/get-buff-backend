from django.urls import reverse
from rest_framework.authtoken.models import Token

from rest_framework.test import APITestCase
from rest_framework import status
from user.models import UserProfile



class UserTest(APITestCase):
    def test_create_user_success(self):
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
        response = self.client.post(url, data)
        self.assertEqual(len(UserProfile.objects.all()), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_user_with_negative_height(self):
        url = reverse('api:account:user_sign_up-list')
        data = {
            "email": "uncleben@gmail.com", 
            "password": "JustPassword",
            "first_name": "Uncle",
            "last_name": "Ben",
            "gender":"male",
            "weight_in_kg":50.10,
            "height_in_cm":-173
        }
        response = self.client.post(url, data)
        self.assertEqual(len(UserProfile.objects.all()), 1)
        self.assertEqual(UserProfile.objects.all().first().height_in_cm, 170)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_login(self):
        # sign up
        url = reverse('api:account:user_sign_up-list')
        data = {
            "email": "uncleben@gmail.com",
            "password": "JustPassword",
            "first_name": "Uncle",
            "last_name": "Ben",
            "gender": "male",
            "weight_in_kg": 50.10,
            "height_in_cm": 173
        }
        self.client.post(url, data)
        # login
        data={
            "username": "uncleben@gmail.com",
            "password": "JustPassword"
        }
        response = self.client.post(reverse("api:account:user_login"),data)
        self.assertEqual(response.json()['token'], Token.objects.all().first().key)

    def test_user_login_fail(self):
        # sign up
        url = reverse('api:account:user_sign_up-list')
        data = {
            "email": "uncleben@gmail.com",
            "password": "JustPassword",
            "first_name": "Uncle",
            "last_name": "Ben",
            "gender": "male",
            "weight_in_kg": 50.10,
            "height_in_cm": 173
        }
        self.client.post(url, data)
        # login
        data = {
            "username": "uncleben@gmail.com",
            "password": "JustPassword."
        }
        response = self.client.post(reverse("api:account:user_login"), data)
        self.assertEqual(response.json()['non_field_errors'][0],
              'Unable to log in with provided credentials.')
        
    def test_user_logout(self):
        # sign up
        url = reverse('api:account:user_sign_up-list')
        data = {
            "email": "uncleben@gmail.com",
            "password": "JustPassword",
            "first_name": "Uncle",
            "last_name": "Ben",
            "gender": "male",
            "weight_in_kg": 50.10,
            "height_in_cm": 173
        }
        self.client.post(url, data)
        # login
        data = {
            "username": "uncleben@gmail.com",
            "password": "JustPassword"
        }
        response = self.client.post(reverse("api:account:user_login"), data)
        self.assertEqual(response.json()['token'],
                         Token.objects.all().first().key)
        token = response.json()['token']
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
        response = self.client.delete(reverse("api:account:user_logout"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['success'],True)
        self.assertEqual(len(Token.objects.all()),0)

    def test_user_logout_fail(self):
        # sign up
        url = reverse('api:account:user_sign_up-list')
        data = {
            "email": "uncleben@gmail.com",
            "password": "JustPassword",
            "first_name": "Uncle",
            "last_name": "Ben",
            "gender": "male",
            "weight_in_kg": 50.10,
            "height_in_cm": 173
        }
        self.client.post(url, data)
        # login
        data = {
            "username": "uncleben@gmail.com",
            "password": "JustPassword"
        }
        response = self.client.post(reverse("api:account:user_login"), data)
        self.assertEqual(response.json()['token'],
                         Token.objects.all().first().key)
        token = response.json()['token']
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token}1')
        response = self.client.delete(reverse("api:account:user_logout"))
        self.assertEqual(response.status_code, 401)
