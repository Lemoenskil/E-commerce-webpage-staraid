from django.test import TestCase
from datetime import datetime
from checkout.models import Order, OrderLineItem
from products.models import Product

class TestOrder(TestCase):
    @classmethod
    def setUpTestData(cls):
        Order.objects.create(
            full_name = "Snippie Smith",
            phone_number = "+31 99 999 9999",
            country = "Netherlands",
            postcode = "9999 XX",
            town_or_city = "Kaasdonk",
            street_address1 = "Kerkstraat 1",
            street_address2 = "",
            date = datetime(2003,9,20),
        )
        

    def setUp(self):
        self.order = Order.objects.get(id=1)
    
    def assertLabelIs(self, field_name, label):
        field_label = self.order._meta.get_field(field_name).verbose_name
        self.assertEquals(field_label, label)

    def test_full_name_label(self):
        self.assertLabelIs("full_name", "full name")

    def test_phone_number_label(self):
        self.assertLabelIs("phone_number", "phone number")

    def test_country_label(self):
        self.assertLabelIs("country", "country")

    def test_postcode_label(self):
        self.assertLabelIs("postcode", "postcode")

    def test_town_or_city_label(self):
        self.assertLabelIs("town_or_city", "town or city")

    def test_street_address1_label(self):
        self.assertLabelIs("street_address1", "street address1")

    def test_street_address2_label(self):
        self.assertLabelIs("street_address2", "street address2")

class TestOrderLineItem(TestCase):
    @classmethod
    def setUpTestData(cls):
        product = Product.objects.create(
            name = "abs",
            description = "description1",
            long_description = "this is a lonnnnnng description",
            features = "feature 1 and feature 2",
            price = 2.45,
            featured = True,
            stock = 9,
            on_offer = False,  
        )
        order = Order.objects.create(
            full_name = "Snippie Smith",
            phone_number = "+31 99 999 9999",
            country = "Netherlands",
            postcode = "9999 XX",
            town_or_city = "Kaasdonk",
            street_address1 = "Kerkstraat 1",
            street_address2 = "",
            date = datetime(2003,9,20),
        )
        OrderLineItem.objects.create(
            order = order,
            product = product,
            quantity = 1,
        )
        

    def setUp(self):
        self.orderLineItem = OrderLineItem.objects.get(id=1)
    
    def assertLabelIs(self, field_name, label):
        field_label = self.orderLineItem._meta.get_field(field_name).verbose_name
        self.assertEquals(field_label, label)

    def test_quantity_label(self):
        self.assertLabelIs("quantity", "quantity")

