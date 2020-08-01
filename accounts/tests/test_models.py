from django.test import TestCase
from datetime import datetime
from django.contrib.auth.models import User

from accounts.models import Profile

class TestProfile(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user("snippie")
        Profile.objects.create(
            user = user,
            birthdate = datetime(2003,9,20),
            full_name = "Snippie Smith",
            phone_number = "+31 99 999 9999",
            country = "Netherlands",
            postcode = "9999 XX",
            town_or_city = "Kaasdonk",
            street_address1 = "Kerkstraat 1",
            street_address2 = "",
        )

    def setUp(self):
        self.profile = Profile.objects.get(id=1)
    
    def assertLabelIs(self, field_name, label):
        field_label = self.profile._meta.get_field(field_name).verbose_name
        self.assertEquals(field_label, label)

    def test_birthdate_label(self):
        self.assertLabelIs("birthdate", "birthdate")

    def test_full_name_label(self):
        self.assertLabelIs("full_name", "fullname")

    def test_phone_number_label(self):
        self.assertLabelIs("phone_number", "phone number")

    def test_country_label(self):
        self.assertLabelIs("country", "country")

    def test_postcode_label(self):
        self.assertLabelIs("postcode", "postcode")

    def test_town_or_city_label(self):
        self.assertLabelIs("town_or_city", "town or city")

    def test_street_address1_label(self):
        self.assertLabelIs("street_address1", "street address 1")

    def test_street_address2_label(self):
        self.assertLabelIs("street_address2", "street address 2")
