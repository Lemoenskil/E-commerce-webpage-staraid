from django.test import TestCase
from checkout.models import Order, OrderLineItem 
from products.models import Product
from datetime import datetime
from django.contrib.auth.models import User
from accounts.models import Profile
from checkout.forms import MakePaymentForm, OrderForm

class TestOrder(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(
            username='fred',
            email='test@test.com',
            password='secret'
        )
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
        
    def test_view_url_redirects_to_login_if_not_logged_in(self):
        response = self.client.get('/checkout/')
        self.assertRedirects(response, '/accounts/login/?next=/checkout/')
           
    def test_view_url_exists_at_desired_location(self):
        self.client.login(username='fred', password='secret')
        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        self.client.login(username='fred', password='secret')
        response = self.client.get('/checkout/')
        self.assertTemplateUsed(response, 'checkout.html')

