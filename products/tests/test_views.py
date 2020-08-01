from django.test import TestCase
from products.models import Product, ProductSpecification

class TestProducts(TestCase):
    @classmethod
    def setUpTestData(cls):
        Product.objects.create(
            name = "abs",
            description = "description1",
            long_description = "this is a lonnnnnng description",
            features = "feature 1 and feature 2",
            price = 2.45,
            featured = True,
            stock = 9,
            on_offer = False,  
        )
           
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products.html')


class TestSingleProduct(TestCase):
    @classmethod
    def setUpTestData(cls):
        Product.objects.create(
            name = "abs",
            description = "description1",
            long_description = "this is a lonnnnnng description",
            features = "feature 1 and feature 2",
            price = 2.45,
            featured = True,
            stock = 9,
            on_offer = False,  
        )

    def setUp(self):
        self.product = Product.objects.get()

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get(f'/products/{self.product.id}')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(f'/products/{self.product.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'single_product.html')
