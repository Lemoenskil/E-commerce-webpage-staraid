from django.test import TestCase
from django.urls import reverse
from decimal import Decimal
from django.db.models.query import QuerySet
from products.models import Product
from shipping.models import Shipping
from cart.views import add_to_cart, adjust_cart
from shipping.views import adjust_region
from django.shortcuts import reverse
from urllib.parse import urlencode

class TestCart(TestCase):
    @classmethod
    def setUpTestData(cls):
        Product.objects.create(
            name = "dummy",
            description = "",
            long_description = "",
            features = "",
            price = 9.99,
            featured = False,
            stock = 1,
            on_offer = False,
        )
        Shipping.objects.create(
            name = "wherever",
            price = 1.00
        )
        Shipping.objects.create(
            name = "katmandu",
            price = 99.99
        )

    def setUp(self):
        self.product = Product.objects.get()
        self.wherever = Shipping.objects.get(id=1)
        self.katmandu = Shipping.objects.get(id=2)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart.html')

    def test_cart_contents_has_expected_properties(self):
        response = self.client.get('/cart/')
        self.assertIn('product_count', response.context)
        self.assertIsInstance(response.context['product_count'], int)
        self.assertIn('cart_items', response.context)
        self.assertIsInstance(response.context['cart_items'], list)
        self.assertIn('sub_total', response.context)
        self.assertIsInstance(response.context['sub_total'], Decimal)
        self.assertIn('total', response.context)
        self.assertIsInstance(response.context['total'], Decimal)
        self.assertIn('regions', response.context)
        self.assertIsInstance(response.context['regions'], QuerySet)
        self.assertIn('selected_region', response.context)
        self.assertIsInstance(response.context['selected_region'], str)
        self.assertIn('region_price', response.context)
        self.assertIsInstance(response.context['region_price'], Decimal)

    def test_empty_cart_contents(self):
        response = self.client.get('/cart/')
        self.assertEqual(response.context['product_count'], 0)
        self.assertEqual(response.context['cart_items'], [])
        self.assertEqual(response.context['sub_total'], 0)
        self.assertEqual(response.context['total'], self.wherever.price)
        self.assertEqual(response.context['selected_region'], self.wherever.name)
        self.assertEqual(response.context['region_price'], self.wherever.price)

    def test_one_item_cart_contents(self):
        self.client.post(reverse(add_to_cart, args=[self.product.id]))
        response = self.client.get('/cart/')
        self.assertEqual(response.context['product_count'], 1)
        self.assertEqual(len(response.context['cart_items']), 1)
        self.assertEqual(response.context['cart_items'][0]['id'], str(self.product.id))
        self.assertEqual(response.context['cart_items'][0]['quantity'], 1)
        self.assertEqual(response.context['cart_items'][0]['product'], self.product)
        self.assertEqual(response.context['cart_items'][0]['total'], self.product.price)
        self.assertEqual(response.context['sub_total'], self.product.price)
        self.assertEqual(response.context['total'], self.product.price + self.wherever.price)
        self.assertEqual(response.context['selected_region'], self.wherever.name)
        self.assertEqual(response.context['region_price'], self.wherever.price)

    def test_two_item_cart_contents(self):
        self.client.post(reverse(add_to_cart, args=[self.product.id]))
        self.client.post(reverse(add_to_cart, args=[self.product.id]))
        response = self.client.get('/cart/')
        self.assertEqual(response.context['product_count'], 2)
        self.assertEqual(len(response.context['cart_items']), 1)
        self.assertEqual(response.context['cart_items'][0]['id'], str(self.product.id))
        self.assertEqual(response.context['cart_items'][0]['quantity'], 2)
        self.assertEqual(response.context['cart_items'][0]['product'], self.product)
        self.assertEqual(response.context['cart_items'][0]['total'], 2 * self.product.price)
        self.assertEqual(response.context['sub_total'], 2 * self.product.price)
        self.assertEqual(response.context['total'], 2 * self.product.price + self.wherever.price)
        self.assertEqual(response.context['selected_region'], self.wherever.name)
        self.assertEqual(response.context['region_price'], self.wherever.price)

    def test_region_cart_contents(self):
        self.client.post(
            reverse(adjust_region),
            urlencode({
                'selected_region': 'katmandu'
            }),
            content_type="application/x-www-form-urlencoded"
        )
        response = self.client.get('/cart/')
        self.assertEqual(response.context['product_count'], 0)
        self.assertEqual(response.context['cart_items'], [])
        self.assertEqual(response.context['sub_total'], 0)
        self.assertEqual(response.context['total'], self.katmandu.price)
        self.assertEqual(response.context['selected_region'], self.katmandu.name)
        self.assertEqual(response.context['region_price'], self.katmandu.price)

    def test_adjust_cart(self):
        self.client.post(reverse(add_to_cart, args=[self.product.id]))
        self.client.post(
            reverse(adjust_cart, args=[self.product.id]),
            urlencode({
                'quantity' + str(self.product.id): 5
            }),
            content_type="application/x-www-form-urlencoded"
        )
        response = self.client.get('/cart/')
        self.assertEqual(response.context['product_count'], 5)
        self.assertEqual(len(response.context['cart_items']), 1)
        self.assertEqual(response.context['cart_items'][0]['id'], str(self.product.id))
        self.assertEqual(response.context['cart_items'][0]['quantity'], 5)
        self.assertEqual(response.context['cart_items'][0]['product'], self.product)
        self.assertEqual(response.context['cart_items'][0]['total'], 5 * self.product.price)
        self.assertEqual(response.context['sub_total'], 5 * self.product.price)
        self.assertEqual(response.context['total'], 5 * self.product.price + self.wherever.price)
        self.assertEqual(response.context['selected_region'], self.wherever.name)
        self.assertEqual(response.context['region_price'], self.wherever.price)

    def test_adjust_cart_to_zero(self):
        self.client.post(reverse(add_to_cart, args=[self.product.id]))
        self.client.post(
            reverse(adjust_cart, args=[self.product.id]),
            urlencode({
                'quantity' + str(self.product.id): 0
            }),
            content_type="application/x-www-form-urlencoded"
        )
        response = self.client.get('/cart/')
        self.assertEqual(response.context['product_count'], 0)
        self.assertEqual(len(response.context['cart_items']), 0)
        self.assertEqual(response.context['sub_total'], 0)
        self.assertEqual(response.context['total'], self.wherever.price)
        self.assertEqual(response.context['selected_region'], self.wherever.name)
        self.assertEqual(response.context['region_price'], self.wherever.price)
