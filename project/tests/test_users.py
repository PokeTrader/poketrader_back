from project.tests.base import BaseTestCase
from project.api.users.models import User

class UsersSignupTest(BaseTestCase):
    def test_register_with_correct_fields_creates_user(self):
        users = User.query.all()
        self.assertEqual(len(users), 0)


        user_data = {
            'user': {
                'username': 'testuser',
                'password': 'somepass'
            }
        }

        response = self.client.post('/api/users/register', json=user_data)

        users = User.query.all()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(users), 1)

    def test_register_fails_without_username(self):
        user_data = {
            'user': {
                'password': 'somepass'
            }
        }

        response = self.client.post('/api/users/register', json=user_data)

        users = User.query.all()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(len(users), 0)

    def test_register_fails_without_password(self):
        user_data = {
            'user': {
                'username': 'someuser'
            }
        }

        response = self.client.post('/api/users/register', json=user_data)

        users = User.query.all()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(len(users), 0)
    
    def test_register_fails_with_invalid_password(self):
        user_data = {
            'user': {
                'username': 'someuser',
                'password': 'no'
            }
        }

        response = self.client.post('/api/users/register', json=user_data)

        users = User.query.all()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(len(users), 0)
    
    def test_register_fails_with_duplicate_username(self):
        user_data = {
            'user': {
                'username': 'someuser',
                'password': 'somepass'
            }
        }

        response = self.client.post('/api/users/register', json=user_data)

        users = User.query.all()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(users), 1)

        user_data = {
            'user': {
                'username': 'someuser',
                'password': 'somepass'
            }
        }

        response = self.client.post('/api/users/register', json=user_data)

        users = User.query.all()

        self.assertEqual(len(users), 1)
        self.assertEqual(response.status_code, 400)


class UsersSigninTest(BaseTestCase):
    def create_user(self):
        user_data = {
            'user': {
                'username': 'someuser',
                'password': 'somepassword'
            }
        }

        self.client.post('/api/users/register', json=user_data)

    def test_signin_with_valid_credentials_authenticates_user(self):
        self.create_user()

        user_data = {
            'user': {
                'username': 'someuser',
                'password': 'somepassword'
            }
        }

        response = self.client.post('/api/users/signin', json=user_data)

        self.assertEqual(response.status_code, 201)
        self.assertTrue("token" in response.json)

    def test_signin_fails_with_incorrect_password(self):
        self.create_user()

        user_data = {
            'user': {
                'username': 'someuser',
                'password': 'wrongpass'
            }
        }

        response = self.client.post('/api/users/signin', json=user_data)

        self.assertEqual(response.status_code, 401)
        self.assertFalse("token" in response.json)

    def test_signin_fails_with_incorrect_username(self):
        self.create_user()

        user_data = {
            'user': {
                'username': 'baduser',
                'password': 'wrongpass'
            }
        }

        response = self.client.post('/api/users/signin', json=user_data)

        self.assertEqual(response.status_code, 401)
        self.assertFalse("token" in response.json)