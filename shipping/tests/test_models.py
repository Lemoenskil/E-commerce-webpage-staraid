from django.test import TestCase
from shipping.models import Shipping

# Create your tests here.
class TestShipping(TestCase):
    @classmethod
    def setUpTestData(cls):
        Shipping.objects.create(
            name = "abs",
            price = 2.45,
        )
    
    def setUp(self):
        self.shipping = Shipping.objects.get(id=1)
    
    def assertLabelIs(self, field_name, label):
        field_label = self.shipping._meta.get_field(field_name).verbose_name
        self.assertEquals(field_label, label)

    def test_name_label(self):
        self.assertLabelIs("name", "name")

    def test_price_label(self):
        self.assertLabelIs("price", "price")