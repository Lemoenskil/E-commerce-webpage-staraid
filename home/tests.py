from django.test import TestCase

class TestHome(TestCase):
    @classmethod
    def setUpTestData(cls):
        pass
           
    def test_home_url_exists_at_desired_location(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)