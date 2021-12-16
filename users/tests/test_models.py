from django.test import TestCase
from users.models import User



class TestModels(TestCase):

    def setUp(self):
        self.user_1 = User.objects.create_user('emailtest@gmail.com', 'usernametest', 'testpassword')

    def tearDown(self):
        self.user_1.delete()

    def test_create_user_invalid_username_format(self):
        user = ''
        try:
            user = User.objects.create_user('emailtest_1@gmail.com', 'user espacio', 'testpassword')
        except ValueError as error:
            print(error)
        
        assert user == ''

    def test_create_user_email_empty(self):
        user = ''
        try:
            user = User.objects.create_user('', 'username1', 'testpassword')
        except ValueError as error:
            print(error)
        
        assert user == ''

    def test_create_user_email_invalid_format_1(self):
        user = ''
        try:
            user = User.objects.create_user('test', 'username1', 'testpassword')
        except ValueError as error:
            print(error)
        
        assert user == ''

    def test_create_user_email_invalid_format_2(self):
        user = ''
        try:
            user = User.objects.create_user('test@123', 'username1', 'testpassword')
        except ValueError as error:
            print(error)
        
        assert user == ''

    def test_create_user_email_invalid_format_3(self):
        user = ''
        try:
            user = User.objects.create_user('test@gmail,com', 'username1', 'testpassword')
        except ValueError as error:
            print(error)
        
        assert user == ''

    def test_create_user_email_valid(self):
        user = ''
        try:
            user = User.objects.create_user('test@gmail.com', 'username1', 'testpassword')
        except ValueError as error:
            print(error)
        
        assert user.email == 'test@gmail.com'