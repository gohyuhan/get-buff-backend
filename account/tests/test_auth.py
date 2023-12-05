from unittest import mock

from rest_framework import exceptions
from rest_framework.authtoken.models import Token
from rest_framework.test import APIRequestFactory,APITestCase
from django_mock_queries.query import MockModel,MockSet

from account.authentication import CustomTokenAuthentication
from account.models import User


class AuthenticationTest(CustomTokenAuthentication):
    word="Test_Token"
    def authenticate(self, request): 
        http = request.META.get("AUTH")
        if not http:
             raise exceptions.AuthenticationFailed("No AUTH in header")
        auth_token = http.split()
        if auth_token[0]!=self.word or len(auth_token)!=2:
            raise exceptions.AuthenticationFailed("Incorrect Token Format")
        token_key = auth_token[1]
        try:
            token = Token.objects.get(key = token_key)
            user = token.user
        except:
            raise exceptions.AuthenticationFailed("Token does not exist")
        return (user,token)


class TestAuth(APITestCase):
    factory = APIRequestFactory()
    url = ""
    def setUp(self):
        super().setUp()
        user=User.objects.create_user(
            email= "uncleben@gmail.com", 
            password= "JustPassword123",
            first_name= "Uncle",
            last_name= "Ben",
        )
        token=Token.objects.create(user=user, key="UncleBen_Key")


    def test_auth_success(self):
        request = self.factory.post(self.url,AUTH = "Test_Token UncleBen_Key")
        auth = AuthenticationTest()
        user,token = auth.authenticate(request)
        self.assertEqual(user.email,"uncleben@gmail.com")
        self.assertEqual(token.key,"UncleBen_Key")
    
    def test_auth_unsuccessfull_wrong_token(self):
        request = self.factory.post(self.url,AUTH = "Test_Token Uncleben_Key")
        auth = AuthenticationTest()
        with self.assertRaises(exceptions.AuthenticationFailed):
            auth.authenticate(request)
    
    def test_auth_unsuccessfull_wrong_token_format(self):
        request = self.factory.post(self.url,AUTH = "Token UncleBen_Key")
        auth = AuthenticationTest()
        with self.assertRaises(exceptions.AuthenticationFailed):
            auth.authenticate(request)
    
    def test_auth_unsuccessfull_no_token(self):
        request = self.factory.post(self.url)
        auth = AuthenticationTest()
        with self.assertRaises(exceptions.AuthenticationFailed):
            auth.authenticate(request)
 