from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from accounts.models import Profile
from django.db.models import Q
from datetime import datetime

class TestLogin(TestCase):
    @classmethod
    def setUpTestData(cls):
        pass
           
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_post_login_user(self):
        User.objects.create_user(username='fred', email='test@test.com', password='secret')
        response = self.client.post('/accounts/login/', {
            "username_or_email": "fred",
            "password": "secret",
        })
        self.assertEqual(response.status_code, 302)

    def test_post_login_invalid_user(self):
        User.objects.create_user(username='fred', email='test@test.com', password='secret')
        response = self.client.post('/accounts/login/', {
            "username_or_email": "anonymous",
            "password": "secret",
        })
        self.assertEqual(response.status_code, 200)

class TestRegister(TestCase):
    @classmethod
    def setUpTestData(cls):
        pass

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/accounts/register/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get('/accounts/register/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_post_creates_user(self):
        response = self.client.post('/accounts/register/', {
            "username": "fred",
            "email": "test@test.com",
            "password1": "secret_password",
            "password2": "secret_password",
            "full_name": "Fred Scheffer",
            "birthdate": "2020-07-14",
            "phone_number": "999 999 9999",
            "country": "United States",
            "postcode": "2000",
            "town_or_city": "New York",
            "street_address1": "Wall Street 1",
            "street_address2": "",
        })
        self.assertEqual(response.status_code, 302)
        user = User.objects.get(username="fred")
        self.assertIsInstance(user, User)

    def test_post_user_form_not_valid(self):
        response = self.client.post('/accounts/register/', {
            "username": "fred",
            "email": "",
            "password1": "secret_password",
            "password2": "secret_password",
            "full_name": "Fred Scheffer",
            "birthdate": "2020-07-14",
            "phone_number": "999 999 9999",
            "country": "United States",
            "postcode": "2000",
            "town_or_city": "New York",
            "street_address1": "Wall Street 1",
            "street_address2": "",
        })
        self.assertEqual(response.status_code, 200)
        with self.assertRaises(User.DoesNotExist):
            user = User.objects.get(username="fred")

    def test_post_profile_form_not_valid(self):
        response = self.client.post('/accounts/register/', {
            "username": "fred",
            "email": "test@test.com",
            "password1": "secret_password",
            "password2": "secret_password",
            "full_name": "Fred Scheffer",
            "birthdate": "2020-07-14",
            "phone_number": "",
            "country": "United States",
            "postcode": "2000",
            "town_or_city": "New York",
            "street_address1": "Wall Street 1",
            "street_address2": "",
        })
        self.assertEqual(response.status_code, 200)
        with self.assertRaises(User.DoesNotExist):
            user = User.objects.get(username="fred")
        
class TestLogout(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(username='fred', email='test@test.com', password='secret')

    def test_logout(self):
        self.client.login(username='fred', password='secret')
        response = self.client.get('/accounts/logout/')
        self.assertEqual(response.status_code, 302)

class TestUpdate(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username='fred', email='test@test.com', password='secret')
        Profile.objects.create(
            user = user,
            birthdate = datetime(2003,9,20),
            full_name = "fred",
            phone_number = "+31 99 999 9999",
            country = "Netherlands",
            postcode = "9999 XX",
            town_or_city = "Kaasdonk",
            street_address1 = "Kerkstraat 1",
            street_address2 = "",
        )

    def test_view_url_exists_at_desired_location(self):
        self.client.login(username='fred', password='secret')
        response = self.client.get('/accounts/update/')
        self.assertEqual(response.status_code, 200)

    def test_not_logged_in_redirects_to_login(self):
        response = self.client.get('/accounts/update/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/accounts/login/?next=/accounts/update/")

    def test_view_uses_correct_template(self):
        self.client.login(username='fred', password='secret')
        response = self.client.get('/accounts/update/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'update.html')
