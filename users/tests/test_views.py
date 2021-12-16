import json
from django.test import TestCase
from users.views import Register, Login, Logout, UserToken
from users.models import User
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient



class TestViews(TestCase):

    def test_user_register(self):
        factory = APIRequestFactory()
        request = factory.post('/register/', {
                                            "username": "test_user",
                                            "email": "test_email@gmail.com",
                                            "password": '123456ABCde',
                                            }, format='json')
        view = Register.as_view()
        response = view(request)
        print("[Register] response.data: {}".format(response.data))
        assert 201 == response.status_code

    def test_user_login(self):
        user = User.objects.create(username='test_user', email="test_email@gmail.com")
        user.set_password("123456ABCde")
        user.save()

        factory = APIRequestFactory()
        request = factory.post('/login/', {
                                            "username": "test_email@gmail.com",
                                            "password": '123456ABCde',
                                            }, format='json')
        view = Login.as_view()
        response = view(request)
        print("[Login] response.data: {}".format(response.data))
        assert 201 == response.status_code

    def test_user_logout(self):
        user = User.objects.create(username='test_user', email="test_email@gmail.com")
        user.set_password("123456ABCde")

        user.save()

        factory = APIRequestFactory()
        request = factory.post('/login/', {
                                            "username": "test_email@gmail.com",
                                            "password": '123456ABCde',
                                            }, format='json')
        view = Login.as_view()
        response = view(request)

        request = factory.post('/logout/?username={}'.format(response.data['user']['username']), HTTP_AUTHORIZATION='Token {}'.format(response.data['token']))
        view = Logout.as_view()
        response = view(request)
        print("[Logout] response.data: {}".format(response.data))

        assert 200 == response.status_code

    def test_user_refresh_token(self):
        user = User.objects.create(username='test_user', email="test_email@gmail.com")
        user.set_password("123456ABCde")

        user.save()

        factory = APIRequestFactory()
        request = factory.post('/login/', {
                                            "username": "test_email@gmail.com",
                                            "password": '123456ABCde',
                                            }, format='json')
        view = Login.as_view()
        response = view(request)

        request = factory.get('/refresh-token/?username={}'.format(response.data['user']['username']), HTTP_AUTHORIZATION='Token {}'.format(response.data['token']))
        view = UserToken.as_view()
        response = view(request)
        print("[Refresh Token] response.data: {}".format(response.data))

        assert 200 == response.status_code