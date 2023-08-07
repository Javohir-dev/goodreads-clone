from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse


class RegistrationTestCase(TestCase):
    def test_user_account_is_created(self):
        self.client.post(
            reverse("users:register"),
            data={
                "username": "salmonxon123", 
                "first_name": "salmonxon", 
                "last_name": "Khamidullaev", 
                "email": "salmonxon.py@gmail.com", 
                "password": "somepassword"
            }
        )

        user = User.objects.get(username='salmonxon123')

        self.assertEqual(user.first_name, "salmonxon")
        self.assertEqual(user.last_name, "Khamidullaev")
        self.assertEqual(user.email, "salmonxon.py@gmail.com")
        self.assertNotEqual(user.password, "anypassword")
        self.assertTrue(user.check_password, "anypassword")

    def test_required_field(self):
        response = self.client.post(
            reverse("users:register"),
            data={
                "first_name": "salmonxon", 
                "email": "salmonxon.py@gmail.com", 
            }
        )

        user_count = User.objects.count()

        self.assertEqual(user_count, 0)
        self.assertFormError(response, 'form', 'username', 'This field is required.')
        self.assertFormError(response, 'form', 'password', 'This field is required.')

    def test_invalid_email(self):
        response = self.client.post(
            reverse("users:register"),
            data={
                "username": "salmonxon123", 
                "first_name": "salmonxon", 
                "last_name": "Khamidullaev", 
                "email": "invalid-email", 
                "password": "somepassword"
            }
        )

        user_count = User.objects.count()

        self.assertEqual(user_count, 0)
        self.assertFormError(response, 'form', 'email', 'Enter a valid email address.')

    def test_unique_username(self):
        # 1. create a username
        user = User.objects.create(
            username="javohir",
            first_name="javohir",
            last_name="khamidullev",
            email="javohir.py@gmail.com",
        )
        user.set_password("somepassword")
        user.save()

        # 2. try to create another user with that same username 
        response = self.client.post(
            reverse("users:register"),
            data={
                "username": "javohir", 
                "first_name": "javohir", 
                "last_name": "khamidullev", 
                "email": "javohir.py@gmail.com", 
                "password": "somepassword"
            }
        )

        # 3. check that the second user was not created
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)

        # 4. check that the form contains error message
        self.assertFormError(response, 'form', 'username', 'A user with that username already exists.')



        


        
