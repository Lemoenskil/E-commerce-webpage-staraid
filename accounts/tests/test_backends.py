from django.test import TestCase
from django.contrib.auth.models import User

from accounts.backends import CaseInsensitiveAuth

class TestCaseInsensitiveAuth(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user("booboo", email="where@ever.com", password="baabaabaa")

    def setUp(self):
        self.caseInsensitiveAuth = CaseInsensitiveAuth()

    def test_authenticate_username_good_password(self):
        user = self.caseInsensitiveAuth.authenticate("booboo", password="baabaabaa")
        self.assertIsInstance(user, User)

    def test_authenticate_email_good_password(self):
        user = self.caseInsensitiveAuth.authenticate("where@ever.com", password="baabaabaa")
        self.assertIsInstance(user, User)

    def test_authenticate_fails_bad_password(self):
        user = self.caseInsensitiveAuth.authenticate("where@ever.com", password="wrong!!")
        self.assertIsNone(user)

    def test_authenticate_fails_non_existent_user(self):
        user = self.caseInsensitiveAuth.authenticate("anonymous", password="baabaabaa")
        self.assertIsNone(user)

    def test_get_user(self):
        user = self.caseInsensitiveAuth.get_user(user_id=1)
        self.assertIsInstance(user, User)

    def test_get_user(self):
        user = self.caseInsensitiveAuth.get_user(user_id=1)
        self.assertIsInstance(user, User)

    def test_get_user_fails_for_missing_user(self):
        user = self.caseInsensitiveAuth.get_user(user_id=2)
        self.assertIsNone(user)
        
