from django.urls import reverse
from rest_framework.authtoken.models import Token
from django.test.utils import override_settings

from rest_framework.test import APITestCase
from rest_framework import status
from user.models import UserProfile
from badges.models import (
    Badge, 
    SkeletonAchivementBadge, 
    Track,
    UserAchivementBadge
)
from muscle.enums import MuscleGroup
from training.enums import (
    TrainingLevel,
    TrainingOrExerciseType
)
from badges.enums import (
    SpecialTargetType,
    TargetCountType,
)
from account.models import User


@override_settings(EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend')
class UserTest(APITestCase):
    def setUp(self):
        badges={
            'badge_1':Badge.objects.create(name='1st Training Completed', image='https://1stbadges'),
            'badge_2':Badge.objects.create(name='100 Exercise Completed', image='https://100exercise'),
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
        }
        SkeletonAchivementBadge.objects.create(
            desp = "Completed Your 1st training of any level to earn this badge",
            required_value = 1,
            badge = badges['badge_1'],
            track = tracks['track_1']
        )
        SkeletonAchivementBadge.objects.create(
            desp = "Completed a total of 100 exercise of any level to earn this badge",
            required_value = 100,
            badge = badges['badge_2'],
            track = tracks['track_2']
        )

    def test_create_user_success(self):
        url = reverse('api:account:user_sign_up')
        data = {
            "email": "uncleben@gmail.com", 
            "password": "JustPassword123",
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
        url = reverse('api:account:user_sign_up')
        data = {
            "email": "uncleben@gmail.com", 
            "password": "JustPassword123",
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

    def test_create_user_with_weak_password(self):
        url = reverse('api:account:user_sign_up')
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
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.json()['error']['password'][0], 
            "Password Must Contain min. 9 chars with at least 1 lowercase, 1 uppercase and 1 number"
        )

    def test_user_login(self):
        user = User.objects.create_user(
            email = "uncleben@gmail.com",
            password = "JustPassword123",
            first_name =  "Uncle",
            last_name =  "Ben",
        )
        UserProfile.objects.filter(
            user = user
        ).update(
            gender = "male",
            weight_in_kg = 50.10,
            height_in_cm = 173,
            target_weight_in_kg=50.10)
        # login
        data={
            "email": "uncleben@gmail.com",
            "password": "JustPassword123"
        }
        response = self.client.post(reverse("api:account:user_login"),data)
        self.assertEqual(response.json()['token'], Token.objects.all().first().key)

    def test_user_login_fail(self):
        user = User.objects.create_user(
            email = "uncleben@gmail.com",
            password = "JustPassword123",
            first_name =  "Uncle",
            last_name =  "Ben",
        )
        UserProfile.objects.filter(
            user = user
        ).update(
            gender = "male",
            weight_in_kg = 50.10,
            height_in_cm = 173,
            target_weight_in_kg=50.10)
        # login
        data = {
            "email": "uncleben@gmail.com",
            "password": "JustPassword."
        }
        response = self.client.post(reverse("api:account:user_login"), data)
        self.assertEqual(response.json()["error"]['non_field_errors'][0],
              'Invalid user/password')
        
    def test_user_logout(self):
        user = User.objects.create_user(
            email = "uncleben@gmail.com",
            password = "JustPassword123",
            first_name =  "Uncle",
            last_name =  "Ben",
        )
        UserProfile.objects.filter(
            user = user
        ).update(
            gender = "male",
            weight_in_kg = 50.10,
            height_in_cm = 173,
            target_weight_in_kg=50.10)
        # login
        data = {
            "email": "uncleben@gmail.com",
            "password": "JustPassword123"
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
        user = User.objects.create_user(
            email = "uncleben@gmail.com",
            password = "JustPassword123",
            first_name =  "Uncle",
            last_name =  "Ben",
        )
        UserProfile.objects.filter(
            user = user
        ).update(
            gender = "male",
            weight_in_kg = 50.10,
            height_in_cm = 173,
            target_weight_in_kg=50.10)
        self.token = Token.objects.create(user=user)
        # login
        data = {
            "email": "uncleben@gmail.com",
            "password": "JustPassword123"
        }
        response = self.client.post(reverse("api:account:user_login"), data)
        self.assertEqual(response.json()['token'],
                         Token.objects.all().first().key)
        token = response.json()['token']
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token}1')
        response = self.client.delete(reverse("api:account:user_logout"))
        self.assertEqual(response.status_code, 401)

    def test_user_change_password(self):
        user = User.objects.create_user(
            email = "uncleben@gmail.com",
            password = "JustPassword123",
            first_name =  "Uncle",
            last_name =  "Ben",
        )
        UserProfile.objects.filter(
            user = user
        ).update(
            gender = "male",
            weight_in_kg = 50.10,
            height_in_cm = 173,
            target_weight_in_kg=50.10)
        self.token = Token.objects.create(user=user)
        # login
        data={
            "email": "uncleben@gmail.com",
            "password": "JustPassword123"
        }
        response = self.client.post(reverse("api:account:user_login"),data)    
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {response.json()['token']}")    
        data={
            "old_password": "JustPassword123",
            "new_password": "JustPassword123555"
        }
        response = self.client.patch(reverse("api:account:change_password"),data) 
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['success'], True)

    def test_user_change_password_old_password_error(self):
        user = User.objects.create_user(
            email = "uncleben@gmail.com",
            password = "JustPassword123",
            first_name =  "Uncle",
            last_name =  "Ben",
        )
        UserProfile.objects.filter(
            user = user
        ).update(
            gender = "male",
            weight_in_kg = 50.10,
            height_in_cm = 173,
            target_weight_in_kg=50.10)
        self.token = Token.objects.create(user=user)
        # login
        data={
            "email": "uncleben@gmail.com",
            "password": "JustPassword123"
        }
        response = self.client.post(reverse("api:account:user_login"),data)    
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {response.json()['token']}")    
        data={
            "old_password": "JustPassword12",
            "new_password": "JustPassword123555"
        }
        response = self.client.patch(reverse("api:account:change_password"),data) 
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['error']['old_password'][0], "Invalid old password")

    def test_user_change_password_new_password_weak_error(self):
        user = User.objects.create_user(
            email = "uncleben@gmail.com",
            password = "JustPassword123",
            first_name =  "Uncle",
            last_name =  "Ben",
        )
        UserProfile.objects.filter(
            user = user
        ).update(
            gender = "male",
            weight_in_kg = 50.10,
            height_in_cm = 173,
            target_weight_in_kg=50.10)
        self.token = Token.objects.create(user=user)
        # login
        data={
            "email": "uncleben@gmail.com",
            "password": "JustPassword123"
        }
        response = self.client.post(reverse("api:account:user_login"),data)    
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {response.json()['token']}")    
        data={
            "old_password": "JustPassword123",
            "new_password": "JustPassword"
        }
        response = self.client.patch(reverse("api:account:change_password"),data) 
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json()['error']['new_password'][0], 
            "Password Must Contain min. 9 chars with at least 1 lowercase, 1 uppercase and 1 number"
        )

    def test_create_user_success_check_badge(self):
        url = reverse('api:account:user_sign_up')
        data = {
            "email": "uncleben@gmail.com", 
            "password": "JustPassword123",
            "first_name": "Uncle",
            "last_name": "Ben",
            "gender":"male",
            "weight_in_kg":50.10,
            "height_in_cm":173
        }
        response = self.client.post(url, data)
        self.assertEqual(len(UserProfile.objects.all()), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            len(UserAchivementBadge.objects.filter(user_profile = UserProfile.objects.all().first())),
            2
        )
        
    
