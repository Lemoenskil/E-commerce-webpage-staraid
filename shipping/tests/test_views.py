from django.test import TestCase
from django.urls import reverse
from shipping.models import Shipping

class TestShipping(TestCase):
    @classmethod
    def setUpTestData(cls):
        pass
           
    def test_post_adjust_region(self):
        Shipping.objects.create(
            name = "abs",
            price = 2.45,
        )
        response = self.client.post('/shipping/adjust_region/', {
            "selected_region": "abs",
        })
        self.assertEqual(response.status_code, 302)
